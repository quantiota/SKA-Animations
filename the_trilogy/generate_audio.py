#!/usr/bin/env python3
"""Generate audio narration for SKA Trilogy animation using edge-tts"""

import asyncio
import edge_tts
import os

# All narration texts in order
narrations = [
    ("01_intro", "The Structured Knowledge Accumulation framework introduces a unifying mathematical principle that connects information theory, physics, and geometry through the continuous evolution of knowledge."),

    ("02_part1_title", "Part One: The Foundation."),

    ("03_part1_content", "The first paper begins with the discovery that learning can be expressed as a law of entropy reduction. Each neural layer evolves autonomously, aligning its knowledge with decision probability through forward-only dynamics."),

    ("04_part1_equation", "This formulation establishes entropy as the central invariant of learning. Neural systems no longer require backpropagation; they self-organize by reducing uncertainty step by step."),

    ("05_part2_title", "Part Two: The Dynamics."),

    ("06_part2_content", "The second paper elevates SKA to the level of physical law. By interpreting the learning rate as a temporal differential, SKA reveals that the evolution of knowledge follows the principle of entropic least action."),

    ("07_part2_euler", "The Euler-Lagrange equation collapses to an identity zero equals zero, showing that the system's trajectory is intrinsically optimal. Learning is a natural law of motion in information space — not an optimization problem, but an entropic flow."),

    ("08_part3_title", "Part Three: The Geometry."),

    ("09_part3_content", "The third work extends SKA to continuous neural fields. By introducing neuron density and local entropy, the neural medium becomes a Riemannian information manifold."),

    ("10_part3_geodesic", "Knowledge propagates along geodesic trajectories that minimize information distance, revealing architectures that are not designed but discovered — the natural geometry of knowledge propagation."),

    ("11_insight", "Classical neural networks and SKA layered networks are approximations of this continuous formulation. Discrete architectures are merely discretizations of the deeper Riemannian geometry."),

    ("12_unified", "From entropy to dynamics to geometry, the SKA trilogy traces the full trajectory of intelligence. Learning is not the correction of error — it is the progressive organization of knowledge along geodesic paths."),

    ("13_unity", "The mathematical unity is complete. Entropy generates the Lagrangian, and the Lagrangian gives rise to the Riemannian metric. This closure mirrors the great symmetries of physics — from potential to motion to geometry."),

    ("14_final", "SKA unites Entropy, Lagrange's action, and Riemann's geometry into a single law of knowledge accumulation."),
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
    output_dir = "/home/coder/project/manim_the_trilogy/audio"

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
