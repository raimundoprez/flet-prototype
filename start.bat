@echo off
setlocal

echo =====================================
echo           STARTING FLET APP
echo =====================================
echo.

:: script variables (ASSETS_DIR is relative to MAIN_PATH)
set VENV_PATH=VEnvWindows
set REQS_FILE=requirements.txt
set MAIN_PATH=src/main.py
set ASSETS_DIR=../resource/assets
set PYTHON_MIN_MAJOR=3
set PYTHON_MIN_MINOR=10
set FLET_DEV_MODE=true
set FLET_WEB_MODE=false

:: check python installation
echo [INFO] Checking Python installation...
python --version >nul 2>&1

if %errorlevel% neq 0 (
    echo [ERROR] Python not detected in PATH.
	pause
    exit /b
)

:: verify minimum Python version
echo [INFO] Verifying minimum Python version (%PYTHON_MIN_MAJOR%.%PYTHON_MIN_MINOR%)...
python -c "import sys; sys.exit(0 if sys.version_info >= (%PYTHON_MIN_MAJOR%, %PYTHON_MIN_MINOR%) else 1)" >nul 2>&1

if %errorlevel% neq 0 (
    echo [ERROR] Python ^(%PYTHON_MIN_MAJOR%.%PYTHON_MIN_MINOR%^)+ required. Current version:
    python --version
	pause
    exit /b
)

:: create and/or activate env
if not exist "%VENV_PATH%" (
    echo [INFO] Creating virtual environment...
    python -m venv "%VENV_PATH%"

    if %errorlevel% neq 0 (
        echo [ERROR] Failed to create a virtual environment.
        pause
        exit /b
    )
)

echo [INFO] Activating virtual environment...
call "%VENV_PATH%\Scripts\activate"

if "%VIRTUAL_ENV%"=="" (
    echo [ERROR] Failed to activate the virtual environment.
    pause
    exit /b
)

:: install Python packages
echo [INFO] Installing packages from %REQS_FILE%...
pip install -r "%REQS_FILE%"

if %errorlevel% neq 0 (
    echo [ERROR] Failed to install the required packages.
    pause
    exit /b
)

:: build the start command
set EXEC_CMD=flet

if "%FLET_DEV_MODE%"=="true" (
    set EXEC_CMD=%EXEC_CMD% run -r
)

if "%FLET_WEB_MODE%"=="true" (
    set EXEC_CMD=%EXEC_CMD% --web
)

set EXEC_CMD=%EXEC_CMD% --assets "%ASSETS_DIR%"
set EXEC_CMD=%EXEC_CMD% "%MAIN_PATH%"

:: start the app
echo [INFO] Starting Flet application...
%EXEC_CMD%

if %errorlevel% neq 0 (
    echo [ERROR] Flet crashed with error code %errorlevel%
    pause
    exit /b
)

echo [INFO] Application closed normally.