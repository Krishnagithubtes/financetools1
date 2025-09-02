#!/usr/bin/env python3
"""
Simple Financial Calculator App Launcher
Complete version with all features
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Main launcher function"""
    print("=" * 60)
    print("    FINANCIAL CALCULATOR APP - COMPLETE VERSION")
    print("=" * 60)
    print("LOGIN SYSTEM:")
    print("   Username: admin | Password: 123")
    print()
    print("CALCULATORS:")
    print("   - EMI Calculator - Loan EMI calculations")
    print("   - RD Calculator - Recurring Deposit maturity")
    print("   - FD Calculator - Fixed Deposit returns")
    print("   - Loan Calculator - Comprehensive loan analysis")

    print("   - GST Calculator - Add/Remove GST")
    print()
    print("TOOLS:")
    print("   - Investment Comparison - Compare all options")
    print("   - Currency Converter - Multi-currency support")
    print("   - Bank Holidays - 2024 calendar")
    print("   - ATM Finder - With Google Maps integration")
    print("   - Credit Score Info - Ranges and tips")
    print()
    print("FEATURES:")
    print("   - Dark/Light Mode Toggle")
    print("   - Material Design UI")
    print("   - Responsive Layout")
    print("   - Session Management")
    print("=" * 60)
    
    try:
        # Import and run the enhanced app
        from main_enhanced import FinancialCalculatorApp
        
        print("\\nStarting Financial Calculator App...")
        print("Login with: admin / 123")
        print("Press Ctrl+C to exit")
        print("=" * 60)
        
        app = FinancialCalculatorApp()
        app.run()
        
    except ImportError as e:
        print(f"Error importing modules: {e}")
        print("Please install dependencies: pip install -r requirements.txt")
        
    except KeyboardInterrupt:
        print("\\n\\nApp closed by user")
        
    except Exception as e:
        print(f"\\nAn error occurred: {e}")
        print("Please check installation and try again")

if __name__ == "__main__":
    main()