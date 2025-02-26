import argparse
import logging
import os
from pathlib import Path
from google import genai

LINUS_AUDIO_FILE = Path('media') / 'Linus_pronounces_linux_(english).ogg'
TRANSCRIBE_PROMPT = 'Generate a transcript of the speech.'


def transcribe_audio(input_file: Path, api_key: str, duration: int):
    assert input_file.exists(), f"File {input_file} does not exist."
    assert duration > 0, "Duration must be a positive integer."

    client = genai.Client(api_key=api_key)

    logging.debug(f"# Uploading file: {input_file}...")
    audio_file = client.files.upload(file=input_file)

    logging.debug("# Analysing file...")
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp",
        contents=[
            f"Provide a transcript of the speech from 00:00:00 and the next {duration} seconds. "
            f"Add timestamps for each line."
            , audio_file]
    )
    return response.text


def positive_int(value: str) -> int:
    int_value = int(value)
    if int_value <= 0:
        raise argparse.ArgumentTypeError("Duration must be a positive integer")
    return int_value


def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Transcribe an audio file using the GenAI API")
    parser.add_argument(
        "--file",
        type=str,
        default=str(LINUS_AUDIO_FILE),
        help=f"Path to the audio file (default: {LINUS_AUDIO_FILE})"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Increase output verbosity"
    )
    parser.add_argument(
        "--google-api-key",
        type=str,
        default=os.environ.get("GOOGLE_API_KEY"),
        help=("Google API key to use. "
              "If not specified, the key is read from the GOOGLE_API_KEY environment variable.")
    )
    parser.add_argument(
        "--duration",
        type=positive_int,
        default=10,
        help="Duration to transcribe in seconds (positive integer, default: 10)"
    )
    args = parser.parse_args()

    # Convert the provided file path to a Path object
    audio_path = Path(args.file)

    # Configure logging based on command-line arguments
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(process)d] %(levelname)s - %(message)s"
    )

    transcription = transcribe_audio(audio_path, args.google_api_key, args.duration)

    print(transcription)


if __name__ == "__main__":
    main()
