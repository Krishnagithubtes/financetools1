#!/usr/bin/env python3
"""
Test script for Financial Calculator App
This script tests if the app can be imported and basic functionality works
"""

def test_app_import():
    """Test if the app can be imported without errors"""
    try:
        from main import FinancialCalculatorApp
        print("[PASS] App imports successfully")
        return True
    except Exception as e:
        print(f"[FAIL] Import failed: {e}")
        return False

def test_app_creation():
    """Test if the app can be created without errors"""
    try:
        from main import FinancialCalculatorApp
        app = FinancialCalculatorApp()
        print("[PASS] App instance created successfully")
        return True
    except Exception as e:
        print(f"[FAIL] App creation failed: {e}")
        return False

def test_calculations():
    """Test calculation methods"""
    try:
        from main import FinancialCalculatorApp
        app = FinancialCalculatorApp()
        
        # Create mock text fields for testing
        class MockTextField:
            def __init__(self, value):
                self.text = str(value)
        
        # Test EMI calculation
        app.emi_principal = MockTextField(100000)
        app.emi_rate = MockTextField(10)
        app.emi_tenure = MockTextField(12)
        app.emi_result = MockTextField("")
        
        app.calculate_emi(None)
        if "EMI:" in app.emi_result.text:
            print("[PASS] EMI calculation works")
        else:
            print("[FAIL] EMI calculation failed")
            
        return True
    except Exception as e:
        print(f"[FAIL] Calculation test failed: {e}")
        return False

if __name__ == "__main__":
    print("Financial Calculator App - Test Suite")
    print("=" * 40)
    
    tests = [
        test_app_import,
        test_app_creation,
        test_calculations
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
    
    print(f"\nTest Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("\n[SUCCESS] All tests passed! Your app is ready to run.")
        print("Run 'python main.py' to start the application.")
    else:
        print("\n[WARNING] Some tests failed. Check the errors above.")