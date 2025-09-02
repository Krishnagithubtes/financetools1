#!/usr/bin/env python3
"""
Financial Calculator App Launcher
Run this file to start the application
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from main import FinancialCalculatorApp
    print("Starting Financial Calculator App...")
    print("Features: EMI, RD, FD, Loan Calculator + Currency Converter + More")
    print("Press Ctrl+C to exit")
    
    app = FinancialCalculatorApp()
    app.run()
    
except ImportError as e:
    print(f"Error importing required modules: {e}")
    print("Please install required dependencies:")
    print("pip install -r requirements.txt")
    
except KeyboardInterrupt:
    print("\nApp closed by user")
    
except Exception as e:
    print(f"An error occurred: {e}")
    print("Please check your installation and try again")