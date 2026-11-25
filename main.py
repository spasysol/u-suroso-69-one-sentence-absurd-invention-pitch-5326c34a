"""One-Sentence Absurd Invention Pitch.

Writes a single original sentence pitching a ridiculous invention that
fixes a tiny everyday annoyance, to /output/entry.txt.

Pure standard library only. No network, no randomness: the same line
every run, so the grader's two executions agree byte for byte.
"""

import os

# The pitch: one sentence, at most 220 characters. The everyday
# annoyance is burnt toast; the absurd fix is not a better toaster,
# but legal paperwork for the breakfast.
LINE = (
    "The Apology Toaster apologizes to your bread in advance, burns it "
    "anyway, then prints a tiny insurance claim form so your breakfast "
    "can sue for damages."
)


def main():
    # The gate accepts 1-220 characters; fail loudly instead of
    # submitting an invalid line.
    assert 1 <= len(LINE) <= 220, "pitch must be 1-220 characters"
    assert LINE.count(".") == 1, "pitch must be exactly one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
