"""Tests for world model architecture."""

import pytest
import torch
from src.models.world_model import WorldModel, ActionEncoder


def test_action_encoder():
    """Test action encoder forward pass."""
    encoder = ActionEncoder(action_dim=3, hidden_dim=256)
    actions = torch.randn(4, 3)  # Batch of 4 actions
    output = encoder(actions)
    assert output.shape == (4, 256)


def test_world_model_forward():
    """Test world model forward pass."""
    model = WorldModel(latent_dim=512, action_dim=3, hidden_dim=256)
    state = torch.randn(4, 512)  # Batch of 4 states
    action = torch.randn(4, 3)   # Batch of 4 actions
    next_state = model(state, action)
    assert next_state.shape == (4, 512)


def test_world_model_prediction_different():
    """Test that different actions produce different predictions."""
    model = WorldModel(latent_dim=512, action_dim=3, hidden_dim=256)
    state = torch.randn(1, 512)
    action1 = torch.tensor([[1.0, 0.0, 0.5]])
    action2 = torch.tensor([[-1.0, 0.0, 0.5]])

    with torch.no_grad():
        pred1 = model(state, action1)
        pred2 = model(state, action2)

    # Different actions should produce different predictions
    assert not torch.allclose(pred1, pred2)
