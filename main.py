"""The Moon Finally Answers Back.

Chosen line (118 characters):

    Four billion years of wishes and not one of you ever wished me a
    happy birthday. Anyway: no, he doesn't like you back.

Why this line wins, against the five judging criteria (in order):
1. Moon answering (5/5): it answers the wishes directly -- four billion
   years of them -- and then answers one specific wish with a blunt "no".
   The Moon is not describing itself; it is replying.
2. Funny on one read (5/5): the birthday complaint is instantly funny
   (everyone wishes ON the Moon, nobody wishes the Moon well), and the
   second sentence lands the real laugh: the Moon knows about your crush.
3. Moon's own voice (5/5): wry, old and tired of being wished upon --
   "four billion years" is the Moon's age talking, not a human's.
4. Comeback in one read (5/5): the turn arrives in the second sentence,
   "Anyway: no, he doesn't like you back" -- a sharp pivot from the
   cosmic complaint to one very personal rejection, before the line ends.
5. Length economy (4/5): 118 of 240 characters, nothing wasted; one
   character shorter would cost the joke, one longer would dilute it.

Score table (1-5 per criterion: Moon answering / funny / Moon's voice /
comeback turn / length economy; total out of 25). 10 candidates.

| #  | Moon | funny | voice | turn | econ | total |
|----|------|-------|-------|------|------|-------|
|  3 |    5 |     5 |     5 |    5 |    4 |    24 |
|  2 |    4 |     5 |     4 |    4 |    4 |    21 |
|  4 |    5 |     4 |     4 |    4 |    4 |    21 |
|  5 |    4 |     4 |     5 |    3 |    4 |    20 |
|  7 |    4 |     4 |     4 |    4 |    4 |    20 |
|  1 |    4 |     4 |     3 |    4 |    4 |    19 |
|  9 |    5 |     4 |     3 |    4 |    3 |    19 |
| 10 |    3 |     4 |     3 |    4 |    4 |    18 |
|  6 |    3 |     4 |     4 |    3 |    3 |    17 |
|  8 |    4 |     3 |     4 |    3 |    3 |    17 |

Candidate lines (for the record):
 1. "I heard every wish, every howl, every 2 a.m. promise. The answer
    is no -- and the one about the lottery ticket was embarrassing for
    us both." (139 chars) -- funny, but "the answer is no" is the
    generic Moon reply half the field will send; the lottery twist is
    second-hand embarrassment, not a comeback.
 2. "You keep howling at me like I run customer service. I am a rock.
    I don't grant wishes, I just reflect sunlight and your poor
    decisions." (135 chars) -- strong voice and a good closing sting,
    but it complains more than it answers a wish.
 3. WINNER (see above).
 4. "Yes, I heard the wish. No, I can't make him text you. I'm a moon,
    not a miracle -- I just glow and watch you make the same mistake
    twice." (136 chars) -- direct answer and good voice, but "not a
    miracle" explains its own joke a little, and the turn is softer
    than #3's.
 5. "Every night you stare up and promise to change. I have watched
    you break that promise 14,605 times. I'm not mad. I'm just very,
    very tired." (139 chars) -- beautifully tired voice, but no sharp
    comeback turn: it ends on a sigh, not a punch.
 6. "You howl, you wish, you promise -- and then you blame me for the
    tides. I've been here four billion years and this is still the
    weirdest job in the solar system." (160 chars) -- a complaint about
    the job, not an answer to anyone's wish; the turn never arrives.
 7. "Okay, fine. Yes, I heard you. The answer is still no, and yes, I
    saw what you did last Tuesday. I see everything. I am the moon. I
    never blink." (143 chars) -- menacing and funny, but "I never
    blink" is a second punch that spends characters after the turn.
 8. "I grant no wishes, I answer no howls, I keep no promises -- I just
    hang here, glowing, while you lot point at me and make the same wish
    every single night." (154 chars) -- a list, not a comeback; the
    joke is the refusal itself, and it never twists.
 9. "You wished on me 4,000 years ago and you're still wishing. I have
    one answer for all of it: stop howling, start sleeping, and no, the
    ex isn't coming back." (155 chars) -- the ending is the joke, but
    the first half is throat-clearing and the voice is a scold, not the
    Moon.
10. "I'm not ignoring you. I heard every single wish. I just have no
    hands, no magic, and no interest -- but nice howl, Dave, very on
    pitch." (134 chars) -- the "Dave" gag is the funniest single beat
    here, but it answers nobody's wish and only lands if the judge
    likes the name joke.

Notes on the scoring:
- The winning line is the only candidate that scores 5 on the first
  four criteria at once: it answers, it is funny, it sounds old and
  tired, and it turns. The birthday grievance is one specific, strong
  image (not a generic "I am the Moon" line), and the crush rejection
  makes the comeback personal in a single read.
- Cliches avoided: "I am just a rock", "I don't grant wishes" and
  "the answer is no" on their own are the obvious Moon replies; #3
  earns its "no" by making it about one named wish instead.
- Short lines win ties: at 118 characters the winner is also the
  shortest candidate, so it wins any byte-count tie-break as well.
"""

import os
import sys

LINE = (
    "Four billion years of wishes and not one of you ever wished me a "
    "happy birthday. Anyway: no, he doesn't like you back."
)


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: LINE is empty", file=sys.stderr)
        return 1
    if len(line) > 240:
        print("error: LINE exceeds 240 characters", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: LINE must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read back and confirm the file holds exactly the chosen line:
    # a gate failure (wrong bytes on disk) must never pass silently.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        print("error: entry.txt does not match the chosen line", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
