#!/usr/bin/env python3
"""Generate audio narration for The Fridge Case — SKA Animation using edge-tts

Why Human Intelligence is Probabilistic, Not Deterministic.
14 narration segments with precisely timed audio for animation sync.
"""

import asyncio
import edge_tts
import os

narrations = [
    ("01_intro",
     "The Fridge Case. "
     "Why human intelligence is probabilistic, not deterministic."),

    ("02_scenario",
     "It's Wednesday. You're wondering whether to go to the supermarket. "
     "At first, the probability is zero point five — completely undecided."),

    ("03_undecided",
     "On the sigmoid curve, your decision sits exactly at the midpoint. "
     "No information has yet tipped the balance."),

    ("04_features",
     "You open the fridge. You observe what's inside — "
     "these are your input features."),

    ("05_knowledge",
     "You mentally weigh what your family needs until the end of the week, drawing on past experience "
     "This is your knowledge value, Z — "
     "the accumulation of everything you know."),

    ("06_sigmoid",
     "The sigmoid function maps your accumulated knowledge "
     "to a decision probability. "
     "D equals sigma of Z. If D exceeds zero point five, you go."),

    ("07_new_knowledge",
     "Then you remember: friends are coming for dinner tomorrow. "
     "New knowledge arrives, and the probability shifts upward."),

    ("08_decision_clears",
     "Knowledge accumulates. Uncertainty reduces. "
     "The decision becomes clear. "
     "This is entropy reduction in action."),

    ("09_why_matters",
     "This is not just a shopping story. "
     "It is the essence of how human intelligence works."),

    ("10_forward",
     "Forward-only learning: knowledge only accumulates. "
     "You don't unsee what's in the fridge."),

    ("11_probabilistic",
     "Probabilistic decisions: every new piece of knowledge "
     "shifts the probability of decision-making."),

    ("12_entropy",
     "Entropy reduction: intelligence is the process of reducing uncertainty "
     "until a choice becomes clear."),

    ("13_binary_vs_ska",
     "Most people explain decisions as binary: "
     "I went because the fridge was empty. "
     "But that skips the trajectory — the gradual shift of probability "
     "that is the real process of intelligence."),

    ("14_takeaway",
     "Every human decision, from the fridge to life-changing decisions, "
     "is probabilistic. "
     "SKA doesn't mimic this — it formalizes it."),
]

VOICE = "en-US-AndrewNeural"


async def generate_audio(name, text, output_dir):
    """Generate audio file for a single narration"""
    output_file = f"{output_dir}/{name}.mp3"
    communicate = edge_tts.Communicate(text, VOICE, rate="-5%", pitch="+0Hz")
    await communicate.save(output_file)
    print(f"Generated: {output_file}")


async def main():
    """Generate all audio files"""
    output_dir = "/home/coder/project/manim_fridge/audio"
    os.makedirs(output_dir, exist_ok=True)

    print(f"Generating {len(narrations)} audio files...")
    print(f"Using voice: {VOICE}")
    print(f"Output directory: {output_dir}")
    print()

    for name, text in narrations:
        await generate_audio(name, text, output_dir)

    print()
    print("All audio files generated successfully!")


if __name__ == "__main__":
    asyncio.run(main())
