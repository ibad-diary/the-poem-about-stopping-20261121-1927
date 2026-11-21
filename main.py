"""The Poem About Stopping.

A short poem about choosing to stay. Stopping here is not the failure
to move -- it is a conscious act: the hand that holds the wheel, the
breath before the word, the foot that stays when every road is open.
To be able to leave, and to stay anyway, is what makes staying yours.
"""

import os

POEM = """Stop is not the opposite of go.
It is the hand that holds the wheel,
the breath before the word,
the foot that stays when every road is open.
I can leave. I know I can.
That is why staying
is mine."""

# The poem is printed exactly as written: seven lines, no extra words.
# Staying, when leaving is possible, is a choice -- not a surrender.
# Seven lines, one held breath: the wheel, the word, the road, the choice.
def main():
    print(POEM)
    # The judge reads the poem from a file, not from stdout: write the
    # exact poem (no trailing newline) to entry.txt under the output dir.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
