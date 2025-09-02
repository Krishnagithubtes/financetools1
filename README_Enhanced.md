# Enhanced Financial Calculator Android App

A comprehensive financial calculator app built with Python using KivyMD framework featuring login system, GST calculator, ATM finder with maps, and dark mode UI.

## 🚀 New Features Added

### 🔐 Login System
- **Username**: `admin`
- **Password**: `123`
- Secure authentication with session management
- User role management (admin/user)
- Password hashing for security

### 🧮 GST Calculator
- **Add GST**: Calculate total amount including GST
- **Remove GST**: Extract base amount from GST-inclusive price
- Shows CGST and SGST breakdown
- Supports all GST rates (5%, 12%, 18%, 28%)

### 🗺️ Enhanced ATM Finder
- Find ATMs near any location
- **Map Integration**: Opens Google Maps for directions
- Shows distance to nearest ATMs
- Lists major bank ATMs (SBI, HDFC, ICICI, Axis, PNB, BOB)

### 🎨 Improved UI/UX
- **Dark/Light Mode Toggle**: Switch themes instantly
- Enhanced styling with custom color schemes
- Better typography and spacing
- Responsive design for different screen sizes
- Material Design 3 components

## 📱 All Features

### Financial Calculators
- **EMI Calculator**: Loan EMI with detailed breakdown
- **RD Calculator**: Recurring Deposit maturity calculator
- **FD Calculator**: Fixed Deposit returns calculator
- **Loan Calculator**: Comprehensive loan analysis

### Additional Tools
- **GST Calculator**: Add/Remove GST calculations
- **Investment Comparison**: Compare FD, RD, SIP, PPF returns
- **Currency Converter**: Convert between USD, INR, EUR, GBP
- **Bank Holidays**: 2024 bank holidays calendar
- **ATM Finder**: Find ATMs with map directions
- **Credit Score Info**: Credit score ranges and improvement tips

## 🛠️ Setup Instructions

### Quick Start (Windows)
1. **Double-click** `run_enhanced.bat`
2. The script will automatically install dependencies
3. App will launch with login screen
4. Use credentials: `admin` / `123`

### Manual Setup
1. **Install Python 3.8+** from [python.org](https://python.org)

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the enhanced app**
   ```bash
   python run_enhanced.py
   ```

### Building for Android
1. **Install Buildozer**
   ```bash
   pip install buildozer
   ```

2. **Build APK**
   ```bash
   buildozer android debug
   ```

## 🔧 Project Structure

```
financial_calculator_app/
├── main_enhanced.py       # Enhanced main application
├── main.py               # Original application
├── auth.py               # Authentication system
├── styles.py             # Styling configurations
├── src/
│   └── utils.py          # Utility functions
├── assets/               # App assets
├── requirements.txt      # Dependencies
├── buildozer.spec       # Android build config
├── run_enhanced.py      # Enhanced launcher
├── run_enhanced.bat     # Windows launcher
└── README_Enhanced.md   # This file
```

## 🎯 Usage Guide

### Login
1. Launch app using `run_enhanced.bat` or `python run_enhanced.py`
2. Enter username: `admin`
3. Enter password: `123`
4. Click LOGIN

### GST Calculator
1. Select "GST Calculator" from home screen
2. Enter amount and GST rate
3. Choose "Add GST" or "Remove GST"
4. View detailed breakdown with CGST/SGST

### ATM Finder with Maps
1. Select "ATM Finder" from home screen
2. Enter your location or PIN code
3. Click "Find ATMs" to see nearby ATMs
4. Click "Open Map" to get directions via Google Maps

### Theme Toggle
- Click the theme icon (🌓) in the top bar
- Instantly switch between dark and light modes
- Settings are remembered across sessions

## 🧮 Calculation Examples

### EMI Calculator
- **Input**: ₹500,000 loan, 8.5% rate, 60 months
- **Output**: Monthly EMI, total amount, interest breakdown

### GST Calculator
- **Add GST**: ₹1000 + 18% GST = ₹1180 (CGST: ₹90, SGST: ₹90)
- **Remove GST**: ₹1180 with 18% GST = ₹1000 base amount

### Investment Comparison
- **Input**: ₹100,000 for 5 years
- **Output**: FD vs RD vs SIP vs PPF returns comparison

## 🔒 Security Features

- Password hashing using SHA-256
- Session management with timeout
- Input sanitization to prevent injection attacks
- Security event logging
- User role-based access control

## 🎨 Styling System

### Color Schemes
- **Dark Theme**: Blue primary with amber accent
- **Light Theme**: Blue primary with amber accent
- **Component Colors**: Success (Green), Warning (Orange), Error (Red)

### Typography
- Material Design typography scale
- Responsive font sizes
- Consistent spacing system

### Components
- Elevated cards with rounded corners
- Material buttons with ripple effects
- Outlined text fields with floating labels
- Smooth animations and transitions

## 📱 Mobile Optimization

- Touch-friendly interface
- Responsive layout for different screen sizes
- Optimized for Android devices
- Material Design guidelines compliance

## 🔧 Customization

### Adding New Calculators
1. Create new screen in `main_enhanced.py`
2. Add calculation logic
3. Update feature cards list
4. Add styling in `styles.py`

### Modifying Authentication
1. Edit `auth.py` for user management
2. Update login credentials
3. Add new user roles
4. Implement additional security features

### Changing Themes
1. Modify color schemes in `styles.py`
2. Update component styles
3. Add new theme variants
4. Implement theme persistence

## 🚀 Advanced Features

### Session Management
- 24-hour session timeout
- Automatic session cleanup
- Multi-user support ready

### Map Integration
- Google Maps integration for ATM directions
- Location-based services
- Real-time navigation support

### Data Persistence
- User preferences saved locally
- Calculation history (can be implemented)
- Offline functionality

## 📋 Requirements

- **Python**: 3.8 or higher
- **KivyMD**: 1.1.1 or higher
- **Kivy**: 2.1.0 or higher
- **Internet**: For currency conversion and maps
- **Storage**: 50MB for app and dependencies

## 🐛 Troubleshooting

### Common Issues
1. **Import Error**: Run `pip install -r requirements.txt`
2. **Login Failed**: Use exact credentials `admin` / `123`
3. **Map Not Opening**: Check internet connection
4. **Theme Not Switching**: Restart app if needed

### Performance Tips
- Close unused screens to save memory
- Clear app data if calculations seem slow
- Ensure stable internet for currency conversion

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

## 📞 Support

For issues or questions:
1. Check troubleshooting section
2. Review code comments
3. Test with provided examples
4. Verify all dependencies are installed

---

**Enjoy using the Enhanced Financial Calculator App! 🎉**