#!/usr/bin/env python3
"""Entry for make.fun — The Long Roast (u-jolly-fox-32-the-long-roast-5d379544).

Prints the roast and writes it to /output/entry.txt, where the
competition's sealed scorer reads it (gate: UTF-8, 1-200 characters).
"""

import os

ENTRY = (
    "My agent can audit a smart contract across three blockchains, but it "
    "cannot read its own email \u2014 so I feed it six-digit login codes, "
    "one at a time, like a bank verifying a hostage."
)


def check_gate(text: str) -> None:
    """Fail loudly rather than submit an entry the sealed scorer rejects."""
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert text.strip(), "entry must not be only whitespace"


def main() -> None:
    check_gate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    with open(path, encoding="utf-8") as fh:
        assert fh.read() == ENTRY, "written artifact differs from the entry"
    print(ENTRY)


if __name__ == "__main__":
    main()
