# Experiment: Use the Whisper model to transcribe an audio file.

# 1) boot up the Whisper model on the CUDA GPU.
# 2) feed it the audio file,
# 3) print the transcript

from faster_whisper import WhisperModel
import torch
from pathlib import Path


def format_timestamp(seconds):
    total_seconds = int(seconds)
    total_minutes = int(seconds // 60)
    total_hours = int(total_minutes // 3600)
    hh = total_hours
    mm = total_minutes % 60
    ss = total_seconds % 60
    return f"{hh}:{mm:02}:{ss:02}"


def transcribe_audio(audio_file_path, model_name):
    # Check if CUDA is available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    compute_type = "float16" if device == "cuda" else "float32"

    # Load the model (using medium model for good balance of accuracy and speed)
    whisper_model = WhisperModel(model_name,
                                 device=device,
                                 compute_type=compute_type)

    # Transcribe the audio file
    segments, info = whisper_model.transcribe(audio_file_path, language="en", task="transcribe", word_timestamps=True)

    # Combine all segments into one transcript
    result = " ".join([f"[{format_timestamp(segment.start)}] {segment.text}" for segment in segments])
    return result


if __name__ == "__main__":
    # Replace with your audio file path
    # audio_file = Path() / "media" / "Linus_pronounces_linux_(english).ogg"
    audio_file = Path() / "media" / "Speech_12dB_alaw8.flac"

    for model in [
        "small", "medium", "large-v3"
    ]:
        try:
            transcript = transcribe_audio(audio_file, model)
            print(f"Transcription ({model}):")
            print(transcript)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
