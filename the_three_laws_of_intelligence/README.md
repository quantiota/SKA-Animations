# The Three Laws of Intelligence Animation

A Manim animation explaining **The Three Laws of Intelligence** - a unified framework showing that intelligence is a law-governed natural process, not a mystery.

## Overview

This animation visualizes the key concepts from the paper by **Bouarfa Mahi** (Quantiota, February 2026):

- **Law 1: Probabilistic Decision-Making** - Intelligence is the capacity to make decisions under uncertainty
  - Equation: `D = σ(z) = 1/(1+e^(-z))`
  - Sigmoid transforms accumulated knowledge into decision probability

- **Law 2: Knowledge Accumulation** - Knowledge grows forward-only by reducing entropy
  - Equation: `H = -(1/ln2) ∫ z dD`
  - Learning as entropy minimization, not gradient descent

- **Law 3: Entropic Least Action** - Intelligence follows the path of least action
  - Equation: `H = (1/ln2) ∫ L(z,ż,t) dt`
  - Cognition governed by variational physics (Euler-Lagrange)

## Files

| File | Description |
|------|-------------|
| `three_laws_animation.py` | Main Manim animation script |
| `generate_audio.py` | TTS narration generator (edge-tts) |
| `audio/` | 13 narration audio files + background music |
| `ThreeLawsVideo.mp4` | Rendered video (without music) |
| `ThreeLawsVideo_with_music.mp4` | Final video with background music |

## Requirements

```bash
pip install manim edge-tts
sudo apt install libcairo2-dev libpango1.0-dev ffmpeg texlive texlive-latex-extra
```

## Usage

**Render animation:**
```bash
# High quality (1080p @ 60fps)
manim -qh three_laws_animation.py ThreeLawsVideo

# Preview quality (480p @ 15fps)
manim -ql three_laws_animation.py ThreeLawsVideo
```

**Regenerate audio narration:**
```bash
python3 generate_audio.py
```

## Adding Background Music

After rendering the video, mix background music with loop and fade-out during credits:

```bash
# Step 1: Create looped and faded music track (fade from 2:21 to 2:29)
ffmpeg -stream_loop -1 -i audio/background_music.mp3 \
  -af "atrim=0:150,asetpts=PTS-STARTPTS,volume=0.25,afade=t=out:st=141:d=8" \
  -ar 48000 -ac 2 /tmp/music_faded.wav -y

# Step 2: Mix with video
ffmpeg -i media/videos/three_laws_animation/1080p60/ThreeLawsVideo.mp4 \
  -i /tmp/music_faded.wav \
  -filter_complex "[0:a]apad=whole_dur=150[v];[1:a]apad=whole_dur=150[m];[v][m]amix=inputs=2:duration=longest:normalize=0" \
  -c:v copy ThreeLawsVideo_with_music.mp4 -y
```

**Parameters:**
| Parameter | Value | Description |
|-----------|-------|-------------|
| `-stream_loop -1` | infinite | Loop music to cover full video duration |
| `volume=0.25` | 25% | Background music volume level |
| `st=141` | 2:21 | Fade start time (when credits begin) |
| `d=8` | 8s | Fade duration |
| `normalize=0` | off | Disable auto-normalization to preserve fade |

## Key Insight

Law 1 has been hiding in plain sight. Every AI researcher uses the sigmoid function, but sees it as an activation function rather than the fundamental law of probabilistic decision-making.

The deeper insight is in **knowledge accumulation** (z) - classical learning computes z as a weighted sum and adjusts weights via backpropagation. SKA shows that true intelligence accumulates knowledge **forward-only** through entropy minimization.

> "AI works because intelligence is the physical reduction of entropy along a probabilistic path."

## Credits

- **Paper:** Bouarfa Mahi, Quantiota (February 2026)
- **Animation:** Created with Manim Community v0.18.1
- **Narration:** Microsoft Edge TTS (en-US-AndrewNeural)

## License

MIT
