@echo off
setlocal
cd /d "%~dp0"
echo ========================================
echo   SUSU PC FARM - ONE-CLICK DOWNLOADER
echo ========================================
echo.
echo Choose how many NEW photos to try downloading for EACH member.
echo There are 12 members, so 50 means up to 600 new photos total.
echo Some downloads may fail due to site limits or duplicate images.
echo.
set /p COUNT=New photos per member (1-100, default 25): 
if "%COUNT%"=="" set COUNT=25
 echo %COUNT%| findstr /r "^[0-9][0-9]*$" >nul
if errorlevel 1 (
  echo Please enter a whole number between 1 and 100.
  pause
  exit /b 2
)
if %COUNT% LSS 1 (
  echo Please enter a number from 1 to 100.
  pause
  exit /b 2
)
if %COUNT% GTR 100 (
  echo Please enter a number from 1 to 100.
  pause
  exit /b 2
)
where py >nul 2>nul
if errorlevel 1 (
  echo ERROR: Python launcher ^(py^) was not found. Install Python from https://www.python.org/downloads/windows/ and enable the launcher.
  pause
  exit /b 1
)
echo.
echo Checking the free search package...
py -m pip install --upgrade ddgs
if errorlevel 1 (
  echo Could not install ddgs. Check your internet connection and try again.
  pause
  exit /b 1
)
echo.
echo Starting download for up to %COUNT% NEW photos per member. Keep this window open.
py download_photos.py %COUNT%
echo.
if errorlevel 1 (
  echo The downloader ended with an error. Read the messages above.
) else (
  echo Finished! photos.json has been rebuilt.
)
echo.
pause
