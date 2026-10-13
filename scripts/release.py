#!/usr/bin/env python3
"""Cut a policy-templates release.

Does the things that are easy to forget - pull, confirm the tree is clean and in
sync, show what actually changed since the last release - then creates and pushes
the tag that triggers .github/workflows/release.yml. The workflow does the rest:
bumps the revision attributes, regenerates docs/oma-uris.md, zips the templates
and opens a draft release.

    python scripts/release.py              # next minor, with confirmation
    python scripts/release.py 9.0          # explicit version
    python scripts/release.py --dry-run    # show what would happen
    python scripts/release.py -y           # skip the confirmation prompt

Forgetting to pull before tagging broke two releases in a row, so that check is
the whole point of this script.
"""

import argparse
import os
import re
import subprocess
import sys

# Files whose contents an admin actually consumes. docs/oma-uris.md is generated
# at release time and the revision attributes are bumped by the workflow, so
# neither counts as a reason to cut a release.
TEMPLATE_FILES = [
    'windows/firefox.admx',
    'windows/en-US/firefox.adml',
    'windows/de-DE/firefox.adml',
    'windows/fr-FR/firefox.adml',
    'windows/ru-RU/firefox.adml',
    'linux/policies.json',
    'mac/org.mozilla.firefox.plist',
]

ACTIONS_URL = 'https://github.com/mozilla/policy-templates/actions/workflows/release.yml'


class Abort(Exception):
    pass


def git(*args, check=True):
    r = subprocess.run(['git'] + list(args), capture_output=True, text=True)
    if check and r.returncode != 0:
        raise Abort('git %s failed:\n%s' % (' '.join(args), (r.stderr or r.stdout).strip()))
    return r.stdout.strip()


def repo_root():
    try:
        return git('rev-parse', '--show-toplevel')
    except Abort:
        raise Abort('Not inside a git repository.')


def current_revision():
    with open('windows/firefox.admx', encoding='utf-8') as f:
        head = f.read(4096)
    m = re.search(r'\brevision="([^"]+)"', head)
    if not m:
        raise Abort('Could not find the revision attribute in windows/firefox.admx.')
    return m.group(1)


def next_minor(rev):
    parts = rev.split('.')
    if len(parts) < 2 or not all(p.isdigit() for p in parts[:2]):
        raise Abort('Cannot auto-increment revision %r; pass the version explicitly.' % rev)
    return '%s.%d' % (parts[0], int(parts[1]) + 1)


def preflight():
    branch = git('rev-parse', '--abbrev-ref', 'HEAD')
    if branch != 'master':
        raise Abort('On branch %r. Releases are cut from master.' % branch)

    if git('status', '--porcelain'):
        raise Abort('Working tree is not clean. Commit or stash first:\n'
                    + git('status', '--short'))

    print('Fetching origin...')
    # --force matters. The release workflow re-points each tag at the version-bump
    # commit it creates, so the local tag this script pushed is left one commit
    # behind origin's. Without --force, git refuses to update it ("would clobber
    # existing tag"), fails the whole fetch, and blocks every later release.
    # Origin is authoritative for released tags, so take its version.
    git('fetch', 'origin', '--tags', '--force', '--prune')

    ahead = git('rev-list', '--count', 'origin/master..HEAD')
    behind = git('rev-list', '--count', 'HEAD..origin/master')
    if ahead != '0':
        raise Abort('Local master has %s commit(s) not on origin. Push or reset first.' % ahead)
    if behind != '0':
        print('  master was %s commit(s) behind; fast-forwarding.' % behind)
        git('merge', '--ff-only', 'origin/master')
    else:
        print('  master is up to date.')


def open_prs():
    """Best-effort warning about open PRs, so a nearly-ready change isn't missed."""
    r = subprocess.run(['gh', 'pr', 'list', '--state', 'open', '--limit', '20',
                        '--json', 'number,title'], capture_output=True, text=True)
    if r.returncode != 0:
        return None
    try:
        import json
        return json.loads(r.stdout)
    except ValueError:
        return None


def last_tag():
    try:
        return git('describe', '--tags', '--abbrev=0')
    except Abort:
        return None


def tag_exists(tag):
    local = git('tag', '-l', tag)
    remote = git('ls-remote', '--tags', 'origin', 'refs/tags/' + tag, check=False)
    return bool(local), bool(remote)


def summarize(prev):
    if not prev:
        print('\nNo previous tag found; cannot summarize.')
        return True

    rng = '%s..HEAD' % prev
    commits = git('log', '--no-merges', '--format=%h %s', rng)
    print('\nCommits since %s:' % prev)
    print('  ' + ('\n  '.join(commits.splitlines()) if commits else '(none)'))

    changed = git('diff', '--name-only', rng, '--', *TEMPLATE_FILES)
    changed = [c for c in changed.splitlines() if c]
    print('\nTemplate files changed since %s:' % prev)
    if changed:
        for c in changed:
            print('  %s' % c)
    else:
        print('  (none)')
    return bool(changed)


def main():
    ap = argparse.ArgumentParser(description='Cut a policy-templates release.')
    ap.add_argument('version', nargs='?', help='Version without the leading v (e.g. 8.2). '
                                               'Defaults to the next minor.')
    ap.add_argument('-n', '--dry-run', action='store_true', help='Show what would happen.')
    ap.add_argument('-y', '--yes', action='store_true', help='Skip the confirmation prompt.')
    args = ap.parse_args()

    os.chdir(repo_root())
    preflight()

    rev = current_revision()
    version = (args.version or next_minor(rev)).lstrip('v')
    tag = 'v' + version

    print('\nCurrent revision in firefox.admx: %s' % rev)
    print('Releasing as:                     %s' % tag)

    local, remote = tag_exists(tag)
    if local or remote:
        where = ' and '.join(w for w, y in [('locally', local), ('on origin', remote)] if y)
        raise Abort('Tag %s already exists %s. Pick another version, or delete it:\n'
                    '  git push origin :refs/tags/%s\n  git tag -d %s' % (tag, where, tag, tag))

    prev = last_tag()
    if not summarize(prev):
        print('\nNote: no template files changed since %s. Releases are cut when the\n'
              'templates change, so consider whether this release is needed.' % prev)

    prs = open_prs()
    if prs:
        print('\nOpen pull requests - merge anything that belongs in this release first,\n'
              'then re-run. Merging after tagging is what breaks the workflow:')
        for p in prs:
            print('  #%d %s' % (p['number'], p['title']))

    print('\nWill run:')
    print('  git tag -m "%s" %s' % (tag, tag))
    print('  git push origin %s' % tag)

    if args.dry_run:
        print('\nDry run; nothing done.')
        return 0

    if not args.yes:
        try:
            if input('\nProceed? [y/N] ').strip().lower() not in ('y', 'yes'):
                print('Aborted.')
                return 1
        except EOFError:
            raise Abort('No terminal for confirmation. Re-run with -y.')

    git('tag', '-m', tag, tag)
    git('push', 'origin', tag)
    print('\nPushed %s. Watch the run:\n  %s' % (tag, ACTIONS_URL))
    print('\nDo not merge anything until it finishes. When the draft release appears,\n'
          'set its title and notes, then publish.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Abort as e:
        print('\nerror: %s' % e, file=sys.stderr)
        sys.exit(1)
