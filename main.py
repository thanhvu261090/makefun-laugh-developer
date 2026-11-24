#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt. Python 3.13, standard library only,
no network access.
"""

from pathlib import Path

ENTRY = (
    "It wasn't a bug, it was a feature flag "
    "\u2014 set by me, in a commit titled 'temporary fix', two years ago."
)

OUTPUT_PATH = Path("/output/entry.txt")


def gate_ok(text: str) -> bool:
    """Gate: 1-200 characters, single line, not only whitespace, UTF-8."""
    if not (1 <= len(text) <= 200):
        return False
    if text.strip() == "":
        return False
    if "\n" in text or "\r" in text:
        return False
    text.encode("utf-8")
    return True


def main() -> None:
    if not gate_ok(ENTRY):
        raise SystemExit("entry failed the gate check")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    # Read back and confirm the file on disk is exactly what we intended.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != ENTRY or not gate_ok(written):
        raise SystemExit("written entry failed the gate check")
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
