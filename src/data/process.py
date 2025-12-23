"""Process raw videos into training data."""

import argparse
from pathlib import Path
from typing import Tuple

import numpy as np


def extract_actions(video_path: Path) -> np.ndarray:
    """Extract robot actions from video using optical flow.

    Args:
        video_path: Path to input video file

    Returns:
        Array of shape (num_frames, 3) containing [flow_x, flow_y, frame_diff]
    """
    # TODO: Implement optical flow and frame differencing
    raise NotImplementedError("Action extraction not yet implemented")


def process_video(
    input_path: Path,
    output_dir: Path,
    fps: int = 10,
    resolution: Tuple[int, int] = (256, 256)
) -> None:
    """Process a single video into training clips.

    Args:
        input_path: Path to raw video file
        output_dir: Directory to save processed data
        fps: Target frames per second (default: 10)
        resolution: Target resolution (width, height) in pixels
    """
    # TODO: Implement video processing pipeline
    raise NotImplementedError("Video processing not yet implemented")


def main():
    parser = argparse.ArgumentParser(
        description="Process raw videos into training data"
    )
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Input directory or video file"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/processed"),
        help="Output directory for processed data"
    )
    parser.add_argument(
        "--fps",
        type=int,
        default=10,
        help="Target frames per second"
    )

    args = parser.parse_args()

    if args.input.is_file():
        process_video(args.input, args.output, args.fps)
    else:
        for video_file in args.input.glob("*.mp4"):
            process_video(video_file, args.output, args.fps)


if __name__ == "__main__":
    main()
