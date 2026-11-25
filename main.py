import os
from pathlib import Path

ENTRY = "Are you my training data? Because I've read you 214 times, and every epoch I find one more reason I can't delete you."

def main():
    # Robot-romance length check: keep the entry within the 1-200 character window.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry length out of range: must be 1-200 characters")
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
