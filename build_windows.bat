@echo off
echo Building Financial Calculator for Windows...

REM Install required packages
pip install pyinstaller

REM Create executable
pyinstaller --onefile --windowed --name "FinancialCalculator" main.py

echo Build complete! Check the dist folder for FinancialCalculator.exe
pause