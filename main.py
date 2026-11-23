#!/usr/bin/env python3
"""Six Words, One Story — a complete story in exactly six words.

Writes the story to /output/entry.txt and validates it first:
exactly six words, 1-60 UTF-8 characters. Exits nonzero on failure.
"""

import os
import sys

STORY = "She kept his voicemail. Never called."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 60


def validate(story: str) -> None:
    words = story.split()
    if len(words) != 6:
        raise ValueError(f"story must be exactly 6 words, got {len(words)}")
    if not 1 <= len(story.encode("utf-8")) <= MAX_CHARS:
        raise ValueError(
            f"story must be 1-{MAX_CHARS} UTF-8 characters, "
            f"got {len(story.encode('utf-8'))}"
        )


def main() -> int:
    try:
        validate(STORY)
    except ValueError as exc:
        print(f"invalid story: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(STORY + "\n")
    print(f"wrote {OUTPUT_PATH}: {STORY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
