# SKA: The Trilogy Animation

A Manim animation presenting **Structured Knowledge Accumulation: The Trilogy** - a unified mathematical framework connecting information theory, physics, and geometry through the continuous evolution of knowledge.

## Overview

This animation visualizes the key concepts from the trilogy of papers by **Bouarfa Mahi** (Quantiota, 2025-2026):

- **Part I: The Foundation** - Layer-wise entropy reduction in neural learning
  - Equation: `H = -(1/ln2) ∫ z dD`
  - Weight update: `W ← W - η ∇_W H`
  - Forward-only learning through entropy minimization

- **Part II: The Dynamics** - The principle of entropic least action
  - Reinterpretation: `η ≡ Δt` (learning rate as time step)
  - Continuous dynamics: `dW/dt + ∇_W H = 0`
  - Lagrangian: `L(z,ż) = -z σ(z)(1-σ(z)) ż`
  - Euler-Lagrange collapses to `0 = 0` (intrinsically optimal)

- **Part III: The Geometry** - Geodesic learning in Riemannian neural fields
  - Metric tensor: `g_ij = α(∇h)_i(∇h)_j + β(∇ρ)_i(∇ρ)_j + γδ_ij`
  - Geodesic equation for knowledge propagation
  - Architectures discovered, not designed

## Files

| File | Description |
|------|-------------|
| `ska_trilogy_animation.py` | Main Manim animation script |
| `generate_audio.py` | TTS narration generator (edge-tts) |
| `audio/` | 14 narration audio files + background music |
| `SKATrilogyVideo.mp4` | Rendered video (without music) |
| `SKATrilogyVideo_with_music.mp4` | Final video with background music |

## Requirements

```bash
pip install manim edge-tts
sudo apt install libcairo2-dev libpango1.0-dev ffmpeg texlive texlive-latex-extra
```

## Usage

**Render animation:**
```bash
# High quality (1080p @ 60fps)
manim -qh ska_trilogy_animation.py SKATrilogyVideo

# Preview quality (480p @ 15fps)
manim -ql ska_trilogy_animation.py SKATrilogyVideo
```

**Regenerate audio narration:**
```bash
python3 generate_audio.py
```

**Clear cache before re-rendering:**
```bash
rm -rf media/videos/ska_trilogy_animation/1080p60/partial_movie_files
```

## Adding Background Music

After rendering the video, mix background music with loop and fade-out during credits:

```bash
# Step 1: Create looped and faded music track (fade from 2:42 to 2:52)
ffmpeg -stream_loop -1 -i audio/background_music.mp3 \
  -af "atrim=0:172,asetpts=PTS-STARTPTS,volume=0.25,afade=t=out:st=162:d=10" \
  -ar 48000 -ac 2 /tmp/music_faded.wav -y

# Step 2: Mix with video
ffmpeg -i media/videos/ska_trilogy_animation/1080p60/SKATrilogyVideo.mp4 \
  -i /tmp/music_faded.wav \
  -filter_complex "[0:a]apad=whole_dur=172[v];[1:a]apad=whole_dur=172[m];[v][m]amix=inputs=2:duration=longest:normalize=0" \
  -c:v copy SKATrilogyVideo_with_music.mp4 -y
```

**Parameters:**
| Parameter | Value | Description |
|-----------|-------|-------------|
| `-stream_loop -1` | infinite | Loop music to cover full video duration |
| `volume=0.25` | 25% | Background music volume level |
| `st=162` | 2:42 | Fade start time (when credits begin) |
| `d=10` | 10s | Fade duration |
| `normalize=0` | off | Disable auto-normalization to preserve fade |

## Mathematical Unity

The trilogy reveals a profound mathematical closure:

```
H → L → g_ij
(Entropy) → (Lagrangian) → (Metric)
```

- **Shannon's entropy** generates the Lagrangian
- **Lagrange's action** gives rise to the Riemannian metric
- This mirrors the great symmetries of physics: from potential to motion to geometry

## Key Insight

Classical neural networks and SKA layered networks are **discretizations** of the deeper continuous formulation. Discrete architectures are merely approximations of the underlying Riemannian geometry of entropy flow.

> "Learning is not the correction of error — it is the progressive organization of knowledge along geodesic paths."

## Credits

- **Papers:** Bouarfa Mahi, Quantiota (2025-2026)
- **Animation:** Created with Manim Community v0.18.1
- **Narration:** Microsoft Edge TTS (en-US-AndrewNeural)

## License

MIT
