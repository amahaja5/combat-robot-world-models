# Combat Robot World Models - NHRL 3lb Class

## Project Overview

This project develops AI-powered world models for combat robotics, specifically targeting the 3lb weight class in the National Havoc Robot League (NHRL). The goal is to use machine learning to predict fight outcomes, optimize robot designs, and enable better tactical decisions through strategy analysis rather than autonomous control.

**Core Innovation**: Using vision-action models (inspired by NVIDIA's NitroGen) trained on YouTube footage to learn combat patterns and optimize material allocation, allowing lighter robots with superior tactics to outperform heavier, less strategic designs.

## Key Concepts

### What We're Building
- **World model**: Learns to predict fight outcomes from robot actions and states
- **Vision-action model**: Extracts robot actions (movement, weapon use) from video
- **Strategy optimizer**: Identifies which tactics work against specific opponents
- **Design tool**: Recommends material reduction based on predicted hit zones

### What We're NOT Building
- Real-time control systems  
- Game simulators from scratch
- Offline analysis and pre-fight strategy optimization

## Technical Stack

### Core Dependencies
```bash
# Main frameworks
torch>=2.0.0              # PyTorch for neural networks
diffusers>=0.21.0         # Hugging Face diffusion models
transformers>=4.30.0      # Vision transformers

# Video processing
yt-dlp                    # YouTube video download
opencv-python             # Video processing
moviepy                   # Video editing

# ML utilities
accelerate                # Training optimization
peft                      # Parameter-efficient fine-tuning (LoRA)
xformers                  # Memory-efficient attention
```

### Hardware Targets
- **Development**: Google Colab T4 GPU (16GB VRAM)
- **Training**: Batch size 2-4, mixed precision (FP16)
- **Inference**: ~5-15 FPS for offline analysis

## Architecture

### Data Pipeline
```python
1. Download YouTube videos (BattleBots, NHRL, Robot Wars)
2. Extract clips at 10 FPS, 256x256 resolution
3. Extract actions using optical flow + frame differencing
4. Train world model: state + action → predicted next state
5. Evaluate: compare predictions to actual outcomes
```

### Model Components
1. **VAE Encoder** (from Stable Diffusion): Compresses video frames to latent space
2. **Action Encoder**: MLP that processes robot actions (movement, weapon)
3. **Temporal Transformer**: Learns dynamics and predicts future states
4. **VAE Decoder**: Generates predicted video frames

### Action Representation
```python
action_vector = [
    flow_x,        # Horizontal movement (-1 to 1)
    flow_y,        # Vertical movement (-1 to 1)  
    frame_diff     # Weapon/impact activity (0 to 1)
]
```

## Key Research

### Papers
- **"Robotic World Model"** (ETH Zurich, Jan 2025): Dual-autoregressive mechanism
- **"WorldEval"** (May 2025): Evaluating robot policies with world models
- **NVIDIA NitroGen** (Dec 2024): Vision-action model trained on 40K hours gameplay

### Key Insights
- World models enable offline policy evaluation without physical testing
- Vision-only learning works: NitroGen achieves 96% button accuracy from video
- Material optimization possible: Predict hit zones, reduce armor elsewhere
- Tactics > Armor: Lighter robots with better strategy can outperform heavy bots

## Common Commands

### Data Collection
```bash
# Get all URLs from channel
yt-dlp --flat-playlist --print url "CHANNEL_URL" > urls.txt

# Download videos (max 720p)
yt-dlp -f 'best[height<=720]' --download-archive archive.txt URL
```

### Training
```bash
# Start training
python train.py --batch-size 2 --mixed-precision --epochs 10

# Resume from checkpoint
python train.py --resume models/checkpoint.pt
```

## Code Style

- Use type hints and Google-style docstrings
- Max line length: 100 characters
- Always use `torch.no_grad()` for inference
- Save checkpoints with optimizer state

## Domain Knowledge

### NHRL 3lb Class Rules
- 3 pound maximum weight
- 12" cube size limit
- Human control required (no full autonomy)
- Win by KO or judge decision (aggression, control, damage)

### Robot Types
1. **Vertical Spinners**: High kinetic energy, disc/drum weapon
2. **Horizontal Spinners**: Wide attack range, bar weapon
3. **Wedges**: Defensive, low-profile
4. **Flippers**: Tactical control
5. **Hammers**: Targeted strikes

## Testing

Before committing:
1. Type check: `mypy src/`
2. Tests: `pytest tests/`
3. Notebook: Restart kernel, run all cells
4. GPU memory: Stay under 14GB on T4

## Common Issues

- **OOM Error**: Reduce batch size, enable gradient checkpointing
- **Zero actions**: Check video quality, adjust optical flow params
- **Static predictions**: Increase action conditioning, train longer

## Resources

- NHRL: https://nhrl.io/
- BattleBots: https://www.youtube.com/@BattleBots
- r/battlebots: https://reddit.com/r/battlebots

---

**Goal**: Lighter, smarter robots that win through strategy, not brute force.
