import argparse
import logging
import os
from pathlib import Path
from google import genai

LINUS_AUDIO_FILE = Path('media') / 'Linus_pronounces_linux_(english).ogg'
TRANSCRIBE_PROMPT = 'Generate a transcript of the speech.'

def transcribe_audio(input_file: Path):
    assert input_file.exists(), f"File {input_file} does not exist."
    # This uses the API key from environment variable GOOGLE_API_KEY
    client = genai.Client()

    logging.debug(f"# Uploading file: {input_file}...")
    audio_file = client.files.upload(file=input_file)

    logging.debug("# Analysing file...")
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp",
        contents=[TRANSCRIBE_PROMPT, audio_file]
    )
    return response.text


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
    args = parser.parse_args()

    # Convert the provided file path to a Path object
    audio_path = Path(args.file)

    # Configure logging based on command-line arguments
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(process)d] %(levelname)s - %(message)s"
    )

    transcription = transcribe_audio(audio_path)

    print(transcription)


if __name__ == "__main__":
    main()
