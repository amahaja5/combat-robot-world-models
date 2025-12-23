# Data Directory

This directory contains training data for combat robot world models.

## Structure

```
data/
├── raw_videos/      # Raw downloaded videos from YouTube
└── processed/       # Processed training data (frames + actions)
```

## Usage

### Download Videos

```bash
python src/data/download.py --channel-url "YOUTUBE_CHANNEL_URL"
```

### Process Videos

```bash
python src/data/process.py --input data/raw_videos --output data/processed
```

## Data Format

Processed data includes:
- **Frames**: 256x256 RGB images at 10 FPS
- **Actions**: [flow_x, flow_y, frame_diff] vectors
- **Metadata**: Video source, timestamps, robot types

## Sources

Recommended YouTube channels for training data:
- BattleBots: https://www.youtube.com/@BattleBots
- NHRL: Search for "NHRL 3lb fights"
- Robot Wars: Classic episodes

## Notes

- All videos should be combat robot fights
- Prefer higher quality footage (720p minimum)
- Ensure you have permission to use the data
- Respect YouTube's terms of service
