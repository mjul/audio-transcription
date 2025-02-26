# audio-transcription
Generate transcripts for audio files


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

Activate the virtual environment
```powershell
  .venv\Scripts\activate
```
