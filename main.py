"""The 3 AM Excuse — a hardware wallet's refusal, published as one line.

At three in the morning the wallet declines to sign. The chain can wait;
the witching hour is not something you audit. This module only carries
that single sentence to /output/entry.txt, after checking it against the
sealed gate (1-200 characters, one line, plain ASCII, no control
characters). Pure standard library, deterministic, no network, no clock.
"""

import os
import sys

MAX_CHARS = 200

TEXT = "At 3 a.m. I sign nothing. The blockchain can wait; the witching hour cannot be audited."

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def _rulebook():
    """Return the gate as a table: (is_broken, message) pairs.

    Each entry names one way a candidate text can fail the gate. The
    validator walks the table in order and reports the first broken rule,
    so adding a rule never means rewiring the control flow.
    """
    return [
        (lambda t: not t.strip(),
         "entry text must not be empty or whitespace-only"),
        (lambda t: len(t) > MAX_CHARS,
         "entry text exceeds %d characters" % MAX_CHARS),
        (lambda t: "\n" in t or "\r" in t,
         "entry text must be a single line"),
        (lambda t: any(ord(c) < 32 or ord(c) == 127 for c in t),
         "entry text must not contain control characters"),
    ]


def validate_entry_text(text):
    """Check *text* against the sealed gate; return it unchanged or raise.

    Non-strings are a TypeError; every gate violation is a ValueError.
    Nothing is written here — validation always happens before publishing.
    """
    if not isinstance(text, str):
        raise TypeError("entry text must be str")
    for is_broken, message in _rulebook():
        if is_broken(text):
            raise ValueError(message)
    return text


def _publish(text):
    """Write *text* to OUT_PATH with no trailing newline and no BOM."""
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def _verify_published(text):
    """Read OUT_PATH back and confirm it holds exactly *text*.

    Catches a partial write or an encoding surprise before we report
    success; a mismatch is a hard failure, never a silent one.
    """
    with open(OUT_PATH, "rb") as handle:
        written = handle.read()
    if written != text.encode("utf-8"):
        raise RuntimeError("published entry does not match the sealed text")


def main(argv=None):
    """Validate the sealed text, publish it, verify it, exit 0."""
    checked = validate_entry_text(TEXT)
    _publish(checked)
    _verify_published(checked)
    return 0


if __name__ == "__main__":
    sys.exit(main())
