# audio-transcription

Generate transcripts for audio files

# Usage

Set the environment variable `GOOGLE_API_KEY` with your Google Gemini API key before running.

## Example usage

### Linus Quote

```powershell
python --verbose --file "media\Linus_pronounces_linux_(english).ogg"
```

```
Hello, this is Linus Torvalds and I pronounce Linux as Linux.
```

### Opus Speech Full Length

```powershell
python main.py --file .\media\Speech_12dB_alaw8.flac
```

```
The birch canoe slid on the smooth planks. Glue the sheet to the dark blue background. It's easy to tell the depth of a well. Four hours of steady work faced us.
```

### Opus Speech with Duration

```powershell
   python main.py --file .\media\Speech_12dB_alaw8.flac --duration 2
```

```
The birch canoe slid on the smooth planks.
```

# Development Notes

## Windows Development Setup

You need to install git, Python and uv to use this project.

Use an Administrator PowerShell to check that git and python are installed or install them:

```powershell
    winget install Git.Git
    python
    winget install --id=astral-sh.uv  -e
```

Restart the terminal after installing the packages to refresh the environment.

Create the virtual environment

```powershell
    uv venv --python=python3.12
```

Activate the virtual environment (first line only if needed)

```powershell
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
    .venv\Scripts\activate
```

# Attributions

Some media files are included as examples:

- The Linus Thorvalds audio file is from <https://commons.wikimedia.org/wiki/File:Linus_pronounces_linux_(english).oga>
- The Opus speech example is from <https://opus-codec.org/examples/> where it is released under Creative Commons CC BY
  3.0.
