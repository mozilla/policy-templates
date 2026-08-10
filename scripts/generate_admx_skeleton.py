#!/usr/bin/env python3
"""Generate ADMX/ADML skeleton entries for a policy from the schema.

Reads `.schema-watch/policies-schema.json`, inspects the named policy's
JSON-schema shape, and emits scaffolding to:

  * windows/firefox.admx          - the <policy> element
  * windows/en-US/firefox.adml    - display name + explain text (schema
                                    description used as a seed)
  * windows/{de-DE,fr-FR,ru-RU}/firefox.adml  - placeholder strings
  * linux/policies.json           - sample entry
  * mac/org.mozilla.firefox.plist - sample entry

The generator handles the common cases mechanically. Nested-object
policies (e.g. LocalNetworkAccess-style with sub-keys) still need
category treatment by hand -- the script emits a JSON-blob skeleton
plus a TODO comment so a maintainer can promote it to a category
later if desired.

Every human-facing string is prefixed with `TODO:` so it's obvious
what still needs review before merging.

Usage:
    python scripts/generate_admx_skeleton.py <PolicyName> [--dry-run]

Run without --dry-run to write the changes; the git working tree is
your undo.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SCHEMA_PATH = Path(".schema-watch/policies-schema.json")
ADMX_PATH = Path("windows/firefox.admx")
LOCALES = ["en-US", "de-DE", "fr-FR", "ru-RU"]
ADML_PATHS = {loc: Path(f"windows/{loc}/firefox.adml") for loc in LOCALES}
LINUX_PATH = Path("linux/policies.json")
MAC_PATH = Path("mac/org.mozilla.firefox.plist")
REGISTRY_PREFIX = r"Software\Policies\Mozilla\Firefox"


# ---------------------------------------------------------------------------
# Schema inspection
# ---------------------------------------------------------------------------


def load_schema() -> dict:
    if not SCHEMA_PATH.exists():
        sys.exit(f"error: {SCHEMA_PATH} not found (run the schema-sync workflow first)")
    with SCHEMA_PATH.open() as f:
        return json.load(f)


def classify(policy_schema: dict) -> str:
    """Return one of: 'boolean', 'string', 'enum-string', 'integer',
    'enum-integer', 'list-string', 'json-blob'."""
    t = policy_schema.get("type")
    enum = policy_schema.get("enum")
    if t == "boolean":
        return "boolean"
    if t == "string":
        return "enum-string" if enum else "string"
    if t in ("integer", "number"):
        return "enum-integer" if enum else "integer"
    if t == "array":
        item_type = (policy_schema.get("items") or {}).get("type")
        if item_type == "string":
            return "list-string"
        return "json-blob"
    if t == "object":
        # If every direct sub-property is a simple primitive with no nesting,
        # this is a category candidate. We still emit a JSON blob and note it,
        # since translating a category is a bigger decision.
        return "json-blob"
    return "json-blob"  # default: safest


def supported_ref(policy_schema: dict, admx_root: ET.Element) -> tuple[str, str | None]:
    """Return (ref_name, warning_or_None).

    Chooses SUPPORTED_FF<N> when the schema declares an ESR backport,
    otherwise SUPPORTED_FF<N>_ONLY. Warns if the chosen ref isn't
    defined in the ADMX yet (the maintainer will need to add it in a
    supported-versions branch first).
    """
    compat = policy_schema.get("x-compatibility") or {}
    fx = (compat.get("firefox") or {}).get("version_added")
    esr = (compat.get("firefox_esr") or {}).get("version_added")

    if not fx or fx is False:
        return ("SUPPORTED_FF_UNKNOWN", "no x-compatibility.firefox.version_added in schema")

    if esr and esr is not False:
        ref = f"SUPPORTED_FF{fx}"
    else:
        ref = f"SUPPORTED_FF{fx}_ONLY"

    ns = "{" + admx_root.tag.split("}")[0][1:] + "}" if "}" in admx_root.tag else ""
    defined = {d.get("name") for d in admx_root.findall(f".//{ns}supportedOn/{ns}definitions/{ns}definition")}
    if ref not in defined:
        return (ref, f"{ref} is not defined in firefox.admx yet - add it in a supported-versions branch first")

    return (ref, None)


# ---------------------------------------------------------------------------
# ADMX policy body generator
# ---------------------------------------------------------------------------


def admx_policy_body(name: str, schema: dict, supported: str) -> str:
    kind = classify(schema)

    if kind == "boolean":
        return dedent(f"""\
            <policy name="{name}" class="Both" displayName="$(string.{name})" explainText="$(string.{name}_Explain)" key="{REGISTRY_PREFIX}" valueName="{name}">
              <parentCategory ref="firefox"/>
              <supportedOn ref="{supported}"/>
              <enabledValue>
                <decimal value="1"/>
              </enabledValue>
              <disabledValue>
                <decimal value="0"/>
              </disabledValue>
            </policy>""")

    if kind == "string":
        return dedent(f"""\
            <policy name="{name}" class="Both" displayName="$(string.{name})" explainText="$(string.{name}_Explain)" key="{REGISTRY_PREFIX}" presentation="$(presentation.Preferences_String)">
              <parentCategory ref="firefox"/>
              <supportedOn ref="{supported}"/>
              <elements>
                <text id="Preferences_String" valueName="{name}"/>
              </elements>
            </policy>""")

    if kind == "integer":
        return dedent(f"""\
            <policy name="{name}" class="Both" displayName="$(string.{name})" explainText="$(string.{name}_Explain)" key="{REGISTRY_PREFIX}" presentation="$(presentation.{name})">
              <parentCategory ref="firefox"/>
              <supportedOn ref="{supported}"/>
              <elements>
                <decimal id="{name}" valueName="{name}"/>
              </elements>
            </policy>""")

    if kind in ("enum-string", "enum-integer"):
        items_xml = []
        for v in schema.get("enum", []):
            label_key = f"{name}_{re.sub(r'[^A-Za-z0-9]+', '', str(v))}"
            if kind == "enum-integer":
                value_xml = f'<decimal value="{v}"/>'
            else:
                value_xml = f'<string>{v}</string>'
            items_xml.append(
                f'          <item displayName="$(string.{label_key})">\n'
                f'            <value>\n'
                f'              {value_xml}\n'
                f'            </value>\n'
                f'          </item>'
            )
        return dedent(f"""\
            <policy name="{name}" class="Both" displayName="$(string.{name})" explainText="$(string.{name}_Explain)" key="{REGISTRY_PREFIX}" presentation="$(presentation.{name})">
              <parentCategory ref="firefox"/>
              <supportedOn ref="{supported}"/>
              <elements>
                <enum id="{name}" valueName="{name}">
{chr(10).join(items_xml)}
                </enum>
              </elements>
            </policy>""")

    if kind == "list-string":
        return dedent(f"""\
            <policy name="{name}" class="Both" displayName="$(string.{name})" explainText="$(string.{name}_Explain)" key="{REGISTRY_PREFIX}" presentation="$(presentation.Permissions)">
              <parentCategory ref="firefox"/>
              <supportedOn ref="{supported}"/>
              <elements>
                <list id="Permissions" key="{REGISTRY_PREFIX}\\{name}" valuePrefix=""/>
              </elements>
            </policy>""")

    # json-blob: multiText + OneLine variant
    body = dedent(f"""\
        <policy name="{name}" class="Both" displayName="$(string.{name})" explainText="$(string.{name}_Explain)" key="{REGISTRY_PREFIX}" presentation="$(presentation.JSON)">
          <parentCategory ref="firefox"/>
          <supportedOn ref="{supported}"/>
          <elements>
            <multiText id="JSON" valueName="{name}" maxLength="16384"/>
          </elements>
        </policy>
        <policy name="{name}OneLine" class="Both" displayName="$(string.{name}OneLine)" explainText="$(string.{name}_Explain)" key="{REGISTRY_PREFIX}" presentation="$(presentation.JSONOneLine)">
          <parentCategory ref="firefox"/>
          <supportedOn ref="{supported}"/>
          <elements>
            <text id="JSONOneLine" valueName="{name}" maxLength="16384"/>
          </elements>
        </policy>""")
    if _is_object_with_primitive_children(schema):
        hint = (
            "<!-- TODO: this schema shape (object with simple sub-keys) may be a\n"
            "     better fit for a category with individual sub-policies. See\n"
            "     LocalNetworkAccess / FirefoxHome for examples. -->\n"
        )
        return hint + body
    return body


def _is_object_with_primitive_children(schema: dict) -> bool:
    if schema.get("type") != "object":
        return False
    props = schema.get("properties") or {}
    if not props:
        return False
    for sub in props.values():
        st = sub.get("type")
        if st not in ("boolean", "string", "integer", "number"):
            if st == "array" and (sub.get("items") or {}).get("type") == "string":
                continue
            return False
    return True


def dedent(text: str) -> str:
    # Trim leading spaces from each line based on the first non-empty line's
    # indent. Keeps our f-strings readable in source.
    lines = text.split("\n")
    stripped = [ln for ln in lines if ln.strip()]
    if not stripped:
        return text
    indent = len(stripped[0]) - len(stripped[0].lstrip(" "))
    return "\n".join(ln[indent:] if len(ln) >= indent else ln for ln in lines)


# ---------------------------------------------------------------------------
# ADML string generators
# ---------------------------------------------------------------------------


def adml_strings(name: str, schema: dict, locale: str) -> list[str]:
    kind = classify(schema)
    description = (schema.get("description") or "").strip()

    if locale == "en-US":
        display = f"TODO: display name for {name}"
        explain = (
            f"TODO: explain text for {name}.\n\n"
            f"Schema description: {description}"
        ) if description else f"TODO: explain text for {name}."
    else:
        display = f"TODO ({locale}): display name for {name}"
        explain = f"TODO ({locale}): explain text for {name}"

    entries = [
        f'      <string id="{name}">{_xml_escape(display)}</string>',
        f'      <string id="{name}_Explain">{_xml_escape(explain)}</string>',
    ]

    if kind in ("enum-string", "enum-integer"):
        for v in schema.get("enum", []):
            label_key = f"{name}_{re.sub(r'[^A-Za-z0-9]+', '', str(v))}"
            label = f"TODO: label for value {v!r}" if locale == "en-US" else f"TODO ({locale}): label for {v!r}"
            entries.append(f'      <string id="{label_key}">{_xml_escape(label)}</string>')

    if kind == "json-blob":
        # OneLine variant needs its own display name.
        display_ol = display + " (JSON on one line)"
        entries.insert(
            1,
            f'      <string id="{name}OneLine">{_xml_escape(display_ol)}</string>',
        )

    return entries


def _xml_escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


# ---------------------------------------------------------------------------
# Presentation entry (for element-based policies)
# ---------------------------------------------------------------------------


def presentation_entry(name: str, schema: dict) -> str | None:
    kind = classify(schema)
    if kind == "integer":
        return f'      <presentation id="{name}">\n        <decimalTextBox refId="{name}"/>\n      </presentation>'
    if kind in ("enum-string", "enum-integer"):
        return f'      <presentation id="{name}">\n        <dropdownList refId="{name}"/>\n      </presentation>'
    return None  # boolean, string, list-string, json-blob reuse shared presentations


# ---------------------------------------------------------------------------
# Sample generators (linux + mac)
# ---------------------------------------------------------------------------


def linux_sample(name: str, schema: dict) -> str:
    """Return the sample line without a trailing comma or indent.

    The caller handles insertion (including fixing the previous last
    entry's trailing comma).
    """
    kind = classify(schema)
    examples = schema.get("examples") or []
    if kind == "boolean":
        return f'"{name}": true | false'
    if kind == "string" and not schema.get("enum"):
        return f'"{name}": "STRING_VALUE"'
    if kind == "integer" and not schema.get("enum"):
        return f'"{name}": 0'
    if kind == "enum-string":
        opts = " | ".join(f'"{v}"' for v in schema.get("enum", []))
        return f'"{name}": {opts}'
    if kind == "enum-integer":
        opts = " | ".join(str(v) for v in schema.get("enum", []))
        return f'"{name}": {opts}'
    if kind == "list-string":
        return f'"{name}": ["EXAMPLE"]'
    if examples:
        formatted = json.dumps(examples[0], indent=2).replace("\n", "\n    ")
        return f'"{name}": {formatted}'
    return f'"{name}": {{}}'


def insert_into_linux_json(text: str, sample_line: str) -> str:
    """Insert a new policy line just before the closing braces.

    Ensures the previous last entry gets its trailing comma and the
    new line lands at the right 4-space indent inside the "policies"
    object.
    """
    closer = "\n  }\n}"
    idx = text.rfind(closer)
    if idx == -1:
        raise ValueError("linux/policies.json closing braces not found")
    prefix, suffix = text[:idx], text[idx:]
    # Append a comma to whatever the current last entry line ended with
    # (unless it already has one).
    if not prefix.rstrip().endswith(","):
        prefix = prefix.rstrip() + ","
    return prefix + "\n    " + sample_line + suffix


def mac_sample(name: str, schema: dict) -> str:
    """Return an XML plist snippet for the policy."""
    kind = classify(schema)
    if kind == "boolean":
        return f"\t<key>{name}</key>\n\t<true/>"
    if kind == "string" and not schema.get("enum"):
        return f"\t<key>{name}</key>\n\t<string>STRING_VALUE</string>"
    if kind == "integer" and not schema.get("enum"):
        return f"\t<key>{name}</key>\n\t<integer>0</integer>"
    if kind == "enum-string":
        first = schema.get("enum", ["VALUE"])[0]
        return f"\t<key>{name}</key>\n\t<string>{first}</string>"
    if kind == "enum-integer":
        first = schema.get("enum", [0])[0]
        return f"\t<key>{name}</key>\n\t<integer>{first}</integer>"
    if kind == "list-string":
        return f"\t<key>{name}</key>\n\t<array>\n\t\t<string>EXAMPLE</string>\n\t</array>"
    # json-blob
    return f"\t<key>{name}</key>\n\t<!-- TODO: plist form of the JSON blob for {name} -->"


# ---------------------------------------------------------------------------
# File mutators
# ---------------------------------------------------------------------------


def insert_before(text: str, marker: str, insertion: str) -> str:
    idx = text.rfind(marker)
    if idx == -1:
        raise ValueError(f"marker {marker!r} not found")
    return text[:idx] + insertion + text[idx:]


def write(path: Path, content: str) -> None:
    path.write_bytes(content.encode("utf-8"))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("policy", help="Top-level policy name from the schema")
    ap.add_argument("--dry-run", action="store_true", help="Print what would change, don't write")
    args = ap.parse_args()
    name = args.policy

    schema = load_schema()
    policy_schema = schema.get("properties", {}).get(name)
    if policy_schema is None:
        sys.exit(f"error: {name!r} is not a top-level property in the schema")

    admx_text = ADMX_PATH.read_text(encoding="utf-8")
    admx_root = ET.fromstring(admx_text)

    # Already there?
    if re.search(rf'<policy name="{re.escape(name)}"', admx_text):
        sys.exit(f"error: {name!r} already exists in {ADMX_PATH}")

    supported, warning = supported_ref(policy_schema, admx_root)
    kind = classify(policy_schema)

    print(f"# Skeleton for {name}", file=sys.stderr)
    print(f"# kind = {kind}", file=sys.stderr)
    print(f"# supportedOn = {supported}", file=sys.stderr)
    if warning:
        print(f"# WARNING: {warning}", file=sys.stderr)
    print(file=sys.stderr)

    # Assemble additions.
    admx_policy = "    " + admx_policy_body(name, policy_schema, supported).replace("\n", "\n    ") + "\n"
    presentation = presentation_entry(name, policy_schema)
    linux_line = linux_sample(name, policy_schema)
    mac_lines = mac_sample(name, policy_schema)

    if args.dry_run:
        print("=== windows/firefox.admx (before </policies>) ===")
        print(admx_policy.rstrip())
        for locale in LOCALES:
            print(f"\n=== windows/{locale}/firefox.adml (before </stringTable>) ===")
            for line in adml_strings(name, policy_schema, locale):
                print(line)
        if presentation:
            print(f"\n=== windows/en-US/firefox.adml (before </presentationTable>) ===")
            print(presentation)
        print(f"\n=== {LINUX_PATH} (append inside 'policies') ===")
        print(linux_line)
        print(f"\n=== {MAC_PATH} (append inside outer dict) ===")
        print(mac_lines)
        return 0

    # Apply.
    admx_text = insert_before(admx_text, "  </policies>", admx_policy)
    write(ADMX_PATH, admx_text)

    for locale in LOCALES:
        path = ADML_PATHS[locale]
        text = path.read_text(encoding="utf-8")
        insertion = "\n".join(adml_strings(name, policy_schema, locale)) + "\n"
        text = insert_before(text, "    </stringTable>", insertion)
        if locale == "en-US" and presentation:
            text = insert_before(text, "    </presentationTable>", presentation + "\n")
        write(path, text)

    linux_text = LINUX_PATH.read_text(encoding="utf-8")
    linux_text = insert_into_linux_json(linux_text, linux_line)
    write(LINUX_PATH, linux_text)

    mac_text = MAC_PATH.read_text(encoding="utf-8")
    mac_text = insert_before(mac_text, "</dict>\n</plist>", mac_lines + "\n")
    write(MAC_PATH, mac_text)

    print(f"Wrote skeleton for {name}. Review the diff and fill in TODO placeholders.", file=sys.stderr)
    if warning:
        print(f"REMINDER: {warning}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
