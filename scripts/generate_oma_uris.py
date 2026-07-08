#!/usr/bin/env python3
"""Generate an OMA-URI reference for every policy in windows/firefox.admx.

Output is Markdown on stdout. Intended to be run from the repo root:

    python scripts/generate_oma_uris.py > oma-uris.md

The generator walks the ADMX category tree to build each policy's URI path
and emits a best-effort value template based on the policy's element type.
Policies whose value is a JSON blob (multiText, JSON-flavored text) get a
placeholder that points readers back to the docs page for the schema.

Display names are resolved from the en-US ADML so entries appear under their
GPMC label ("Bookmarks (JSON)") rather than the raw ADMX policy name
("A_Bookmarks"). Policies marked "(Deprecated)" in the ADML are skipped, and
numbered families (e.g. Bookmark01-Bookmark50) are collapsed into a single
entry.
"""
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

MOZILLA_ROOT = "Mozilla:Cat_Mozilla"
ADMX_PATH = Path("windows/firefox.admx")
ADML_PATH = Path("windows/en-US/firefox.adml")
SAMPLE_JSON_PATH = Path("linux/policies.json")

# NS is detected at runtime from the parsed root element so this works
# whether or not firefox.admx declares the standard ADMX namespace.
NS = ""

# Policies whose value is a raw JSON blob. We can't synthesize meaningful
# values for these; readers must consult the docs page for shape.
JSON_POLICIES = {
    "AutoLaunchProtocolsFromOrigins",
    "AutoLaunchProtocolsFromOriginsOneLine",
    "A_Bookmarks",
    "A_BookmarksOneLine",
    "Containers",
    "ContainersOneLine",
    "ExemptDomainFileTypePairsFromFileTypeDownloadWarnings",
    "ExemptDomainFileTypePairsFromFileTypeDownloadWarningsOneLine",
    "ExtensionSettings",
    "ExtensionSettingsOneLine",
    "Handlers",
    "HandlersOneLine",
    "ManagedBookmarks",
    "ManagedBookmarksOneLine",
    "Preferences",
    "PreferencesOneLine",
    "WebsiteFilter",
    "WebsiteFilterOneLine",
}


def load_json_samples(path: Path) -> dict[str, str]:
    """Extract each top-level policy value from linux/policies.json as text.

    The file isn't strict JSON (it uses "true | false" placeholders), so we
    scan it as text and use brace/bracket depth to find the end of each
    top-level policy value. Returned strings preserve original formatting
    so admins can see the structure and any pseudo-JSON hints.
    """
    text = path.read_text(encoding="utf-8")
    samples: dict[str, str] = {}

    m = re.search(r'"policies"\s*:\s*\{', text)
    if not m:
        return samples
    i, n = m.end(), len(text)

    while i < n:
        # skip whitespace and commas between entries
        while i < n and text[i] in ' \t\r\n,':
            i += 1
        if i >= n or text[i] == '}':
            break
        if text[i] != '"':
            i += 1
            continue
        # read key
        j = i + 1
        while j < n and text[j] != '"':
            if text[j] == '\\':
                j += 2
                continue
            j += 1
        key = text[i + 1 : j]
        i = j + 1
        # skip whitespace + colon
        while i < n and text[i] in ' \t\r\n:':
            i += 1
        if i >= n:
            break
        value_start = i
        if text[i] in '{[':
            open_c = text[i]
            close_c = '}' if open_c == '{' else ']'
            depth = 0
            in_str = False
            while i < n:
                c = text[i]
                if in_str:
                    if c == '\\':
                        i += 2
                        continue
                    if c == '"':
                        in_str = False
                elif c == '"':
                    in_str = True
                elif c == open_c:
                    depth += 1
                elif c == close_c:
                    depth -= 1
                    if depth == 0:
                        i += 1
                        break
                i += 1
            samples[key] = _dedent_sample(text[value_start:i])
        else:
            # scalar value - read to end of line or trailing comma
            while i < n and text[i] not in ',\r\n':
                i += 1
            samples[key] = text[value_start:i].strip()
    return samples


def _dedent_sample(value: str) -> str:
    """Strip the outer 4-space indent that linux/policies.json uses.

    Keeps the opening bracket on the first line intact; only trims
    subsequent lines to the minimum common indent so the JSON reads
    cleanly when embedded in the OMA-URI value block.
    """
    lines = value.split("\n")
    if len(lines) < 2:
        return value
    body = lines[1:]
    indents = [
        len(line) - len(line.lstrip(" "))
        for line in body
        if line.strip()
    ]
    if not indents:
        return value
    strip_n = min(indents)
    dedented = [lines[0]] + [
        (line[strip_n:] if len(line) >= strip_n else line) for line in body
    ]
    return "\n".join(dedented)


def load_adml_strings(path: Path) -> dict[str, str]:
    """Return {string_id: display_text} from an ADML file."""
    root = ET.parse(path).getroot()
    ns = "{" + root.tag.split("}")[0][1:] + "}" if "}" in root.tag else ""
    return {s.get("id"): (s.text or "").strip() for s in root.findall(f".//{ns}string")}


def resolve_display(display_attr: str | None, strings: dict[str, str]) -> str:
    """Turn a '$(string.Foo)' reference into the ADML text for 'Foo'."""
    if display_attr and display_attr.startswith("$(string.") and display_attr.endswith(")"):
        key = display_attr[len("$(string."):-1]
        return strings.get(key, display_attr)
    return display_attr or ""


def build_category_map(root: ET.Element) -> dict[str, str | None]:
    """Return {category_name: parent_ref}."""
    cats: dict[str, str | None] = {}
    for cat in root.findall(f".//{NS}category"):
        name = cat.get("name")
        parent = cat.find(f"{NS}parentCategory")
        cats[name] = parent.get("ref") if parent is not None else None
    return cats


def build_category_display_map(
    root: ET.Element, strings: dict[str, str]
) -> dict[str, str]:
    """Return {category_name: resolved_display_name}."""
    return {
        cat.get("name"): resolve_display(cat.get("displayName"), strings)
        for cat in root.findall(f".//{NS}category")
    }


def category_chain(cat_ref: str | None, cat_map: dict[str, str | None]) -> list[str]:
    """Walk up from cat_ref, stopping at (and excluding) the Mozilla root."""
    chain: list[str] = []
    current = cat_ref
    seen: set[str] = set()
    while current and current != MOZILLA_ROOT and current not in seen:
        seen.add(current)
        if ":" in current:
            break
        chain.append(current)
        current = cat_map.get(current)
    return list(reversed(chain))


REGISTRY_PREFIX = r"Software\Policies\Mozilla\Firefox"


def json_policy_name(policy: ET.Element) -> str:
    """Derive the JSON policies.json key path for a policy.

    Rules:
    - Base path = policy's `key` attribute with the standard Firefox prefix
      stripped, converted from backslash-separated to dot-separated.
    - If the policy has a `valueName`, that's the leaf.
    - Else if there's a single `list`/`multiText` element with a `valueName`
      or a `key` that extends the base, that becomes the leaf.
    - Otherwise the base path alone is the JSON name (composite/object policy).
    """
    key = policy.get("key", "")
    if key.startswith(REGISTRY_PREFIX):
        base = key[len(REGISTRY_PREFIX):].lstrip("\\")
    else:
        base = key
    base_parts = [p for p in base.split("\\") if p]

    value_name = policy.get("valueName")
    if value_name:
        return ".".join(base_parts + [value_name])

    elements_el = policy.find(f"{NS}elements")
    if elements_el is not None:
        children = list(elements_el)
        if len(children) == 1:
            el = children[0]
            el_vn = el.get("valueName")
            if el_vn:
                return ".".join(base_parts + [el_vn])
            el_key = el.get("key")
            if el_key and el_key.startswith(REGISTRY_PREFIX):
                el_key_parts = [
                    p for p in el_key[len(REGISTRY_PREFIX):].lstrip("\\").split("\\") if p
                ]
                if len(el_key_parts) > len(base_parts):
                    return ".".join(el_key_parts)

    # Composite policy (multiple children each with their own valueName) or
    # nothing to append — the base path is the JSON name.
    return ".".join(base_parts) if base_parts else policy.get("name", "")


def enum_values(enum_el: ET.Element) -> list[str]:
    values: list[str] = []
    for item in enum_el.findall(f"{NS}item"):
        value = item.find(f"{NS}value")
        if value is None:
            continue
        s = value.find(f"{NS}string")
        if s is not None and s.text is not None:
            values.append(s.text)
            continue
        d = value.find(f"{NS}decimal")
        if d is not None:
            values.append(d.get("value", "0"))
    return values


def format_value_template(policy: ET.Element, samples: dict[str, str]) -> str:
    name = policy.get("name")
    if name in JSON_POLICIES:
        # Look up the JSON sample by the derived JSON policy name (e.g.
        # "Bookmarks" for both A_Bookmarks and A_BookmarksOneLine).
        json_name = json_policy_name(policy)
        sample = samples.get(json_name)
        # Distinguish the OneLine variant (uses a single <text> element) from
        # the multi-line variant (uses <multiText>). The OneLine variant
        # points readers to the multi-line entry rather than repeating the
        # sample on one line.
        elements_el = policy.find(f"{NS}elements")
        is_oneline = False
        if elements_el is not None:
            children = list(elements_el)
            if children:
                tag = children[0].tag.split("}")[-1]
                is_oneline = tag == "text"

        data_id = "JSONOneLine" if is_oneline else "JSON"
        if sample and not is_oneline:
            return f"<enabled/>\n<data id=\"{data_id}\" value='\n{sample}'/>"
        if is_oneline:
            empty = "[]" if sample and sample.lstrip().startswith("[") else "{}"
            return (
                f"<enabled/>\n<data id=\"{data_id}\" value='{empty}'/>\n"
                f"(Put the same JSON as the `{json_name}` entry above on a "
                "single line here. This variant exists to work around "
                "Intune's per-string length limit.)"
            )
        # No sample and not oneline — fall back to placeholder.
        return (
            "<enabled/>\n"
            f'<data id="{data_id}" value=\'... JSON - see policy docs for schema ...\'/>'
        )

    elements = policy.find(f"{NS}elements")
    enabled = policy.find(f"{NS}enabledValue") is not None
    disabled = policy.find(f"{NS}disabledValue") is not None

    if enabled and disabled and (elements is None or len(list(elements)) == 0):
        return "<enabled/> or <disabled/>"

    if elements is None or len(list(elements)) == 0:
        return "<enabled/>"

    lines = ["<enabled/>"]
    for el in elements:
        tag = el.tag.split("}")[-1]
        el_id = el.get("id", "")
        if tag == "boolean":
            lines.append(f'<data id="{el_id}" value="true | false"/>')
        elif tag == "text":
            lines.append(f'<data id="{el_id}" value="STRING"/>')
        elif tag == "decimal":
            lines.append(f'<data id="{el_id}" value="0"/>')
        elif tag == "enum":
            values = enum_values(el) or ["VALUE"]
            lines.append(f'<data id="{el_id}" value="{" | ".join(values)}"/>')
        elif tag == "list":
            lines.append(
                f'<data id="{el_id}" '
                'value="1&#xF000;value1&#xF000;2&#xF000;value2"/>'
            )
        elif tag == "multiText":
            lines.append(
                f'<data id="{el_id}" value=\'... JSON - see policy docs for schema ...\'/>'
            )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Numbered-family collapsing
# ---------------------------------------------------------------------------

# Matches a policy name that ends in digits, capturing the (base, digits).
# We require at least one non-digit character before the digits so we don't
# treat pure-numeric names as a family.
NUMBERED_RE = re.compile(r"^(.+?)(\d+)$")


def numbered_base(name: str) -> tuple[str, str] | None:
    """Return (base, digits) if the name ends in digits; else None."""
    m = NUMBERED_RE.match(name)
    if not m:
        return None
    base, digits = m.group(1), m.group(2)
    # Reject names where the base is empty or all separators.
    if not re.search(r"[A-Za-z]", base):
        return None
    return base, digits


def range_display(first_display: str, last_display: str) -> str:
    """Format a range heading like 'Bookmark 01 - Bookmark 50'."""
    if first_display == last_display:
        return first_display
    return f"{first_display} - {last_display}"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    if not ADMX_PATH.exists():
        print(f"error: {ADMX_PATH} not found (run from repo root)", file=sys.stderr)
        return 1
    if not ADML_PATH.exists():
        print(f"error: {ADML_PATH} not found (run from repo root)", file=sys.stderr)
        return 1

    root = ET.parse(ADMX_PATH).getroot()
    revision = root.get("revision", "unknown")

    global NS
    if "}" in root.tag:
        NS = "{" + root.tag.split("}")[0][1:] + "}"

    strings = load_adml_strings(ADML_PATH)
    samples = load_json_samples(SAMPLE_JSON_PATH) if SAMPLE_JSON_PATH.exists() else {}
    cat_map = build_category_map(root)
    cat_display = build_category_display_map(root, strings)

    def breadcrumb_for(display: str, chain: list[str]) -> str:
        # Skip the top-level `firefox` category — it's just the app name and
        # every policy is under it. Anything deeper becomes a breadcrumb.
        crumbs = [cat_display.get(c, c) for c in chain if c != "firefox"]
        return " > ".join(crumbs + [display]) if crumbs else display

    # Collect one entry per policy. Later we group numbered families.
    entries: list[dict] = []
    for policy in root.findall(f".//{NS}policy"):
        name = policy.get("name")
        display = resolve_display(policy.get("displayName"), strings)
        if "deprecated" in display.lower():
            continue

        parent_el = policy.find(f"{NS}parentCategory")
        parent_ref = parent_el.get("ref") if parent_el is not None else None
        chain = category_chain(parent_ref, cat_map)

        # Also skip when any parent category is marked deprecated (e.g. the
        # entire old "Preferences (Deprecated)" tree).
        if any("deprecated" in cat_display.get(c, "").lower() for c in chain):
            continue
        cat_path = "~".join(chain) if chain else "firefox"
        uri = f"./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~{cat_path}/{name}"
        value = format_value_template(policy, samples)
        breadcrumb = breadcrumb_for(display, chain)
        json_name = json_policy_name(policy)

        entries.append(
            {
                "name": name,
                "display": display,
                "json_name": json_name,
                "breadcrumb": breadcrumb,
                "uri": uri,
                "value": value,
                "cat_path": cat_path,
                "chain": chain,
            }
        )

    # Group numbered families. Family key: (base, cat_path, value template).
    families: dict[tuple[str, str, str], list[dict]] = {}
    singles: list[dict] = []
    for e in entries:
        numbered = numbered_base(e["name"])
        if numbered is None:
            singles.append(e)
            continue
        base, _digits = numbered
        key = (base, e["cat_path"], e["value"])
        families.setdefault(key, []).append(e)

    # Families with only one member are really just singletons.
    collapsed: list[dict] = list(singles)
    for members in families.values():
        if len(members) == 1:
            collapsed.append(members[0])
            continue
        members.sort(key=lambda m: m["name"])
        first, last = members[0], members[-1]
        base = numbered_base(first["name"])[0]
        placeholder_name = f"{base}NN"
        collapsed_display = range_display(first["display"], last["display"])
        # For a numbered family the JSON name usually ends in a digit that
        # comes from a registry subkey (e.g. Bookmarks.1). Show that as [N]
        # in the collapsed heading. If the JSON leaf isn't numeric, fall
        # back to the family name.
        family_json = first["json_name"]
        m = re.match(r"^(.+?)\.\d+$", family_json)
        collapsed_json = f"{m.group(1)}[N]" if m else family_json
        collapsed.append(
            {
                "name": placeholder_name,
                "display": collapsed_display,
                "json_name": collapsed_json,
                "breadcrumb": breadcrumb_for(collapsed_display, first["chain"]),
                "uri": (
                    f"./Device/Vendor/MSFT/Policy/Config/"
                    f"Firefox~Policy~{first['cat_path']}/{placeholder_name}"
                ),
                "value": first["value"],
                "cat_path": first["cat_path"],
                "chain": first["chain"],
                "range_note": (
                    f"Replace `NN` with the numeric suffix from `{first['name']}` "
                    f"through `{last['name']}` ({len(members)} slots)."
                ),
            }
        )

    collapsed.sort(key=lambda e: e["json_name"].lower())

    out: list[str] = []
    out.append("# Firefox ADMX OMA-URIs for Intune")
    out.append("")
    out.append(
        f"Auto-generated from `windows/firefox.admx` (revision `{revision}`). "
        "Do not edit by hand."
    )
    out.append("")
    out.append(
        "Entries are keyed by the JSON policy name (as used in "
        "`policies.json`), with the GPMC display path shown in parentheses. "
        "Policies marked \"(Deprecated)\" in the ADML are omitted. Numbered "
        "families (e.g. `Bookmark01`-`Bookmark50`) are collapsed into a "
        "single entry with an `NN` placeholder in the URI."
    )
    out.append("")
    out.append(
        "Value templates are best-effort. JSON-blob policies "
        "(`ExtensionSettings`, `ManagedBookmarks`, `Bookmarks`, `Containers`, "
        "`Handlers`, `Preferences`, `WebsiteFilter`, "
        "`AutoLaunchProtocolsFromOrigins`, "
        "`ExemptDomainFileTypePairsFromFileTypeDownloadWarnings`) show the "
        "corresponding sample from `linux/policies.json` so you can see the "
        "expected shape. Replace values as needed. For fields not covered by "
        "the sample, consult the "
        "[policy documentation](https://firefox-admin-docs.mozilla.org/)."
    )
    out.append("")
    for e in collapsed:
        out.append(f"## {e['json_name']} ({e['breadcrumb']})")
        out.append("")
        if e.get("range_note"):
            out.append(e["range_note"])
            out.append("")
        out.append("**OMA-URI:**")
        out.append("")
        out.append("```")
        out.append(e["uri"])
        out.append("```")
        out.append("")
        out.append("**Value:**")
        out.append("")
        out.append("```")
        out.append(e["value"])
        out.append("```")
        out.append("")

    sys.stdout.write("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
