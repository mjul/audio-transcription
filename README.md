# audio-transcription

Generate transcripts for audio files

# Usage

Set the environment variable `GOOGLE_API_KEY` with your Google Gemini API key before running.

```powershell
   python --verbose --file "media\Linus_pronounces_linux_(english).ogg"
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

- <https://commons.wikimedia.org/wiki/File:Linus_pronounces_linux_(english).oga>
