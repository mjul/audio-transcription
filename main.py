import os
import argparse
from pathlib import Path
from google import genai

LINUS_AUDIO_FILE = Path('media') / 'Linus_pronounces_linux_(english).ogg'
TRANSCRIBE_PROMPT = 'Generate a transcript of the speech.'


def log(message: str):
    print(
        f"[{os.getpid()}] {message}"
    )


def transcribe_audio(input_file: Path):
    # This uses the API key from environment variable GOOGLE_API_KEY
    client = genai.Client()

    log(f"# Uploading file: {input_file}...")
    audio_file = client.files.upload(file=input_file)

    log("# Analysing file...")
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
    args = parser.parse_args()

    # Convert the provided file path to a Path object
    audio_path = Path(args.file)

    transcription = transcribe_audio(audio_path)

    print(transcription)


if __name__ == "__main__":
    main()
