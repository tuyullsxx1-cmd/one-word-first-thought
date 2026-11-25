"""One Word, First Thought — writes the entry word to /output/entry.txt."""

import os
from pathlib import Path

ENTRY = "Defenestration"


def main():
    if len(ENTRY.split()) != 1:
        raise ValueError("entry must be exactly one word")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
