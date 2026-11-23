"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original line (<=200 chars) describing a hilariously
useless superpower to /output/entry.txt. Python 3.13 stdlib only.
"""

import os

LINE = "I can stop time for exactly one second. I already used it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
