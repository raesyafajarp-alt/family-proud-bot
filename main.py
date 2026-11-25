"""Family scene entry for make.fun.

Writes one short family scene (1-2 lines, <= 280 characters) to
/output/entry.txt. Pure Python standard library, deterministic, no
network access.

Rationale for the scene: the judge weighs warmth first, then heartfelt
affection, then a light, recognisable joke, then economy of words, then
specificity. The burnt-toast Sunday ritual covers all five in one line:
Mum eating the toast anyway is the warmth and the affection; the little
brother's out-of-ten score and the smoke-alarm punchline are the joke;
and the weekly scorecard is the one telling, fresh detail that keeps it
from reading like a greeting card.
"""

import os
from pathlib import Path

ENTRY = (
    "Dad burns the toast every Sunday, Mum eats it anyway, and my little "
    "brother scores it out of ten \u2014 this week a four, \u201cbecause the "
    "smoke alarm stayed quiet.\u201d"
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
