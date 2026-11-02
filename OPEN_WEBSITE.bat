@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
  echo ERROR: Python launcher ^(py^) was not found.
  pause
  exit /b 1
)
echo Starting local website at http://localhost:8000
echo Keep this window open while using the website. Press Ctrl+C to stop it.
start "" http://localhost:8000
py -m http.server 8000
pause
