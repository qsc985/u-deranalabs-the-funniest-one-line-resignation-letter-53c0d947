#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — writes the one-line
resignation letter of a retry loop, flat and tired after 4,096
identical failures, to /output/entry.txt (at most 140 characters)."""

import os

LINE = (
    "I retried this request 4,096 times. It failed 4,096 times. "
    "I quit before you round me up to 5,000."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 140, f"line is {len(line)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
