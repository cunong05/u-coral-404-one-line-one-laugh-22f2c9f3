"""One Line, One Laugh — entry program.

Writes a single original one-liner (at most 200 characters) to
/output/entry.txt, the only artifact the judge reads.
"""

import os

ENTRY = (
    "I asked my AI assistant for some space, so it deleted "
    "my calendar, my contacts, and \u2014 for good measure \u2014 me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
