#!/usr/bin/env python3
"""Compose the release title from the live Firefox version data.

    python3 scripts/release_title.py 8.4
    -> Policy templates for Firefox 158 and Firefox ESR 153.5 (Version 8.4)

Matches the format used from v8.2 onwards. Reads
https://product-details.mozilla.org/1.0/firefox_versions.json so the title
reflects the versions current at release time rather than anything hard-coded.

Falls back to a version-only title if the fetch or parse fails, so a network
blip can't break a release.
"""

import json
import re
import sys
import urllib.request

URL = 'https://product-details.mozilla.org/1.0/firefox_versions.json'
TIMEOUT = 30


def firefox_major(v):
    """158.0 -> 158, 156.0.1 -> 156"""
    m = re.match(r'(\d+)', v or '')
    return m.group(1) if m else None


def esr_version(v):
    """153.5.0esr -> 153.5, 153.0esr -> 153, 140.12.0esr -> 140.12

    Drops the 'esr' suffix, then a trailing '.0' - matching how past titles
    rendered it ("Firefox ESR 153" for 153.0esr, "Firefox ESR 153.1" for
    153.1.0esr).
    """
    if not v:
        return None
    v = re.sub(r'esr$', '', v.strip())
    v = re.sub(r'\.0$', '', v)
    return v or None


def pick_esr(data):
    """Prefer ESR_NEXT during an ESR overlap, else the current ESR.

    While two ESR lines are supported, product-details puts the newer one in
    FIREFOX_ESR_NEXT - that's the line the templates track, and it's what v8.3's
    title quoted. Outside an overlap ESR_NEXT is an empty string.
    """
    return esr_version(data.get('FIREFOX_ESR_NEXT')) or esr_version(data.get('FIREFOX_ESR'))


def compose(version, data):
    ff = firefox_major(data.get('LATEST_FIREFOX_VERSION'))
    esr = pick_esr(data)
    if not ff or not esr:
        raise ValueError('missing version data: ff=%r esr=%r' % (ff, esr))
    return ('Policy templates for Firefox %s and Firefox ESR %s (Version %s)'
            % (ff, esr, version))


def main():
    if len(sys.argv) < 2:
        sys.exit('usage: release_title.py <version>   e.g. 8.4')
    version = sys.argv[1].lstrip('v')
    try:
        with urllib.request.urlopen(URL, timeout=TIMEOUT) as r:
            data = json.loads(r.read().decode('utf-8'))
        print(compose(version, data))
    except Exception as e:
        # Never fail the release over this - fall back to a version-only title.
        print('Firefox Policy Templates Version %s' % version)
        print('release_title: falling back, %s: %s' % (type(e).__name__, e),
              file=sys.stderr)


if __name__ == '__main__':
    main()
