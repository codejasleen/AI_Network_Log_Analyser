@echo off
echo ========================================
echo AI Network Log Analyzer - Setup
echo ========================================
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt -q
echo.

REM Check if .env file exists
if not exist ".env" (
    echo WARNING: .env file not found!
    echo Creating .env file...
    echo GEMINI_API_KEY=your-gemini-api-key-here > .env
    echo.
    echo Please edit .env file and add your API key!
    echo Then run this script again.
    pause
    exit /b 1
)

REM Check if API key is set in .env
findstr /C:"your-gemini-api-key-here" .env >nul
if %errorlevel%==0 (
    echo WARNING: API key not configured in .env file!
    echo.
    echo Please edit .env file and replace:
    echo   GEMINI_API_KEY=your-gemini-api-key-here
    echo.
    echo With your actual API key from:
    echo   https://aistudio.google.com/app/apikey
    echo.
    pause
    exit /b 1
)

echo ========================================
echo Starting AI Network Log Analyzer...
echo ========================================
echo.
streamlit run app.py
