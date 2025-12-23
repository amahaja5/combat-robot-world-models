"""Download combat robot videos from YouTube."""

import argparse
from pathlib import Path
from typing import Optional


def download_videos(
    channel_url: str,
    output_dir: Path,
    max_resolution: int = 720,
    archive_file: Optional[Path] = None
) -> None:
    """Download videos from a YouTube channel.

    Args:
        channel_url: URL of the YouTube channel or playlist
        output_dir: Directory to save downloaded videos
        max_resolution: Maximum video resolution (default: 720p)
        archive_file: Path to download archive file to avoid re-downloading
    """
    # TODO: Implement using yt-dlp
    raise NotImplementedError("Video download not yet implemented")


def main():
    parser = argparse.ArgumentParser(
        description="Download combat robot videos from YouTube"
    )
    parser.add_argument(
        "--channel-url",
        required=True,
        help="YouTube channel or playlist URL"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/raw_videos"),
        help="Output directory for videos"
    )
    parser.add_argument(
        "--max-resolution",
        type=int,
        default=720,
        help="Maximum video resolution"
    )

    args = parser.parse_args()
    download_videos(args.channel_url, args.output, args.max_resolution)


if __name__ == "__main__":
    main()
