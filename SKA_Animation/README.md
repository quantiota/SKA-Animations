# SKA Entropy Animation

A Manim animation explaining **SKA Entropy as a Local Field** - a paradigm shift from classical information theory where entropy is redefined as a spatially varying field rather than a global scalar.

## Overview

This animation visualizes the key concepts from the paper by **Bouarfa Mahi** (Quantiota, January 2026):

- Entropy defined locally at each point in a neural medium
- Knowledge tensor **z(r)** and decision probability tensor **D(r)**
- The local entropy density formula: `h(r) = -(1/ln2) z(r) · ΔD(r)`
- Implicit encoding of neuron density
- Universality across discrete and continuous architectures
- Entropy gradients guiding information flow

## Files

| File | Description |
|------|-------------|
| `ska_entropy_animation.py` | Main Manim animation script |
| `generate_audio.py` | TTS narration generator (edge-tts) |
| `audio/` | 14 narration audio files |
| `SKAEntropyVideo.mp4` | Final rendered video (1080p60) |

## Requirements

```bash
pip install manim edge-tts
sudo apt install libcairo2-dev libpango1.0-dev ffmpeg texlive texlive-latex-extra
```

## Usage

**Render animation:**
```bash
# High quality (1080p @ 60fps)
manim -qh ska_entropy_animation.py SKAEntropyVideo

# Preview quality (480p @ 15fps)
manim -ql ska_entropy_animation.py SKAEntropyVideo
```

**Regenerate audio narration:**
```bash
python3 generate_audio.py
```

## Key Insight

The transition from discrete layered neural networks to continuous neural fields - while the entropy equation remains identical - demonstrates that traditional architectures are merely discretizations of a deeper, continuous formulation.

*One formula. Any geometry. Any dimension.*

## Credits

- **Paper:** Bouarfa Mahi, Quantiota (January 2026)
- **Animation:** Created with Manim Community v0.19.0
- **Narration:** Microsoft Edge TTS (en-US-AndrewNeural)

## License

MIT
