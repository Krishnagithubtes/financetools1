"""
Public Funds Calculator Module
Comprehensive calculator for various government schemes and public funds
"""

import math
from datetime import datetime, timedelta

class PublicFundsCalculator:
    """Calculator for various public investment schemes"""
    
    def __init__(self):
        # Current rates (2024)
        self.rates = {
            'ppf': 7.1,
            'nsc': 6.8,
            'kisan_vikas_patra': 7.5,
            'sukanya_samriddhi': 8.0,
            'senior_citizen_savings': 8.2,
            'post_office_td': 6.9,
            'post_office_rd': 5.8,
            'post_office_mis': 7.4
        }
        
        # Scheme limits and features
        self.scheme_details = {
            'ppf': {
                'min_deposit': 500,
                'max_deposit': 150000,
                'tenure': 15,
                'tax_benefit': True,
                'premature_withdrawal': False
            },
            'nsc': {
                'min_deposit': 1000,
                'max_deposit': None,
                'tenure': 5,
                'tax_benefit': True,
                'premature_withdrawal': False
            },
            'sukanya_samriddhi': {
                'min_deposit': 250,
                'max_deposit': 150000,
                'tenure': 21,
                'tax_benefit': True,
                'premature_withdrawal': True
            }
        }
    
    def calculate_ppf(self, annual_deposit, years=15):
        """Calculate PPF maturity"""
        rate = self.rates['ppf'] / 100
        maturity = 0
        
        for year in range(years):
            deposit_value = annual_deposit * ((1 + rate) ** (years - year))
            maturity += deposit_value
        
        total_invested = annual_deposit * years
        interest = maturity - total_invested
        
        return {
            'scheme': 'Public Provident Fund (PPF)',
            'maturity_amount': maturity,
            'total_invested': total_invested,
            'interest_earned': interest,
            'rate': self.rates['ppf'],
            'tax_free': True,
            'tenure': years
        }
    
    def calculate_nsc(self, investment_amount, years=5):
        """Calculate NSC maturity"""
        rate = self.rates['nsc'] / 100
        maturity = investment_amount * ((1 + rate) ** years)
        interest = maturity - investment_amount
        
        return {
            'scheme': 'National Savings Certificate (NSC)',
            'maturity_amount': maturity,
            'total_invested': investment_amount,
            'interest_earned': interest,
            'rate': self.rates['nsc'],
            'tax_free': False,
            'tenure': years
        }
    
    def calculate_sukanya_samriddhi(self, annual_deposit, years=21):
        """Calculate Sukanya Samriddhi Yojana"""
        rate = self.rates['sukanya_samriddhi'] / 100
        
        # Deposits for first 15 years only
        deposit_years = min(years, 15)
        maturity = 0
        
        # Calculate deposits with compounding
        for year in range(deposit_years):
            deposit_value = annual_deposit * ((1 + rate) ** (years - year))
            maturity += deposit_value
        
        total_invested = annual_deposit * deposit_years
        interest = maturity - total_invested
        
        return {
            'scheme': 'Sukanya Samriddhi Yojana',
            'maturity_amount': maturity,
            'total_invested': total_invested,
            'interest_earned': interest,
            'rate': self.rates['sukanya_samriddhi'],
            'tax_free': True,
            'tenure': years,
            'deposit_years': deposit_years
        }
    
    def calculate_kisan_vikas_patra(self, investment_amount):
        """Calculate Kisan Vikas Patra (doubles money)"""
        rate = self.rates['kisan_vikas_patra'] / 100
        
        # Calculate time to double
        doubling_time = math.log(2) / math.log(1 + rate)
        maturity_amount = investment_amount * 2
        
        return {
            'scheme': 'Kisan Vikas Patra (KVP)',
            'maturity_amount': maturity_amount,
            'total_invested': investment_amount,
            'interest_earned': investment_amount,
            'rate': self.rates['kisan_vikas_patra'],
            'doubling_time': doubling_time,
            'tax_free': False
        }
    
    def calculate_senior_citizen_savings(self, investment_amount, years=5):
        """Calculate Senior Citizen Savings Scheme"""
        rate = self.rates['senior_citizen_savings'] / 100
        
        # Quarterly interest payout
        quarterly_rate = rate / 4
        quarterly_interest = investment_amount * quarterly_rate
        annual_interest = quarterly_interest * 4
        total_interest = annual_interest * years
        
        return {
            'scheme': 'Senior Citizen Savings Scheme (SCSS)',
            'maturity_amount': investment_amount + total_interest,
            'total_invested': investment_amount,
            'interest_earned': total_interest,
            'quarterly_interest': quarterly_interest,
            'annual_interest': annual_interest,
            'rate': self.rates['senior_citizen_savings'],
            'tax_free': False,
            'tenure': years
        }
    
    def calculate_post_office_td(self, investment_amount, years=5):
        """Calculate Post Office Time Deposit"""
        rate = self.rates['post_office_td'] / 100
        maturity = investment_amount * ((1 + rate) ** years)
        interest = maturity - investment_amount
        
        return {
            'scheme': 'Post Office Time Deposit',
            'maturity_amount': maturity,
            'total_invested': investment_amount,
            'interest_earned': interest,
            'rate': self.rates['post_office_td'],
            'tax_free': False,
            'tenure': years
        }
    
    def calculate_post_office_rd(self, monthly_deposit, years=5):
        """Calculate Post Office Recurring Deposit"""
        rate = self.rates['post_office_rd'] / 100 / 12
        months = years * 12
        
        if rate == 0:
            maturity = monthly_deposit * months
        else:
            maturity = monthly_deposit * (((1 + rate) ** months - 1) / rate) * (1 + rate)
        
        total_invested = monthly_deposit * months
        interest = maturity - total_invested
        
        return {
            'scheme': 'Post Office Recurring Deposit',
            'maturity_amount': maturity,
            'total_invested': total_invested,
            'interest_earned': interest,
            'monthly_deposit': monthly_deposit,
            'rate': self.rates['post_office_rd'],
            'tax_free': False,
            'tenure': years
        }
    
    def calculate_post_office_mis(self, investment_amount):
        """Calculate Post Office Monthly Income Scheme"""
        rate = self.rates['post_office_mis'] / 100
        monthly_income = (investment_amount * rate) / 12
        annual_income = monthly_income * 12
        
        return {
            'scheme': 'Post Office Monthly Income Scheme (MIS)',
            'investment_amount': investment_amount,
            'monthly_income': monthly_income,
            'annual_income': annual_income,
            'rate': self.rates['post_office_mis'],
            'tax_free': False,
            'tenure': 5
        }
    
    def compare_all_schemes(self, investment_amount, years=5):
        """Compare all public fund schemes"""
        results = {}
        
        # PPF (if tenure allows)
        if years >= 15:
            annual_ppf = investment_amount / years
            if annual_ppf <= 150000:
                results['PPF'] = self.calculate_ppf(annual_ppf, years)
        
        # NSC
        results['NSC'] = self.calculate_nsc(investment_amount, min(years, 5))
        
        # KVP
        results['KVP'] = self.calculate_kisan_vikas_patra(investment_amount)
        
        # Post Office TD
        results['Post_Office_TD'] = self.calculate_post_office_td(investment_amount, years)
        
        # SCSS (if applicable)
        if years <= 5:
            results['SCSS'] = self.calculate_senior_citizen_savings(investment_amount, years)
        
        return results
    
    def calculate_tax_implications(self, scheme_results):
        """Calculate tax implications for different schemes"""
        tax_analysis = {}
        
        for scheme, result in scheme_results.items():
            if result.get('tax_free'):
                tax_analysis[scheme] = {
                    'taxable_interest': 0,
                    'tax_savings': 'Fully tax-free',
                    'net_return': result['maturity_amount']
                }
            else:
                # Assume 30% tax bracket
                taxable_interest = result['interest_earned']
                tax_amount = taxable_interest * 0.30
                net_return = result['maturity_amount'] - tax_amount
                
                tax_analysis[scheme] = {
                    'taxable_interest': taxable_interest,
                    'tax_amount': tax_amount,
                    'net_return': net_return,
                    'effective_rate': ((net_return - result['total_invested']) / result['total_invested']) * 100
                }
        
        return tax_analysis
    
    def get_scheme_eligibility(self, age, gender=None, investment_amount=None):
        """Check eligibility for different schemes"""
        eligibility = {}
        
        # PPF - Universal
        eligibility['PPF'] = {
            'eligible': True,
            'conditions': 'Open to all Indian residents'
        }
        
        # NSC - Universal
        eligibility['NSC'] = {
            'eligible': True,
            'conditions': 'Open to all Indian residents'
        }
        
        # Sukanya Samriddhi - Girl child
        eligibility['Sukanya_Samriddhi'] = {
            'eligible': gender == 'female' and age <= 10,
            'conditions': 'For girl child below 10 years'
        }
        
        # SCSS - Senior Citizens
        eligibility['SCSS'] = {
            'eligible': age >= 60,
            'conditions': 'For senior citizens (60+ years)'
        }
        
        # KVP - Universal
        eligibility['KVP'] = {
            'eligible': True,
            'conditions': 'Open to all Indian residents'
        }
        
        return eligibility

# Demo function
def demo_public_funds():
    """Demo public funds calculator"""
    calc = PublicFundsCalculator()
    
    print("=== Public Funds Calculator Demo ===\n")
    
    # PPF Calculation
    print("1. PPF Calculation (₹1,50,000/year for 15 years):")
    ppf_result = calc.calculate_ppf(150000, 15)
    print(f"Maturity: ₹{ppf_result['maturity_amount']:,.0f}")
    print(f"Interest: ₹{ppf_result['interest_earned']:,.0f}")
    print(f"Tax-free: {ppf_result['tax_free']}\n")
    
    # NSC Calculation
    print("2. NSC Calculation (₹1,00,000 for 5 years):")
    nsc_result = calc.calculate_nsc(100000, 5)
    print(f"Maturity: ₹{nsc_result['maturity_amount']:,.0f}")
    print(f"Interest: ₹{nsc_result['interest_earned']:,.0f}\n")
    
    # Sukanya Samriddhi
    print("3. Sukanya Samriddhi (₹1,50,000/year for 21 years):")
    ssy_result = calc.calculate_sukanya_samriddhi(150000, 21)
    print(f"Maturity: ₹{ssy_result['maturity_amount']:,.0f}")
    print(f"Interest: ₹{ssy_result['interest_earned']:,.0f}")
    print(f"Tax-free: {ssy_result['tax_free']}\n")
    
    # Comparison
    print("4. Scheme Comparison (₹1,00,000 investment):")
    comparison = calc.compare_all_schemes(100000, 5)
    for scheme, result in comparison.items():
        print(f"{scheme}: ₹{result['maturity_amount']:,.0f} ({result['rate']}%)")
    
    print("\n=== Demo Complete ===")

if __name__ == "__main__":
    demo_public_funds()