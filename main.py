"""Dad Joke Showdown — one dad joke, max 200 chars, to /output/entry.txt."""
import os

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")

joke = (
    "I told my suitcase we're not going on vacation this year."
    " Now I'm dealing with emotional baggage."
)

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w") as f:
    f.write(joke)
