import os
from pathlib import Path
from google import genai

LINUS_AUDIO_FILE = Path('media') / 'Linus_pronounces_linux_(english).ogg'
TRANSCRIBE_PROMPT = 'Generate a transcript of the speech.'


def main():
    # This uses the API key from environment variable GOOGLE_API_KEY
    client = genai.Client()

    print(f"Uploading file: {LINUS_AUDIO_FILE}...")
    audio_file = client.files.upload(file=LINUS_AUDIO_FILE)
    print("Analysing file...")
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp",
        contents=[TRANSCRIBE_PROMPT, audio_file]
    )
    print(response.text)


if __name__ == "__main__":
    main()
