# Financial Calculator APK

## Building APK Instructions

### Method 1: Using Buildozer (Linux/WSL recommended)
```bash
# Install buildozer
pip install buildozer

# Build APK
buildozer android debug
```

### Method 2: Using Python-for-Android
```bash
# Run the build script
python build_apk.py
```

### Method 3: Using Kivy Buildozer Docker (Recommended for Windows)
```bash
# Pull the buildozer docker image
docker pull kivy/buildozer

# Build APK using docker
docker run --rm -v "%cd%":/home/user/hostcwd kivy/buildozer android debug
```

### Method 4: Manual Setup (Advanced)
1. Install Android SDK and NDK
2. Set environment variables
3. Use python-for-android directly

## APK Features
- EMI Calculator
- RD Calculator  
- FD Calculator
- Loan Comparison
- Currency Converter
- Bank Holidays
- ATM Finder
- Credit Score Info
- Dark/Light Theme Toggle

## Requirements
- Python 3.7+
- Kivy
- KivyMD
- Android SDK (for building)

## Note
Building APK on Windows requires additional setup. Use WSL or Docker for easier building.