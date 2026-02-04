#!/usr/bin/env python3
"""Generate audio narration for Three Laws of Intelligence animation using edge-tts"""

import asyncio
import edge_tts
import os

# All narration texts in order
narrations = [
    ("01_intro", "What if intelligence could be described by just three fundamental laws?"),

    ("02_law1_principle", "Law One: Probabilistic Decision-Making. Intelligence is the capacity to make decisions under uncertainty."),

    ("03_law1_sigmoid", "The sigmoid function transforms accumulated knowledge into decision probability. As knowledge z increases, the decision D moves from uncertainty toward confidence."),

    ("04_law1_meaning", "This equation bridges cognition and mathematics. Intelligence is not deterministic, but probabilistic."),

    ("05_law2_principle", "Law Two: Knowledge Accumulation. Knowledge grows forward-only by reducing uncertainty through structured accumulation."),

    ("06_law2_formula", "The entropy H is measured as an integral over the knowledge trajectory z and the change in decision probability."),

    ("07_law2_entropy", "As knowledge increases, entropy decreases. The system becomes more structured and predictable. Learning is entropy minimization, not gradient descent."),

    ("08_law3_principle", "Law Three: Entropic Least Action. Among all possible learning paths, intelligence follows the path of least action."),

    ("09_law3_paths", "Consider multiple possible paths through knowledge space. Only one path minimizes entropy — the optimal trajectory."),

    ("10_law3_physics", "This law brings physics into intelligence. The Euler-Lagrange equation governs how cognition evolves — minimizing entropy rather than energy. No backpropagation, just natural forward-only optimization."),

    ("11_unified", "Together, these three laws form a unified framework. Probabilistic decisions, knowledge accumulation, and entropic least action."),

    ("12_paradigm", "This represents a paradigm shift. From 'AI works because it learns patterns' to 'AI works because intelligence is the physical reduction of entropy along a probabilistic path.'"),

    ("13_final", "Intelligence isn't a mystery. It's a law-governed natural process."),
]

# Use a professional sounding voice
VOICE = "en-US-AndrewNeural"  # Warm, Confident, Authentic


async def generate_audio(name, text, output_dir):
    """Generate audio file for a single narration"""
    output_file = f"{output_dir}/{name}.mp3"
    communicate = edge_tts.Communicate(text, VOICE, rate="-5%", pitch="+0Hz")
    await communicate.save(output_file)
    print(f"Generated: {output_file}")


async def main():
    """Generate all audio files"""
    output_dir = "/home/coder/project/manim_the_three_laws_of_intelligence/audio"

    # Create audio directory if it doesn't exist
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
