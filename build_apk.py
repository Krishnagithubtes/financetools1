#!/usr/bin/env python3
"""
Alternative APK build script using python-for-android directly
"""
import os
import subprocess
import sys

def build_apk():
    print("Building Financial Calculator APK...")
    
    # Install python-for-android
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "python-for-android"], check=True)
    except subprocess.CalledProcessError:
        print("Failed to install python-for-android")
        return False
    
    # Create APK using p4a
    try:
        cmd = [
            sys.executable, "-m", "pythonforandroid.toolchain", "apk",
            "--private", ".",
            "--package", "com.example.financialcalculator",
            "--name", "FinancialCalculator",
            "--version", "1.0",
            "--bootstrap", "sdl2",
            "--requirements", "python3,kivy,kivymd",
            "--permission", "INTERNET",
            "--permission", "ACCESS_NETWORK_STATE",
            "--arch", "arm64-v8a"
        ]
        
        subprocess.run(cmd, check=True)
        print("APK built successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Failed to build APK: {e}")
        return False

if __name__ == "__main__":
    build_apk()