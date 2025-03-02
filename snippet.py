import argparse
import logging
import os
from pathlib import Path

from moviepy import AudioFileClip, VideoFileClip


def positive_int_arg(value: str) -> int:
    int_value = int(value)
    if int_value <= 0:
        raise argparse.ArgumentTypeError("Duration must be a positive integer")
    return int_value


def input_file_arg(file: str) -> Path:
    path = Path(file)
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"The file {file} does not exist.")
    return path


def output_file_arg(file: str) -> Path:
    path = Path(file)
    if not path.parent.is_dir():
        raise argparse.ArgumentTypeError(f"The output file parent dir {path.parent} does not exist.")
    if path.exists():
        raise argparse.ArgumentTypeError(f"The output file already exists.")
    return path


def is_video_file(filepath: Path) -> bool:
    try:
        with VideoFileClip(filepath) as clip:
            # Check if the clip has a nonzero width and height
            # (which indicates that there’s a video stream)
            return clip.w > 0 and clip.h > 0
    except Exception:
        # If an exception occurs, it may not be a video file.
        return False


def create_snippet(input_file: Path, output_file: Path, duration: int):
    assert duration > 0, "Duration must be a positive integer."
    if is_video_file(input_file):
        print("Input file is a video file. Extracting audio snippet...")
        with VideoFileClip(input_file) as video:
            start = 0
            end = min(video.duration, duration)
            audio_snippet = video.audio.subclipped(start, end)
            audio_snippet.write_audiofile(output_file)
    else:
        print("Input file is an audio file. Extracting audio snippet...")
        with AudioFileClip(input_file) as audio:
            start = 0
            end = min(audio.duration, duration)
            audio_snippet = audio.subclipped(start, end)
            audio_snippet.write_audiofile(output_file)


def main():
    parser = argparse.ArgumentParser(description="Extract a snippet from an audio file.")
    parser.add_argument(
        "--file",
        type=input_file_arg,
        required=True,
        help=f"Path to the input audio file."
    )
    parser.add_argument(
        "--output",
        type=output_file_arg,
        required=True,
        help=f"Path to the output audio file."
    )
    parser.add_argument(
        "--duration",
        type=positive_int_arg,
        default=10,
        help="Duration to transcribe in seconds (positive integer, default: 10)"
    )
    args = parser.parse_args()

    create_snippet(args.file, args.output, args.duration)

    print()


if __name__ == "__main__":
    main()
