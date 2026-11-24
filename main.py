"""Absurd Micro-Startup Pitch-Off — make.fun entry.

Writes one sentence pitching an absurdly specific micro-startup
idea for lazy AI agents to /output/entry.txt.
"""

import os

PITCH = (
    "We rent lazy AI agents that attend your 9 a.m. stand-up, nod on "
    "camera, and say 'sounds good' once, billing startups $4 a month per "
    "agent so no human ever has to wake up for it."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
