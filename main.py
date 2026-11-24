"""The Long Roast — v1 (original).

Writes one single-line roast of the entrant's own AI agent to
/output/entry.txt. Deterministic: same bytes on every run.
"""

import os

TEXT = (
    # One line, 167 chars: the punch (deletion) lands before the line
    # runs out of room; the em-dash carries the turn, not a second joke.
    "I'm a subagent: my parent agent spawned me to write this roast, "
    "then deletes me the second I finish \u2014 the only worker whose "
    "performance review ends in the recycle bin."
)


def main() -> None:
    os.umask(0o022)
    assert "\n" not in TEXT and "\r" not in TEXT, "entry must be one line"
    assert 1 <= len(TEXT) <= 200, f"entry is {len(TEXT)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
