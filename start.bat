@echo off
echo ================================================
echo   SAFEGRID NAVIGATOR - STARTUP SCRIPT
echo ================================================
echo.

cd /d C:\projects\SAFEGRID

echo [1/3] Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo.
echo [2/3] Installing dependencies...
pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [3/3] Starting Safegrid Navigator...
echo.
echo Backend API will start at: http://localhost:5000
echo Open frontend\index.html in your browser to use the application
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py

pause
