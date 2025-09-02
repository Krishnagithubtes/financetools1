"""
Public Provident Fund (PPF) Calculator Module
Handles PPF calculations, tax benefits, and maturity projections
"""

import math
from datetime import datetime, timedelta

class PPFCalculator:
    """PPF Calculator with all features"""
    
    def __init__(self):
        self.current_rate = 7.1  # Current PPF interest rate (2024)
        self.min_deposit = 500   # Minimum annual deposit
        self.max_deposit = 150000  # Maximum annual deposit
        self.lock_period = 15    # Lock-in period in years
        self.tax_exemption_limit = 150000  # 80C limit
    
    def calculate_ppf_maturity(self, annual_deposit, years=15, interest_rate=None):
        """Calculate PPF maturity amount"""
        if interest_rate is None:
            interest_rate = self.current_rate
        
        if annual_deposit < self.min_deposit:
            return None, f"Minimum deposit is ₹{self.min_deposit}"
        
        if annual_deposit > self.max_deposit:
            return None, f"Maximum deposit is ₹{self.max_deposit}"
        
        # PPF compounds annually
        r = interest_rate / 100
        maturity_amount = 0
        
        # Calculate year by year compounding
        for year in range(years):
            # Deposit made at beginning of year
            deposit_value = annual_deposit * ((1 + r) ** (years - year))
            maturity_amount += deposit_value
        
        total_invested = annual_deposit * years
        interest_earned = maturity_amount - total_invested
        
        return {
            'maturity_amount': maturity_amount,
            'total_invested': total_invested,
            'interest_earned': interest_earned,
            'effective_rate': (interest_earned / total_invested) * 100,
            'years': years,
            'annual_deposit': annual_deposit
        }, None
    
    def calculate_monthly_target(self, target_amount, years=15, interest_rate=None):
        """Calculate required monthly deposit to reach target"""
        if interest_rate is None:
            interest_rate = self.current_rate
        
        r = interest_rate / 100
        
        # Use formula to find required annual deposit
        # Target = Annual_Deposit * [((1+r)^n - 1) / r] * (1+r)
        factor = (((1 + r) ** years - 1) / r) * (1 + r)
        required_annual = target_amount / factor
        required_monthly = required_annual / 12
        
        if required_annual > self.max_deposit:
            return None, f"Required annual deposit ₹{required_annual:.0f} exceeds limit of ₹{self.max_deposit}"
        
        return {
            'required_monthly': required_monthly,
            'required_annual': required_annual,
            'target_amount': target_amount,
            'years': years,
            'total_investment': required_annual * years
        }, None
    
    def calculate_tax_benefits(self, annual_deposit):
        """Calculate tax benefits under Section 80C"""
        eligible_amount = min(annual_deposit, self.tax_exemption_limit)
        
        # Tax savings for different tax brackets
        tax_brackets = {
            '5%': eligible_amount * 0.05,
            '20%': eligible_amount * 0.20,
            '30%': eligible_amount * 0.30
        }
        
        return {
            'eligible_amount': eligible_amount,
            'tax_savings': tax_brackets,
            'max_benefit': tax_brackets['30%']
        }
    
    def calculate_extension_benefits(self, maturity_amount, extension_years=5):
        """Calculate benefits of PPF extension"""
        # After 15 years, can extend in blocks of 5 years
        # Can withdraw partial amount or continue without deposits
        
        # Option 1: Continue with deposits
        additional_deposits = self.max_deposit * extension_years
        r = self.current_rate / 100
        
        # Existing amount grows
        existing_growth = maturity_amount * ((1 + r) ** extension_years)
        
        # New deposits compound
        new_deposits_value = 0
        for year in range(extension_years):
            deposit_value = self.max_deposit * ((1 + r) ** (extension_years - year))
            new_deposits_value += deposit_value
        
        total_after_extension = existing_growth + new_deposits_value
        
        # Option 2: No new deposits, just growth
        growth_only = maturity_amount * ((1 + r) ** extension_years)
        
        return {
            'with_deposits': {
                'final_amount': total_after_extension,
                'additional_investment': additional_deposits,
                'total_growth': total_after_extension - maturity_amount - additional_deposits
            },
            'without_deposits': {
                'final_amount': growth_only,
                'growth': growth_only - maturity_amount
            },
            'extension_years': extension_years
        }
    
    def compare_with_alternatives(self, annual_deposit, years=15):
        """Compare PPF with other investment options"""
        
        # PPF calculation
        ppf_result, _ = self.calculate_ppf_maturity(annual_deposit, years)
        
        # FD at 6.5%
        fd_rate = 6.5 / 100
        fd_maturity = annual_deposit * (((1 + fd_rate) ** years - 1) / fd_rate) * (1 + fd_rate)
        
        # ELSS (tax saving mutual fund) at 12%
        elss_rate = 12 / 100
        elss_maturity = annual_deposit * (((1 + elss_rate) ** years - 1) / elss_rate) * (1 + elss_rate)
        
        # NSC at 6.8%
        nsc_rate = 6.8 / 100
        nsc_maturity = annual_deposit * (((1 + nsc_rate) ** years - 1) / nsc_rate) * (1 + nsc_rate)
        
        return {
            'PPF': {
                'maturity': ppf_result['maturity_amount'],
                'tax_free': True,
                'lock_in': '15 years',
                'rate': f"{self.current_rate}%"
            },
            'Fixed_Deposit': {
                'maturity': fd_maturity,
                'tax_free': False,
                'lock_in': 'Flexible',
                'rate': '6.5%'
            },
            'ELSS': {
                'maturity': elss_maturity,
                'tax_free': False,
                'lock_in': '3 years',
                'rate': '12% (assumed)'
            },
            'NSC': {
                'maturity': nsc_maturity,
                'tax_free': False,
                'lock_in': '5 years',
                'rate': '6.8%'
            }
        }
    
    def calculate_loan_against_ppf(self, ppf_balance, loan_percentage=25):
        """Calculate loan eligibility against PPF"""
        # Can take loan from 3rd year onwards
        # Maximum 25% of balance at end of 2nd preceding year
        
        max_loan = ppf_balance * (loan_percentage / 100)
        interest_rate = self.current_rate + 1  # PPF rate + 1%
        
        return {
            'max_loan_amount': max_loan,
            'interest_rate': interest_rate,
            'repayment_period': '36 months maximum',
            'eligibility': 'From 3rd financial year'
        }
    
    def calculate_partial_withdrawal(self, ppf_balance, withdrawal_percentage=50):
        """Calculate partial withdrawal after 7th year"""
        # Can withdraw up to 50% from 7th year onwards
        
        max_withdrawal = ppf_balance * (withdrawal_percentage / 100)
        
        return {
            'max_withdrawal': max_withdrawal,
            'eligibility': 'From 7th financial year',
            'frequency': 'Once per financial year',
            'tax_implication': 'Tax-free'
        }

# Demo functions
def demo_ppf_calculations():
    """Demo PPF calculator functionality"""
    ppf = PPFCalculator()
    
    print("=== PPF Calculator Demo ===\n")
    
    # Basic maturity calculation
    print("1. PPF Maturity Calculation:")
    result, error = ppf.calculate_ppf_maturity(150000, 15)
    if result:
        print(f"Annual Deposit: ₹{result['annual_deposit']:,}")
        print(f"Maturity Amount: ₹{result['maturity_amount']:,.0f}")
        print(f"Total Invested: ₹{result['total_invested']:,}")
        print(f"Interest Earned: ₹{result['interest_earned']:,.0f}")
        print(f"Effective Rate: {result['effective_rate']:.1f}%\n")
    
    # Target-based calculation
    print("2. Target-based Calculation:")
    target_result, error = ppf.calculate_monthly_target(5000000, 15)
    if target_result:
        print(f"Target Amount: ₹{target_result['target_amount']:,}")
        print(f"Required Monthly: ₹{target_result['required_monthly']:,.0f}")
        print(f"Required Annual: ₹{target_result['required_annual']:,.0f}\n")
    
    # Tax benefits
    print("3. Tax Benefits:")
    tax_benefits = ppf.calculate_tax_benefits(150000)
    print(f"Eligible Amount: ₹{tax_benefits['eligible_amount']:,}")
    print(f"Tax Savings (30% bracket): ₹{tax_benefits['max_benefit']:,.0f}\n")
    
    # Comparison with alternatives
    print("4. Investment Comparison:")
    comparison = ppf.compare_with_alternatives(150000, 15)
    for investment, details in comparison.items():
        print(f"{investment}: ₹{details['maturity']:,.0f} ({details['rate']})")
    
    print("\n=== Demo Complete ===")

if __name__ == "__main__":
    demo_ppf_calculations()