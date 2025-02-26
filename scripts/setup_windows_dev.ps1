<#
.SYNOPSIS
Installs Git, Python, and uv tool on Windows using winget (where available) and pip.

.DESCRIPTION
This script automates the installation of Git, Python, and the uv tool on Windows.
It assumes winget is available and uses it to install Git and Python.
Then, it uses pip to install the uv tool.
The script will fail and exit if winget is not available.

.NOTES
Requires PowerShell 5.1 or later.
Requires Administrator privileges to install software.
Assumes winget is available on the system. If winget is not available, the script will exit.
#>

# --- Configuration ---
$gitPackageName = "Git.Git" # Package name for Git on winget
$pythonPackageName = "Python.Python.3.12" # Example package name for Python 3.12. Adjust if needed.
$uvPackageName = "uv" # Package name for uv on pip

# --- Helper Functions ---

function Test-CommandExists {
    param(
        [string]$CommandName
    )
    return Get-Command -Name $CommandName -ErrorAction SilentlyContinue
}

function Install-WingetPackage {
    param(
        [string]$PackageName
    )
    Write-Host "Attempting to install '$PackageName' using winget..."
    winget install --exact --id $PackageName --accept-source-agreements
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Successfully installed '$PackageName' using winget." -ForegroundColor Green
        return $true
    } else {
        Write-Host "Failed to install '$PackageName' using winget. Error code: $($LASTEXITCODE)" -ForegroundColor Red
        return $false
    }
}

function Install-PipPackage {
    param(
        [string]$PackageName
    )
    Write-Host "Attempting to install '$PackageName' using pip..."
    python -m pip install --upgrade pip # Ensure pip is up to date
    python -m pip install $PackageName
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Successfully installed '$PackageName' using pip." -ForegroundColor Green
        return $true
    } else {
        Write-Host "Failed to install '$PackageName' using pip. Error code: $($LASTEXITCODE)" -ForegroundColor Red
        return $false
    }
}

function Check-GitInstalled {
    Write-Host "Checking if Git is installed..."
    if (Test-CommandExists git) {
        git --version
        Write-Host "Git is already installed." -ForegroundColor Green
        return $true
    } else {
        Write-Host "Git is not installed." -ForegroundColor Yellow
        return $false
    }
}

function Check-PythonInstalled {
    Write-Host "Checking if Python is installed..."
    if (Test-CommandExists python) {
        python --version
        Write-Host "Python is already installed." -ForegroundColor Green
        return $true
    } else {
        Write-Host "Python is not installed." -ForegroundColor Yellow
        return $false
    }
}

function Check-UVInstalled {
    Write-Host "Checking if uv is installed..."
    if (Test-CommandExists uv) {
        uv --version
        Write-Host "uv is already installed." -ForegroundColor Green
        return $true
    } else {
        Write-Host "uv is not installed." -ForegroundColor Yellow
        return $false
    }
}

# --- Main Script ---

Write-Host "--- Starting Git, Python, and uv Installation Script ---"

# 1. Check if winget is available - Fail if not
Write-Host "Checking if winget is available..."
if (-not (Test-CommandExists winget)) {
    Write-Error "winget is not available on this system. This script requires winget. Please install winget and try again."
    return # Exit the script if winget is not available
}
Write-Host "winget is available. Proceeding with installation." -ForegroundColor Green

# 2. Install Git if not installed
Write-Host "" # Add an empty line for readability
Write-Host "--- Git Installation ---"
if (-not (Check-GitInstalled)) {
    if (-not (Install-WingetPackage -PackageName $gitPackageName)) {
        Write-Error "Failed to install Git using winget. Script cannot continue."
        return # Exit if Git installation fails
    } else {
        Write-Host "Git installed successfully using winget." -ForegroundColor Green
        Check-GitInstalled # Verify Git installation
    }
} else {
    Write-Host "Git is already installed. Skipping Git installation." -ForegroundColor Green
}

# 3. Install Python if not installed
Write-Host "" # Add an empty line for readability
Write-Host "--- Python Installation ---"
if (-not (Check-PythonInstalled)) {
    if (-not (Install-WingetPackage -PackageName $pythonPackageName)) {
        Write-Error "Failed to install Python using winget. Script cannot continue."
        return # Exit if Python installation fails
    } else {
        Write-Host "Python installed successfully using winget." -ForegroundColor Green
        Check-PythonInstalled # Verify Python installation
    }
} else {
    Write-Host "Python is already installed. Skipping Python installation." -ForegroundColor Green
}

# 4. Install uv using pip if not installed
Write-Host "" # Add an empty line for readability
Write-Host "--- uv tool Installation ---"
if (-not (Check-UVInstalled)) {
    if (Install-PipPackage -PackageName $uvPackageName) {
        Write-Host "uv tool installed successfully." -ForegroundColor Green
        Check-UVInstalled # Verify uv installation
    } else {
        Write-Error "Failed to install uv tool using pip. Please check errors above and ensure Python and pip are working correctly. Script cannot continue."
        return # Exit if uv installation fails
    }
} else {
    Write-Host "uv tool is already installed. Skipping uv installation." -ForegroundColor Green
}


Write-Host ""
Write-Host "--- Git, Python, and uv Installation Script Completed ---"
Write-Host "Please verify the installations manually by running 'git --version', 'python --version' and 'uv --version' in a new PowerShell or Command Prompt window."
Write-Host "You might need to close and reopen your terminal for environment changes to take effect."
