from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationDrawerMenu
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.scrollview import ScrollView
import math
import requests
from datetime import datetime, date
import json

class FinancialCalculatorApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        
    def build(self):
        self.screen_manager = MDScreenManager()
        
        # Create screens
        self.create_home_screen()
        self.create_emi_screen()
        self.create_rd_screen()
        self.create_fd_screen()
        self.create_loan_screen()
        self.create_currency_screen()
        self.create_bank_holiday_screen()
        self.create_atm_finder_screen()
        self.create_credit_score_screen()
        
        return self.screen_manager
    
    def create_home_screen(self):
        screen = MDScreen(name="home")
        
        layout = MDBoxLayout(orientation="vertical", spacing="20dp", padding="20dp")
        
        # Top bar
        toolbar = MDTopAppBar(
            title="Financial Calculator",
            right_action_items=[["theme-light-dark", lambda x: self.toggle_theme()]],
            elevation=2
        )
        layout.add_widget(toolbar)
        
        # Scroll view for cards
        scroll = ScrollView()
        card_layout = MDBoxLayout(orientation="vertical", spacing="15dp", adaptive_height=True)
        
        # Feature cards
        features = [
            ("EMI Calculator", "calculator", "emi"),
            ("RD Calculator", "piggy-bank", "rd"),
            ("FD Calculator", "bank", "fd"),
            ("Loan Comparison", "compare", "loan"),
            ("Currency Converter", "currency-usd", "currency"),
            ("Bank Holidays", "calendar", "bank_holiday"),
            ("ATM Finder", "map-marker", "atm_finder"),
            ("Credit Score", "chart-line", "credit_score")
        ]
        
        for title, icon, screen_name in features:
            card = self.create_feature_card(title, icon, screen_name)
            card_layout.add_widget(card)
        
        scroll.add_widget(card_layout)
        layout.add_widget(scroll)
        
        screen.add_widget(layout)
        self.screen_manager.add_widget(screen)
    
    def create_feature_card(self, title, icon, screen_name):
        card = MDCard(
            size_hint_y=None,
            height="80dp",
            elevation=3,
            padding="10dp",
            on_release=lambda x: self.switch_screen(screen_name)
        )
        
        card_layout = MDBoxLayout(orientation="horizontal", spacing="15dp")
        
        icon_btn = MDIconButton(icon=icon, theme_icon_color="Primary")
        label = MDLabel(text=title, theme_text_color="Primary", size_hint_x=0.8)
        
        card_layout.add_widget(icon_btn)
        card_layout.add_widget(label)
        card.add_widget(card_layout)
        
        return card
    
    def create_emi_screen(self):
        screen = MDScreen(name="emi")
        layout = MDBoxLayout(orientation="vertical", spacing="20dp", padding="20dp")
        
        # Top bar
        toolbar = MDTopAppBar(
            title="EMI Calculator",
            left_action_items=[["arrow-left", lambda x: self.switch_screen("home")]],
            elevation=2
        )
        layout.add_widget(toolbar)
        
        # Input fields
        self.emi_principal = MDTextField(hint_text="Principal Amount", input_filter="float")
        self.emi_rate = MDTextField(hint_text="Interest Rate (%)", input_filter="float")
        self.emi_tenure = MDTextField(hint_text="Tenure (months)", input_filter="int")
        
        layout.add_widget(self.emi_principal)
        layout.add_widget(self.emi_rate)
        layout.add_widget(self.emi_tenure)
        
        # Calculate button
        calc_btn = MDRaisedButton(text="Calculate EMI", on_release=self.calculate_emi)
        layout.add_widget(calc_btn)
        
        # Result label
        self.emi_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="100dp")
        layout.add_widget(self.emi_result)
        
        screen.add_widget(layout)
        self.screen_manager.add_widget(screen)
    
    def create_rd_screen(self):
        screen = MDScreen(name="rd")
        layout = MDBoxLayout(orientation="vertical", spacing="20dp", padding="20dp")
        
        toolbar = MDTopAppBar(
            title="RD Calculator",
            left_action_items=[["arrow-left", lambda x: self.switch_screen("home")]],
            elevation=2
        )
        layout.add_widget(toolbar)
        
        self.rd_monthly = MDTextField(hint_text="Monthly Deposit", input_filter="float")
        self.rd_rate = MDTextField(hint_text="Interest Rate (%)", input_filter="float")
        self.rd_tenure = MDTextField(hint_text="Tenure (months)", input_filter="int")
        
        layout.add_widget(self.rd_monthly)
        layout.add_widget(self.rd_rate)
        layout.add_widget(self.rd_tenure)
        
        calc_btn = MDRaisedButton(text="Calculate RD", on_release=self.calculate_rd)
        layout.add_widget(calc_btn)
        
        self.rd_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="100dp")
        layout.add_widget(self.rd_result)
        
        screen.add_widget(layout)
        self.screen_manager.add_widget(screen)
    
    def create_fd_screen(self):
        screen = MDScreen(name="fd")
        layout = MDBoxLayout(orientation="vertical", spacing="20dp", padding="20dp")
        
        toolbar = MDTopAppBar(
            title="FD Calculator",
            left_action_items=[["arrow-left", lambda x: self.switch_screen("home")]],
            elevation=2
        )
        layout.add_widget(toolbar)
        
        self.fd_principal = MDTextField(hint_text="Principal Amount", input_filter="float")
        self.fd_rate = MDTextField(hint_text="Interest Rate (%)", input_filter="float")
        self.fd_tenure = MDTextField(hint_text="Tenure (years)", input_filter="float")
        
        layout.add_widget(self.fd_principal)
        layout.add_widget(self.fd_rate)
        layout.add_widget(self.fd_tenure)
        
        calc_btn = MDRaisedButton(text="Calculate FD", on_release=self.calculate_fd)
        layout.add_widget(calc_btn)
        
        self.fd_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="100dp")
        layout.add_widget(self.fd_result)
        
        screen.add_widget(layout)
        self.screen_manager.add_widget(screen)
    
    def create_loan_screen(self):
        screen = MDScreen(name="loan")
        layout = MDBoxLayout(orientation="vertical", spacing="20dp", padding="20dp")
        
        toolbar = MDTopAppBar(
            title="Loan Comparison",
            left_action_items=[["arrow-left", lambda x: self.switch_screen("home")]],
            elevation=2
        )
        layout.add_widget(toolbar)
        
        self.loan_amount = MDTextField(hint_text="Loan Amount", input_filter="float")
        self.loan_tenure = MDTextField(hint_text="Tenure (years)", input_filter="float")
        
        layout.add_widget(self.loan_amount)
        layout.add_widget(self.loan_tenure)
        
        calc_btn = MDRaisedButton(text="Compare Loans", on_release=self.compare_loans)
        layout.add_widget(calc_btn)
        
        self.loan_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="250dp")
        layout.add_widget(self.loan_result)
        
        screen.add_widget(layout)
        self.screen_manager.add_widget(screen)
    

    
    def create_currency_screen(self):
        screen = MDScreen(name="currency")
        layout = MDBoxLayout(orientation="vertical", spacing="20dp", padding="20dp")
        
        toolbar = MDTopAppBar(
            title="Currency Converter",
            left_action_items=[["arrow-left", lambda x: self.switch_screen("home")]],
            elevation=2
        )
        layout.add_widget(toolbar)
        
        self.curr_amount = MDTextField(hint_text="Amount", input_filter="float")
        self.curr_from = MDTextField(hint_text="From Currency (e.g., USD)")
        self.curr_to = MDTextField(hint_text="To Currency (e.g., INR)")
        
        layout.add_widget(self.curr_amount)
        layout.add_widget(self.curr_from)
        layout.add_widget(self.curr_to)
        
        convert_btn = MDRaisedButton(text="Convert Currency", on_release=self.convert_currency)
        layout.add_widget(convert_btn)
        
        self.curr_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="100dp")
        layout.add_widget(self.curr_result)
        
        screen.add_widget(layout)
        self.screen_manager.add_widget(screen)
    
    def create_bank_holiday_screen(self):
        screen = MDScreen(name="bank_holiday")
        layout = MDBoxLayout(orientation="vertical", spacing="20dp", padding="20dp")
        
        toolbar = MDTopAppBar(
            title="Bank Holidays",
            left_action_items=[["arrow-left", lambda x: self.switch_screen("home")]],
            elevation=2
        )
        layout.add_widget(toolbar)
        
        check_btn = MDRaisedButton(text="Check Bank Holidays", on_release=self.check_bank_holidays)
        layout.add_widget(check_btn)
        
        self.holiday_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="300dp")
        layout.add_widget(self.holiday_result)
        
        screen.add_widget(layout)
        self.screen_manager.add_widget(screen)
    
    def create_atm_finder_screen(self):
        screen = MDScreen(name="atm_finder")
        layout = MDBoxLayout(orientation="vertical", spacing="20dp", padding="20dp")
        
        toolbar = MDTopAppBar(
            title="ATM Finder",
            left_action_items=[["arrow-left", lambda x: self.switch_screen("home")]],
            elevation=2
        )
        layout.add_widget(toolbar)
        
        self.atm_location = MDTextField(hint_text="Enter Location/PIN Code")
        layout.add_widget(self.atm_location)
        
        find_btn = MDRaisedButton(text="Find ATMs", on_release=self.find_atms)
        layout.add_widget(find_btn)
        
        self.atm_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="200dp")
        layout.add_widget(self.atm_result)
        
        screen.add_widget(layout)
        self.screen_manager.add_widget(screen)
    
    def create_credit_score_screen(self):
        screen = MDScreen(name="credit_score")
        layout = MDBoxLayout(orientation="vertical", spacing="20dp", padding="20dp")
        
        toolbar = MDTopAppBar(
            title="Credit Score Info",
            left_action_items=[["arrow-left", lambda x: self.switch_screen("home")]],
            elevation=2
        )
        layout.add_widget(toolbar)
        
        info_btn = MDRaisedButton(text="Credit Score Information", on_release=self.show_credit_info)
        layout.add_widget(info_btn)
        
        self.credit_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="300dp")
        layout.add_widget(self.credit_result)
        
        screen.add_widget(layout)
        self.screen_manager.add_widget(screen)
    
    # Calculation methods
    def calculate_emi(self, instance):
        try:
            P = float(self.emi_principal.text)
            r = float(self.emi_rate.text) / 100 / 12
            n = int(self.emi_tenure.text)
            
            emi = P * r * (1 + r)**n / ((1 + r)**n - 1)
            total_amount = emi * n
            interest = total_amount - P
            
            self.emi_result.text = f"EMI: ₹{emi:.2f}\nTotal Amount: ₹{total_amount:.2f}\nTotal Interest: ₹{interest:.2f}"
        except:
            self.emi_result.text = "Please enter valid values"
    
    def calculate_rd(self, instance):
        try:
            P = float(self.rd_monthly.text)
            r = float(self.rd_rate.text) / 100 / 12
            n = int(self.rd_tenure.text)
            
            maturity = P * (((1 + r)**n - 1) / r) * (1 + r)
            total_invested = P * n
            interest = maturity - total_invested
            
            self.rd_result.text = f"Maturity Amount: ₹{maturity:.2f}\nTotal Invested: ₹{total_invested:.2f}\nInterest Earned: ₹{interest:.2f}"
        except:
            self.rd_result.text = "Please enter valid values"
    
    def calculate_fd(self, instance):
        try:
            P = float(self.fd_principal.text)
            r = float(self.fd_rate.text) / 100
            t = float(self.fd_tenure.text)
            
            maturity = P * (1 + r)**t
            interest = maturity - P
            
            self.fd_result.text = f"Maturity Amount: ₹{maturity:.2f}\nPrincipal: ₹{P:.2f}\nInterest Earned: ₹{interest:.2f}"
        except:
            self.fd_result.text = "Please enter valid values"
    
    def compare_loans(self, instance):
        try:
            P = float(self.loan_amount.text)
            years = float(self.loan_tenure.text)
            n = years * 12
            
            # Different loan types with typical rates
            loan_types = {
                'Home Loan': 8.5,
                'Personal Loan': 12.0,
                'Car Loan': 9.5,
                'Education Loan': 10.0
            }
            
            results = []
            for loan_type, rate in loan_types.items():
                r = rate / 100 / 12
                emi = P * r * (1 + r)**n / ((1 + r)**n - 1)
                total_amount = emi * n
                interest = total_amount - P
                
                results.append(f"{loan_type} ({rate}%):\nEMI: ₹{emi:.0f} | Total: ₹{total_amount:.0f}")
            
            self.loan_result.text = f"Loan Comparison for ₹{P:.0f}:\n\n" + "\n\n".join(results)
        except:
            self.loan_result.text = "Please enter valid values"
    

    
    def convert_currency(self, instance):
        try:
            # Mock conversion rates (in real app, use API)
            rates = {
                'USD': {'INR': 83.0, 'EUR': 0.85, 'GBP': 0.73},
                'INR': {'USD': 0.012, 'EUR': 0.010, 'GBP': 0.009},
                'EUR': {'USD': 1.18, 'INR': 98.0, 'GBP': 0.86}
            }
            
            amount = float(self.curr_amount.text)
            from_curr = self.curr_from.text.upper()
            to_curr = self.curr_to.text.upper()
            
            if from_curr in rates and to_curr in rates[from_curr]:
                converted = amount * rates[from_curr][to_curr]
                self.curr_result.text = f"{amount} {from_curr} = {converted:.2f} {to_curr}"
            else:
                self.curr_result.text = "Currency pair not supported"
        except:
            self.curr_result.text = "Please enter valid values"
    
    def check_bank_holidays(self, instance):
        holidays_2024 = [
            "Jan 26 - Republic Day",
            "Mar 8 - Holi",
            "Mar 29 - Good Friday",
            "Apr 11 - Eid ul-Fitr",
            "Aug 15 - Independence Day",
            "Oct 2 - Gandhi Jayanti",
            "Oct 31 - Diwali",
            "Dec 25 - Christmas"
        ]
        
        self.holiday_result.text = "Bank Holidays 2024:\n\n" + "\n".join(holidays_2024)
    
    def find_atms(self, instance):
        location = self.atm_location.text
        if location:
            self.atm_result.text = f"ATMs near {location}:\n\n• SBI ATM - 0.2 km\n• HDFC ATM - 0.5 km\n• ICICI ATM - 0.8 km\n• Axis Bank ATM - 1.2 km"
        else:
            self.atm_result.text = "Please enter a location"
    
    def show_credit_info(self, instance):
        info = """Credit Score Ranges:

300-579: Poor
580-669: Fair  
670-739: Good
740-799: Very Good
800-850: Excellent

Tips to Improve:
• Pay bills on time
• Keep credit utilization low
• Don't close old accounts
• Monitor your report regularly"""
        
        self.credit_result.text = info
    
    def switch_screen(self, screen_name):
        self.screen_manager.current = screen_name
    
    def toggle_theme(self):
        self.theme_cls.theme_style = "Light" if self.theme_cls.theme_style == "Dark" else "Dark"

if __name__ == "__main__":
    FinancialCalculatorApp().run()