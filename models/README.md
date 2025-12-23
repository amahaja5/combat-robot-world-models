# Models Directory

This directory contains trained model checkpoints.

## Structure

```
models/
├── checkpoints/     # Training checkpoints
└── best_model.pt    # Best performing model (after training)
```

## Model Files

Model checkpoints include:
- Model state dict
- Optimizer state
- Training configuration
- Loss history
- Epoch number

## Usage

### Load a Model

```python
import torch
from src.models.world_model import WorldModel

model = WorldModel()
checkpoint = torch.load("models/best_model.pt")
model.load_state_dict(checkpoint['model_state_dict'])
```

### Resume Training

```bash
python src/training/train.py --resume models/checkpoints/checkpoint_1000.pt
```

## Notes

- Models are saved in PyTorch format (.pt)
- Each checkpoint is ~200MB (depending on architecture)
- Best model is automatically updated during training
