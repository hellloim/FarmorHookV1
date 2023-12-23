@echo off
title FarmorHooks Installer V1.0

:check_python
python --version >NUL 2>&1
if %errorlevel% neq 0 (
    echo.
    echo Python is not installed. Please install Python and then run this installer again.
    pause
    exit
)

echo.
echo Installing required packages...
pip install colorama requests
echo.
echo Installation complete.
echo.
echo FarmorHooks requirements installed.
echo.