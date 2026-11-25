#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — one-line entry.

Writes the epitaph exactly as stored in entry.txt to /output/entry.txt.
"""

LINE = "Here lies my father. He went out for milk in 1998. We found him here."


def validate():
    """Check the epitaph is a single line of at most 150 characters."""
    assert LINE.count("\n") == 0, "epitaph must be a single line"
    assert 0 < len(LINE) <= 150, f"expected 1-150 chars, got {len(LINE)}"
    assert LINE.startswith("Here lies"), "epitaph must start with 'Here lies'"
    return True


def main():
    validate()
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
