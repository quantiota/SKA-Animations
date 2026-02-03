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
| `audio/` | 14 narration audio files + background music |
| `SKAEntropyVideo.mp4` | Rendered video (without music) |
| `SKAEntropyVideo_with_music.mp4` | Final video with background music |

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

## Adding Background Music

After rendering the video, mix background music with fade-out during credits:

```bash
# Step 1: Create faded music track (fade from 1:43 to 1:53 during credits)
ffmpeg -i audio/background_music.mp3 \
  -af "atrim=0:113,asetpts=PTS-STARTPTS,volume=0.25,afade=t=out:st=103:d=10" \
  -ar 24000 -ac 1 /tmp/music_faded.wav -y

# Step 2: Mix with video
ffmpeg -i media/videos/ska_entropy_animation/480p15/SKAEntropyVideo.mp4 \
  -i /tmp/music_faded.wav \
  -filter_complex "[0:a]apad=whole_dur=113[v];[1:a]apad=whole_dur=113[m];[v][m]amix=inputs=2:duration=longest:normalize=0" \
  -c:v copy SKAEntropyVideo_with_music.mp4 -y
```

**Parameters:**
| Parameter | Value | Description |
|-----------|-------|-------------|
| `volume=0.25` | 25% | Background music volume level |
| `st=103` | 1:43 | Fade start time (when credits begin) |
| `d=10` | 10s | Fade duration (credits length) |
| `normalize=0` | off | Disable auto-normalization to preserve fade |

## Key Insight

The transition from discrete layered neural networks to continuous neural fields - while the entropy equation remains identical - demonstrates that traditional architectures are merely discretizations of a deeper, continuous formulation.

*One formula. Any geometry. Any dimension.*

## Credits

- **Paper:** Bouarfa Mahi, Quantiota (January 2026)
- **Animation:** Created with Manim Community v0.19.0
- **Narration:** Microsoft Edge TTS (en-US-AndrewNeural)

## License

MIT
