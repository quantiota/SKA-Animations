# The Fridge Case — SKA Animation

A Manim animation presenting **The Fridge Case: Why Human Intelligence is Probabilistic, Not Deterministic** - a concrete everyday example that makes SKA's probabilistic intelligence framework intuitive.

## Overview

This animation visualizes the key concepts from **Structured Knowledge Accumulation (SKA)** by **Bouarfa Mahi** (Quantiota, 2026):

- **The Undecided State** - Decision probability at the sigmoid midpoint
  - Sigmoid function: `D = σ(z) = 1/(1 + e^{-z})`
  - At z=0, D=0.5 — completely undecided

- **Knowledge Accumulation** - Input features and knowledge tensor
  - Input features X: what you observe in the fridge
  - Knowledge tensor z(r): accumulated assessment
  - Decision probability D(r): mapped via sigmoid

- **Three Principles of Intelligence**
  - Forward-only: knowledge only accumulates — you don't unsee what's in the fridge
  - Probabilistic: every new piece of knowledge shifts the probability of decision-making
  - Entropy reduction: intelligence reduces uncertainty until a choice becomes clear

## Files

| File | Description |
|------|-------------|
| `fridge_animation.py` | Main Manim animation script |
| `generate_audio.py` | TTS narration generator (edge-tts) |
| `audio/` | 14 narration audio files + background music |
| `FridgeCaseVideo.mp4` | Rendered video (without music) |
| `FridgeCaseVideo_with_music.mp4` | Final video with background music |

## Requirements

```bash
pip install manim edge-tts
sudo apt install libcairo2-dev libpango1.0-dev ffmpeg texlive texlive-latex-extra
```

## Usage

**Render animation:**
```bash
# High quality (1080p @ 60fps)
manim -qh fridge_animation.py FridgeCaseVideo

# Preview quality (480p @ 15fps)
manim -ql fridge_animation.py FridgeCaseVideo
```

**Regenerate audio narration:**
```bash
python3 generate_audio.py
```

**Clear cache before re-rendering:**
```bash
rm -rf media/videos/fridge_animation/1080p60/partial_movie_files
```

## Adding Background Music

After rendering the video, mix background music with loop and fade-out during credits:

```bash
# Step 1: Create looped and faded music track (fade from 2:11 to 2:20)
ffmpeg -stream_loop -1 -i audio/background_music.mp3 -af "atrim=0:140,asetpts=PTS-STARTPTS,volume=0.25,afade=t=out:st=131:d=9" -ar 48000 -ac 2 /tmp/music_faded.wav -y

# Step 2: Mix with video
ffmpeg -i media/videos/fridge_animation/1080p60/FridgeCaseVideo.mp4 -i /tmp/music_faded.wav -filter_complex "[0:a]apad=whole_dur=140[v];[1:a]apad=whole_dur=140[m];[v][m]amix=inputs=2:duration=longest:normalize=0" -c:v copy FridgeCaseVideo_with_music.mp4 -y
```

**Parameters:**
| Parameter | Value | Description |
|-----------|-------|-------------|
| `-stream_loop -1` | infinite | Loop music to cover full video duration |
| `volume=0.25` | 25% | Background music volume level |
| `st=131` | 2:11 | Fade start time (when credits begin) |
| `d=9` | 9s | Fade duration |
| `normalize=0` | off | Disable auto-normalization to preserve fade |

## The Fridge Metaphor

The fridge case reveals the structure of probabilistic intelligence:

```
X → z → D = σ(z)
(Observe) → (Accumulate) → (Decide)
```

- **Input features X** are what you see when you open the fridge
- **Knowledge z** is your accumulated assessment of what's needed
- **Decision D** is the sigmoid-mapped probability of going shopping
- New knowledge (friends coming for dinner) shifts z, which shifts D

## Key Insight

Most people explain decisions as binary: "I went because the fridge was empty." But that skips the trajectory — the gradual shift of probability that is the real process of intelligence.

> "Every human decision — from the fridge to life-changing decisions — is probabilistic. SKA doesn't mimic this — it formalizes it."

## Credits

- **Paper:** Bouarfa Mahi, Quantiota (2026)
- **Animation:** Created with Manim Community v0.18.1
- **Narration:** Microsoft Edge TTS (en-US-AndrewNeural)

## License

MIT
