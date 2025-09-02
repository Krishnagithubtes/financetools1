#!/usr/bin/env python3
"""
Enhanced Financial Calculator App Launcher
Features: Login System, GST Calculator, ATM Finder with Maps, Dark Mode UI
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        'kivymd',
        'kivy', 
        'requests'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    return missing_packages

def install_dependencies():
    """Install missing dependencies"""
    import subprocess
    
    print("Installing required dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("Failed to install dependencies automatically.")
        print("Please run: pip install -r requirements.txt")
        return False

def main():
    """Main launcher function"""
    print("=" * 50)
    print("Financial Calculator App - Enhanced Version")
    print("=" * 50)
    print("Features:")
    print("• EMI, RD, FD, Loan Calculators")
    print("• GST Calculator (Add/Remove GST)")
    print("• Currency Converter")
    print("• Investment Comparison Tool")
    print("• Bank Holidays Calendar")
    print("• ATM Finder with Map Integration")
    print("• Credit Score Information")
    print("• Login System (admin/123)")
    print("• Dark/Light Mode Toggle")
    print("=" * 50)
    
    # Check dependencies
    missing = check_dependencies()
    if missing:
        print(f"Missing dependencies: {', '.join(missing)}")
        install_choice = input("Install missing dependencies? (y/n): ").lower()
        
        if install_choice == 'y':
            if not install_dependencies():
                return
        else:
            print("Cannot run app without required dependencies.")
            return
    
    try:
        # Import and run the enhanced app
        from main_enhanced import FinancialCalculatorApp
        
        print("\\nStarting Financial Calculator App...")
        print("Login Credentials: Username=admin, Password=123")
        print("Press Ctrl+C to exit")
        print("=" * 50)
        
        app = FinancialCalculatorApp()
        app.run()
        
    except ImportError as e:
        print(f"Error importing app modules: {e}")
        print("Please ensure all files are in the correct location.")
        
    except KeyboardInterrupt:
        print("\\n\\nApp closed by user")
        
    except Exception as e:
        print(f"\\nAn error occurred: {e}")
        print("Please check your installation and try again")

if __name__ == "__main__":
    main()