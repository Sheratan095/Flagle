$name = "Flagle"

# Define venv path
$venvPath = "venv"
$venvPython = "$venvPath\Scripts\python.exe"

# Step 1: Create virtual environment if it doesn't exist
if (-Not (Test-Path $venvPath)) {
    Write-Host "Creating virtual environment..."
    python -m venv $venvPath

    if (-Not (Test-Path $venvPython)) {
        Write-Error "Failed to create virtual environment!"
        exit 1
    }

    Write-Host "Installing dependencies into virtual environment..."
    & $venvPython -m pip install --upgrade pip
    & $venvPython -m pip install pyinstaller
}
else {
    Write-Host "Virtual environment already exists."
}

# Step 2: Run PyInstaller
Write-Host "Building project with PyInstaller..."
& $venvPython -m PyInstaller `
  --icon "assets/icon.ico" `
  --onedir `
  --noconfirm `
  --windowed `
  --hidden-import "PIL._tkinter_finder" `
  --hidden-import "PIL.ImageTk" `
  source/$name.py

# Step 3: Copy resources to output folder
$distPath = "dist/$name"

if (-Not (Test-Path $distPath)) {
    Write-Error "Build failed: $distPath does not exist."
    exit 1
}

Write-Host "Copying extra files..."
Copy-Item -Path "config.json" -Destination $distPath -Force
Copy-Item -Path "assets" -Destination $distPath -Recurse -Force
Copy-Item -Path "flags" -Destination $distPath -Recurse -Force

Write-Host ""
Write-Host "Build complete! Executable and files ready in $distPath"
