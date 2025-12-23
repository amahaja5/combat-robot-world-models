"""World model architecture for combat robot dynamics prediction."""

from typing import Optional

import torch
import torch.nn as nn


class ActionEncoder(nn.Module):
    """MLP encoder for robot action vectors."""

    def __init__(self, action_dim: int = 3, hidden_dim: int = 256):
        """Initialize action encoder.

        Args:
            action_dim: Dimension of action vector (default: 3 for [flow_x, flow_y, frame_diff])
            hidden_dim: Hidden layer dimension
        """
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(action_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )

    def forward(self, actions: torch.Tensor) -> torch.Tensor:
        """Encode action vector.

        Args:
            actions: Tensor of shape (batch, action_dim)

        Returns:
            Encoded actions of shape (batch, hidden_dim)
        """
        return self.net(actions)


class WorldModel(nn.Module):
    """World model for predicting combat robot dynamics."""

    def __init__(
        self,
        latent_dim: int = 512,
        action_dim: int = 3,
        hidden_dim: int = 256,
        num_layers: int = 4
    ):
        """Initialize world model.

        Args:
            latent_dim: Dimension of VAE latent space
            action_dim: Dimension of action vector
            hidden_dim: Hidden dimension for transformers
            num_layers: Number of transformer layers
        """
        super().__init__()

        # Action encoder
        self.action_encoder = ActionEncoder(action_dim, hidden_dim)

        # State projection
        self.state_proj = nn.Linear(latent_dim, hidden_dim)

        # Temporal transformer
        # TODO: Implement proper transformer architecture
        self.temporal_model = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(
                d_model=hidden_dim,
                nhead=8,
                dim_feedforward=hidden_dim * 4,
                batch_first=True
            ),
            num_layers=num_layers
        )

        # Output projection
        self.output_proj = nn.Linear(hidden_dim, latent_dim)

    def forward(
        self,
        state: torch.Tensor,
        action: torch.Tensor
    ) -> torch.Tensor:
        """Predict next state given current state and action.

        Args:
            state: Current state in latent space, shape (batch, latent_dim)
            action: Robot action, shape (batch, action_dim)

        Returns:
            Predicted next state in latent space, shape (batch, latent_dim)
        """
        # Encode inputs
        state_emb = self.state_proj(state)  # (batch, hidden_dim)
        action_emb = self.action_encoder(action)  # (batch, hidden_dim)

        # Combine state and action
        combined = state_emb + action_emb  # (batch, hidden_dim)

        # Add sequence dimension for transformer
        combined = combined.unsqueeze(1)  # (batch, 1, hidden_dim)

        # Apply temporal model
        output = self.temporal_model(combined)  # (batch, 1, hidden_dim)

        # Project to latent space
        next_state = self.output_proj(output.squeeze(1))  # (batch, latent_dim)

        return next_state
