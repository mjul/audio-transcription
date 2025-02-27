import argparse
import logging
import os
from pathlib import Path

from moviepy import AudioFileClip


def positive_int(value: str) -> int:
    int_value = int(value)
    if int_value <= 0:
        raise argparse.ArgumentTypeError("Duration must be a positive integer")
    return int_value


def input_file(file: str) -> Path:
    path = Path(file)
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"The file {file} does not exist.")
    return path


def output_file(file: str) -> Path:
    path = Path(file)
    if not path.parent.is_dir():
        raise argparse.ArgumentTypeError(f"The output file parent dir {path.parent} does not exist.")
    if path.exists():
        raise argparse.ArgumentTypeError(f"The output file already exists.")
    return path


def create_snippet(input: Path, output: Path, duration: int):
    assert duration > 0, "Duration must be a positive integer."
    with AudioFileClip(input) as audio:
        start = 0
        end = min(audio.duration, duration)
        audio_snippet = audio.subclipped(start, end)
        audio_snippet.write_audiofile(output)


def main():
    parser = argparse.ArgumentParser(description="Extract a snippet from an audio file.")
    parser.add_argument(
        "--file",
        type=input_file,
        required=True,
        help=f"Path to the input audio file."
    )
    parser.add_argument(
        "--output",
        type=output_file,
        required=True,
        help=f"Path to the output audio file."
    )
    parser.add_argument(
        "--duration",
        type=positive_int,
        default=10,
        help="Duration to transcribe in seconds (positive integer, default: 10)"
    )
    args = parser.parse_args()

    create_snippet(args.file, args.output, args.duration)

    print()


if __name__ == "__main__":
    main()
