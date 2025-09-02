@echo off
title Financial Calculator App - Enhanced
color 0A

echo ================================================
echo    Financial Calculator App - Enhanced Version
echo ================================================
echo.
echo Features:
echo - Login System (admin/123)
echo - EMI, RD, FD, Loan Calculators  
echo - GST Calculator (Add/Remove GST)
echo - Currency Converter
echo - Investment Comparison
echo - Bank Holidays Calendar
echo - ATM Finder with Map Integration
echo - Credit Score Information
echo - Dark/Light Mode Toggle
echo.
echo ================================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo Installing/Updating dependencies...
pip install -r requirements.txt

echo.
echo Starting Financial Calculator App...
echo Login with: Username=admin, Password=123
echo.
echo Press Ctrl+C to exit the app
echo ================================================
echo.

python run_enhanced.py

echo.
echo App closed. Press any key to exit...
pause >nul