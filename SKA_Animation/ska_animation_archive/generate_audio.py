#!/usr/bin/env python3
"""Generate audio narration for SKA Entropy animation using edge-tts"""

import asyncio
import edge_tts


# All narration texts in order
narrations = [
    ("01_intro_classical", "In classical information theory, entropy measures global uncertainty over an entire distribution."),
    ("02_intro_ska", "SKA takes a different approach: entropy is defined locally, at each point in the neural medium."),
    ("03_volume_element", "Consider a volume element at position r, containing n of r neurons."),
    ("04_tensors", "We define the knowledge tensor z of r, and the decision probability tensor D of r."),
    ("05_learning_step", "During a learning step, decisions shift by delta D."),
    ("06_dot_product", "The local entropy density is their dot product."),
    ("07_density_intro", "Neuron density needs no explicit variable."),
    ("08_density_sum", "The dot product sums over n of r terms automatically."),
    ("09_density_implicit", "Denser regions produce proportionally smaller entropy. Density is implicit in the structure itself."),
    ("10_universality", "The identical equation, in any spatial dimension. One formula. Any geometry."),
    ("11_hubs", "High-density regions have greater capacity to reduce entropy, becoming natural hubs for knowledge accumulation."),
    ("12_gradient", "The gradient of h guides information flow."),
    ("13_self_regulates", "The system self-regulates, by local capacity."),
    ("14_finale", "Entropy, reimagined. Not as a global summary, but as a living, breathing field."),
]

# Use a professional sounding voice
VOICE = "en-US-AndrewNeural"  # Warm, Confident, Authentic

async def generate_audio(name, text, output_dir="/home/coder/manim/audio"):
    """Generate audio file for a single narration"""
    output_file = f"{output_dir}/{name}.mp3"
    communicate = edge_tts.Communicate(text, VOICE, rate="-5%", pitch="+0Hz")
    await communicate.save(output_file)
    print(f"Generated: {output_file}")

async def main():
    """Generate all audio files"""
    print(f"Generating {len(narrations)} audio files...")
    print(f"Using voice: {VOICE}")
    print()

    for name, text in narrations:
        await generate_audio(name, text)

    print()
    print("All audio files generated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
