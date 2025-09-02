from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.metrics import dp
import math
import requests
from datetime import datetime, date
import json
import webbrowser


class FinancialCalculatorApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.is_logged_in = False
        self.dialog = None
        
    def build(self):
        self.screen_manager = MDScreenManager()
        
        # Create screens
        self.create_login_screen()
        self.create_home_screen()
        self.create_emi_screen()
        self.create_rd_screen()
        self.create_fd_screen()
        self.create_loan_screen()

        self.create_gst_screen()
        self.create_comparison_screen()
        self.create_currency_screen()
        self.create_bank_holiday_screen()
        self.create_atm_finder_screen()
        self.create_credit_score_screen()
        
        return self.screen_manager
    
    def create_login_screen(self):
        screen = MDScreen(name="login")
        layout = MDBoxLayout(orientation="vertical", spacing="30dp", padding="40dp")
        
        # Theme toggle button at top
        theme_btn = MDIconButton(
            icon="theme-light-dark",
            theme_icon_color="Primary",
            pos_hint={"center_x": 0.5},
            on_release=lambda x: self.toggle_theme()
        )
        layout.add_widget(theme_btn)
        
        # App title
        title = MDLabel(
            text="Financial Calculator",
            theme_text_color="Primary",
            font_style="H4",
            halign="center",
            size_hint_y=None,
            height="80dp"
        )
        layout.add_widget(title)
        
        # Login card
        login_card = MDCard(
            size_hint_y=None,
            height="300dp",
            elevation=5,
            padding="30dp",
            spacing="20dp"
        )
        
        card_layout = MDBoxLayout(orientation="vertical", spacing="20dp")
        
        login_title = MDLabel(
            text="Login",
            theme_text_color="Primary",
            font_style="H5",
            halign="center",
            size_hint_y=None,
            height="40dp"
        )
        card_layout.add_widget(login_title)
        
        self.username_field = MDTextField(
            hint_text="Username",
            icon_right="account",
            size_hint_y=None,
            height="50dp"
        )
        card_layout.add_widget(self.username_field)
        
        self.password_field = MDTextField(
            hint_text="Password",
            password=True,
            icon_right="eye-off",
            size_hint_y=None,
            height="50dp"
        )
        card_layout.add_widget(self.password_field)
        
        login_btn = MDRaisedButton(
            text="LOGIN",
            size_hint_y=None,
            height="50dp",
            on_release=self.login
        )
        card_layout.add_widget(login_btn)
        
        login_card.add_widget(card_layout)
        layout.add_widget(login_card)
        
        # Demo credentials info
        demo_info = MDLabel(
            text="Demo Credentials:\nUsername: admin\nPassword: 123",
            theme_text_color="Secondary",
            halign="center",
            size_hint_y=None,
            height="80dp"
        )
        layout.add_widget(demo_info)
        
        screen.add_widget(layout)
        self.screen_manager.add_widget(screen)
    
    def login(self, instance):
        username = self.username_field.text
        password = self.password_field.text
        
        if username == "admin" and password == "123":
            self.is_logged_in = True
            self.switch_screen("home")
            self.show_dialog("Login Successful", "Welcome to Financial Calculator!")
        else:
            self.show_dialog("Login Failed", "Invalid username or password")
    
    def show_dialog(self, title, text):
        if not self.dialog:
            self.dialog = MDDialog(
                title=title,
                text=text,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=self.close_dialog
                    )
                ]
            )
        else:
            self.dialog.title = title
            self.dialog.text = text
        self.dialog.open()
    
    def close_dialog(self, instance):
        self.dialog.dismiss()
    
    def create_home_screen(self):
        screen = MDScreen(name="home")
        
        layout = MDBoxLayout(orientation="vertical", spacing="20dp", padding="20dp")
        
        # Top bar with logout
        toolbar = MDTopAppBar(
            title="Financial Calculator",
            right_action_items=[
                ["theme-light-dark", lambda x: self.toggle_theme()],
                ["logout", lambda x: self.logout()]
            ],
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
            ("Loan Calculator", "cash", "loan"),

            ("GST Calculator", "percent", "gst"),
            ("Comparison Tool", "compare", "comparison"),
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
    
    def logout(self):
        self.is_logged_in = False
        self.username_field.text = ""
        self.password_field.text = ""
        self.switch_screen("login")
    
    def create_feature_card(self, title, icon, screen_name):
        card = MDCard(
            size_hint_y=None,
            height="80dp",
            elevation=3,
            padding="10dp",
            on_release=lambda x: self.switch_screen(screen_name) if self.is_logged_in else self.switch_screen("login")
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
        
        toolbar = MDTopAppBar(
            title="EMI Calculator",
            left_action_items=[["arrow-left", lambda x: self.switch_screen("home")]],
            elevation=2
        )
        layout.add_widget(toolbar)
        
        self.emi_principal = MDTextField(hint_text="Principal Amount (₹)", input_filter="float")
        self.emi_rate = MDTextField(hint_text="Interest Rate (%)", input_filter="float")
        self.emi_tenure = MDTextField(hint_text="Tenure (months)", input_filter="int")
        
        layout.add_widget(self.emi_principal)
        layout.add_widget(self.emi_rate)
        layout.add_widget(self.emi_tenure)
        
        calc_btn = MDRaisedButton(text="Calculate EMI", on_release=self.calculate_emi)
        layout.add_widget(calc_btn)
        
        self.emi_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="150dp")
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
        
        self.rd_monthly = MDTextField(hint_text="Monthly Deposit (₹)", input_filter="float")
        self.rd_rate = MDTextField(hint_text="Interest Rate (%)", input_filter="float")
        self.rd_tenure = MDTextField(hint_text="Tenure (months)", input_filter="int")
        
        layout.add_widget(self.rd_monthly)
        layout.add_widget(self.rd_rate)
        layout.add_widget(self.rd_tenure)
        
        calc_btn = MDRaisedButton(text="Calculate RD", on_release=self.calculate_rd)
        layout.add_widget(calc_btn)
        
        self.rd_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="150dp")
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
        
        self.fd_principal = MDTextField(hint_text="Principal Amount (₹)", input_filter="float")
        self.fd_rate = MDTextField(hint_text="Interest Rate (%)", input_filter="float")
        self.fd_tenure = MDTextField(hint_text="Tenure (years)", input_filter="float")
        
        layout.add_widget(self.fd_principal)
        layout.add_widget(self.fd_rate)
        layout.add_widget(self.fd_tenure)
        
        calc_btn = MDRaisedButton(text="Calculate FD", on_release=self.calculate_fd)
        layout.add_widget(calc_btn)
        
        self.fd_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="150dp")
        layout.add_widget(self.fd_result)
        
        screen.add_widget(layout)
        self.screen_manager.add_widget(screen)
    
    def create_loan_screen(self):
        screen = MDScreen(name="loan")
        layout = MDBoxLayout(orientation="vertical", spacing="20dp", padding="20dp")
        
        toolbar = MDTopAppBar(
            title="Loan Calculator",
            left_action_items=[["arrow-left", lambda x: self.switch_screen("home")]],
            elevation=2
        )
        layout.add_widget(toolbar)
        
        self.loan_amount = MDTextField(hint_text="Loan Amount (₹)", input_filter="float")
        self.loan_rate = MDTextField(hint_text="Interest Rate (%)", input_filter="float")
        self.loan_tenure = MDTextField(hint_text="Tenure (years)", input_filter="float")
        
        layout.add_widget(self.loan_amount)
        layout.add_widget(self.loan_rate)
        layout.add_widget(self.loan_tenure)
        
        calc_btn = MDRaisedButton(text="Calculate Loan", on_release=self.calculate_loan)
        layout.add_widget(calc_btn)
        
        self.loan_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="200dp")
        layout.add_widget(self.loan_result)
        
        screen.add_widget(layout)
        self.screen_manager.add_widget(screen)
    


    def create_gst_screen(self):
        screen = MDScreen(name="gst")
        layout = MDBoxLayout(orientation="vertical", spacing="20dp", padding="20dp")
        
        toolbar = MDTopAppBar(
            title="GST Calculator",
            left_action_items=[["arrow-left", lambda x: self.switch_screen("home")]],
            elevation=2
        )
        layout.add_widget(toolbar)
        
        self.gst_amount = MDTextField(hint_text="Amount (₹)", input_filter="float")
        self.gst_rate = MDTextField(hint_text="GST Rate (%)", input_filter="float")
        
        layout.add_widget(self.gst_amount)
        layout.add_widget(self.gst_rate)
        
        # GST calculation buttons
        btn_layout = MDBoxLayout(orientation="horizontal", spacing="10dp", size_hint_y=None, height="50dp")
        
        add_gst_btn = MDRaisedButton(text="Add GST", on_release=self.add_gst, size_hint_x=0.5)
        remove_gst_btn = MDRaisedButton(text="Remove GST", on_release=self.remove_gst, size_hint_x=0.5)
        
        btn_layout.add_widget(add_gst_btn)
        btn_layout.add_widget(remove_gst_btn)
        layout.add_widget(btn_layout)
        
        self.gst_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="200dp")
        layout.add_widget(self.gst_result)
        
        screen.add_widget(layout)
        self.screen_manager.add_widget(screen)
    
    def create_comparison_screen(self):
        screen = MDScreen(name="comparison")
        layout = MDBoxLayout(orientation="vertical", spacing="20dp", padding="20dp")
        
        toolbar = MDTopAppBar(
            title="Investment Comparison",
            left_action_items=[["arrow-left", lambda x: self.switch_screen("home")]],
            elevation=2
        )
        layout.add_widget(toolbar)
        
        self.comp_amount = MDTextField(hint_text="Investment Amount (₹)", input_filter="float")
        self.comp_tenure = MDTextField(hint_text="Tenure (years)", input_filter="float")
        
        layout.add_widget(self.comp_amount)
        layout.add_widget(self.comp_tenure)
        
        calc_btn = MDRaisedButton(text="Compare Investments", on_release=self.compare_investments)
        layout.add_widget(calc_btn)
        
        self.comp_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="250dp")
        layout.add_widget(self.comp_result)
        
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
        self.curr_from = MDTextField(hint_text="From Currency (USD, INR, EUR, GBP)")
        self.curr_to = MDTextField(hint_text="To Currency (USD, INR, EUR, GBP)")
        
        layout.add_widget(self.curr_amount)
        layout.add_widget(self.curr_from)
        layout.add_widget(self.curr_to)
        
        convert_btn = MDRaisedButton(text="Convert Currency", on_release=self.convert_currency)
        layout.add_widget(convert_btn)
        
        self.curr_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="150dp")
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
        
        self.holiday_year = MDTextField(hint_text="Enter Year (e.g., 2024)", input_filter="int", text="2024")
        layout.add_widget(self.holiday_year)
        
        check_btn = MDRaisedButton(text="Check Bank Holidays", on_release=self.check_bank_holidays)
        layout.add_widget(check_btn)
        
        self.holiday_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="400dp")
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
        
        btn_layout = MDBoxLayout(orientation="horizontal", spacing="10dp", size_hint_y=None, height="50dp")
        
        find_btn = MDRaisedButton(text="Find ATMs", on_release=self.find_atms, size_hint_x=0.5)
        map_btn = MDRaisedButton(text="Open Map", on_release=self.open_map, size_hint_x=0.5)
        
        btn_layout.add_widget(find_btn)
        btn_layout.add_widget(map_btn)
        layout.add_widget(btn_layout)
        
        self.atm_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="300dp")
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
        
        self.credit_result = MDLabel(text="", theme_text_color="Primary", size_hint_y=None, height="400dp")
        layout.add_widget(self.credit_result)
        
        screen.add_widget(layout)
        self.screen_manager.add_widget(screen)
    
    # Calculation methods
    def calculate_emi(self, instance):
        try:
            P = float(self.emi_principal.text)
            r = float(self.emi_rate.text) / 100 / 12
            n = int(self.emi_tenure.text)
            
            if r == 0:
                emi = P / n
            else:
                emi = P * r * (1 + r)**n / ((1 + r)**n - 1)
            
            total_amount = emi * n
            interest = total_amount - P
            
            self.emi_result.text = f"EMI Calculation Results:\n\n1. Principal Amount: ₹{P:.2f}\n2. Interest Rate: {float(self.emi_rate.text):.1f}% per annum\n3. Tenure: {int(self.emi_tenure.text)} months\n4. Monthly EMI: ₹{emi:.2f}\n5. Total Amount Payable: ₹{total_amount:.2f}\n6. Total Interest: ₹{interest:.2f}\n7. Interest Percentage: {(interest/P)*100:.1f}%"
        except:
            self.emi_result.text = "Please enter valid values"
    
    def calculate_rd(self, instance):
        try:
            P = float(self.rd_monthly.text)
            r = float(self.rd_rate.text) / 100 / 12
            n = int(self.rd_tenure.text)
            
            if r == 0:
                maturity = P * n
            else:
                maturity = P * (((1 + r)**n - 1) / r) * (1 + r)
            
            total_invested = P * n
            interest = maturity - total_invested
            
            self.rd_result.text = f"RD Calculation Results:\n\n1. Monthly Deposit: ₹{P:.2f}\n2. Interest Rate: {float(self.rd_rate.text):.1f}% per annum\n3. Tenure: {int(self.rd_tenure.text)} months\n4. Total Invested: ₹{total_invested:.2f}\n5. Interest Earned: ₹{interest:.2f}\n6. Maturity Amount: ₹{maturity:.2f}\n7. Return Rate: {(interest/total_invested)*100:.1f}%"
        except:
            self.rd_result.text = "Please enter valid values"
    
    def calculate_fd(self, instance):
        try:
            P = float(self.fd_principal.text)
            r = float(self.fd_rate.text) / 100
            t = float(self.fd_tenure.text)
            
            maturity = P * (1 + r)**t
            interest = maturity - P
            
            self.fd_result.text = f"FD Calculation Results:\n\n1. Principal Amount: ₹{P:.2f}\n2. Interest Rate: {float(self.fd_rate.text):.1f}% per annum\n3. Tenure: {t} years\n4. Interest Earned: ₹{interest:.2f}\n5. Maturity Amount: ₹{maturity:.2f}\n6. Total Return: {(interest/P)*100:.1f}%"
        except:
            self.fd_result.text = "Please enter valid values"
    
    def calculate_loan(self, instance):
        try:
            P = float(self.loan_amount.text)
            r = float(self.loan_rate.text) / 100 / 12
            n = float(self.loan_tenure.text) * 12
            
            if r == 0:
                emi = P / n
            else:
                emi = P * r * (1 + r)**n / ((1 + r)**n - 1)
            
            total_amount = emi * n
            interest = total_amount - P
            
            self.loan_result.text = f"Loan Calculation Results:\n\n1. Loan Amount: ₹{P:.2f}\n2. Interest Rate: {float(self.loan_rate.text):.1f}% per annum\n3. Tenure: {float(self.loan_tenure.text):.0f} years\n4. Monthly EMI: ₹{emi:.2f}\n5. Total Interest: ₹{interest:.2f}\n6. Total Amount Payable: ₹{total_amount:.2f}\n7. Interest to Principal Ratio: {(interest/P)*100:.1f}%"
        except:
            self.loan_result.text = "Please enter valid values"
    
    def add_gst(self, instance):
        try:
            amount = float(self.gst_amount.text)
            gst_rate = float(self.gst_rate.text)
            
            gst_amount = amount * gst_rate / 100
            total_amount = amount + gst_amount
            
            self.gst_result.text = f"GST Calculation (Adding GST):\n\n1. Base Amount: ₹{amount:.2f}\n2. GST Rate: {gst_rate}%\n3. CGST ({gst_rate/2}%): ₹{gst_amount/2:.2f}\n4. SGST ({gst_rate/2}%): ₹{gst_amount/2:.2f}\n5. Total GST Amount: ₹{gst_amount:.2f}\n6. Final Amount (Inc. GST): ₹{total_amount:.2f}"
        except:
            self.gst_result.text = "Please enter valid values"
    
    def remove_gst(self, instance):
        try:
            total_amount = float(self.gst_amount.text)
            gst_rate = float(self.gst_rate.text)
            
            base_amount = total_amount / (1 + gst_rate/100)
            gst_amount = total_amount - base_amount
            
            self.gst_result.text = f"GST Calculation (Removing GST):\n\n1. Total Amount (Inc. GST): ₹{total_amount:.2f}\n2. GST Rate: {gst_rate}%\n3. CGST ({gst_rate/2}%): ₹{gst_amount/2:.2f}\n4. SGST ({gst_rate/2}%): ₹{gst_amount/2:.2f}\n5. Total GST Amount: ₹{gst_amount:.2f}\n6. Base Amount (Exc. GST): ₹{base_amount:.2f}"
        except:
            self.gst_result.text = "Please enter valid values"
    
    def compare_investments(self, instance):
        try:
            amount = float(self.comp_amount.text)
            years = float(self.comp_tenure.text)
            
            # Different investment options
            fd_return = amount * (1 + 0.06)**years
            rd_months = years * 12
            rd_monthly = amount / rd_months
            rd_return = rd_monthly * (((1 + 0.065/12)**rd_months - 1) / (0.065/12)) * (1 + 0.065/12)
            sip_monthly = amount / rd_months
            sip_return = sip_monthly * (((1 + 0.12/12)**rd_months - 1) / (0.12/12))
            ppf_return = amount * (1 + 0.075)**years
            
            best_option = max([(fd_return, 'Fixed Deposit'), (rd_return, 'Recurring Deposit'), (sip_return, 'Mutual Fund SIP'), (ppf_return, 'PPF')], key=lambda x: x[0])[1]
            self.comp_result.text = f"Investment Comparison for ₹{amount:.0f} over {years} years:\n\n1. Fixed Deposit (6%): ₹{fd_return:.2f}\n2. Recurring Deposit (6.5%): ₹{rd_return:.2f}\n3. PPF (7.5%): ₹{ppf_return:.2f}\n4. Mutual Fund SIP (12%): ₹{sip_return:.2f}\n\n5. Best Option: {best_option}\n6. Highest Return: ₹{max(fd_return, rd_return, sip_return, ppf_return):.2f}"
        except:
            self.comp_result.text = "Please enter valid values"
    
    def convert_currency(self, instance):
        try:
            rates = {
                'USD': {'INR': 83.0, 'EUR': 0.85, 'GBP': 0.73, 'JPY': 110.0},
                'INR': {'USD': 0.012, 'EUR': 0.010, 'GBP': 0.009, 'JPY': 1.32},
                'EUR': {'USD': 1.18, 'INR': 98.0, 'GBP': 0.86, 'JPY': 129.0},
                'GBP': {'USD': 1.37, 'INR': 114.0, 'EUR': 1.16, 'JPY': 150.0}
            }
            
            amount = float(self.curr_amount.text)
            from_curr = self.curr_from.text.upper()
            to_curr = self.curr_to.text.upper()
            
            if from_curr == to_curr:
                converted = amount
            elif from_curr in rates and to_curr in rates[from_curr]:
                converted = amount * rates[from_curr][to_curr]
            else:
                self.curr_result.text = "Currency pair not supported\n\nSupported: USD, INR, EUR, GBP"
                return
            
            self.curr_result.text = f"Currency Conversion Results:\n\n1. From Currency: {from_curr}\n2. To Currency: {to_curr}\n3. Amount to Convert: {amount:.2f} {from_curr}\n4. Exchange Rate: 1 {from_curr} = {rates[from_curr][to_curr] if from_curr != to_curr else 1:.4f} {to_curr}\n5. Converted Amount: {converted:.2f} {to_curr}\n6. Note: Rates are indicative"
        except:
            self.curr_result.text = "Please enter valid values"
    
    def check_bank_holidays(self, instance):
        try:
            year = int(self.holiday_year.text) if self.holiday_year.text else 2024
        except:
            year = 2024
        
        holidays_data = {
            2024: [
                "Jan 26 - Republic Day",
                "Mar 8 - Holi",
                "Mar 29 - Good Friday", 
                "Apr 11 - Eid ul-Fitr",
                "May 1 - Labour Day",
                "Aug 15 - Independence Day",
                "Aug 19 - Raksha Bandhan",
                "Sep 7 - Janmashtami",
                "Oct 2 - Gandhi Jayanti",
                "Oct 31 - Diwali",
                "Nov 1 - Govardhan Puja",
                "Dec 25 - Christmas Day"
            ],
            2025: [
                "Jan 26 - Republic Day",
                "Feb 26 - Holi",
                "Apr 18 - Good Friday",
                "Mar 31 - Eid ul-Fitr",
                "May 1 - Labour Day",
                "Aug 15 - Independence Day",
                "Aug 9 - Raksha Bandhan",
                "Aug 26 - Janmashtami",
                "Oct 2 - Gandhi Jayanti",
                "Oct 20 - Diwali",
                "Oct 21 - Govardhan Puja",
                "Dec 25 - Christmas Day"
            ],
            2023: [
                "Jan 26 - Republic Day",
                "Mar 8 - Holi",
                "Apr 7 - Good Friday",
                "Apr 22 - Eid ul-Fitr",
                "May 1 - Labour Day",
                "Aug 15 - Independence Day",
                "Aug 31 - Raksha Bandhan",
                "Sep 7 - Janmashtami",
                "Oct 2 - Gandhi Jayanti",
                "Nov 12 - Diwali",
                "Nov 14 - Govardhan Puja",
                "Dec 25 - Christmas Day"
            ]
        }
        
        if year in holidays_data:
            holidays = holidays_data[year]
            ordered_holidays = "\n".join([f"{i+1}. {holiday}" for i, holiday in enumerate(holidays)])
            self.holiday_result.text = f"Bank Holidays {year}:\n\n{ordered_holidays}\n\nNote: Holidays may vary by state and bank. Please check with your local branch for confirmation."
        else:
            self.holiday_result.text = f"Holiday data for {year} not available.\n\nAvailable years:\n1. 2023\n2. 2024\n3. 2025\n\nNote: Please enter a supported year or contact your bank for specific year holiday information."
    
    def find_atms(self, instance):
        location = self.atm_location.text
        if location:
            atms = [
                "State Bank of India ATM - 0.2 km",
                "HDFC Bank ATM - 0.5 km", 
                "ICICI Bank ATM - 0.8 km",
                "Axis Bank ATM - 1.2 km",
                "Punjab National Bank ATM - 1.5 km",
                "Bank of Baroda ATM - 1.8 km"
            ]
            self.atm_result.text = f"ATMs near {location}:\n\n" + "\n".join([f"{i+1}. {atm}" for i, atm in enumerate(atms)]) + "\n\nClick 'Open Map' for directions"
        else:
            self.atm_result.text = "Please enter a location"
    
    def open_map(self, instance):
        location = self.atm_location.text
        if location:
            # Open Google Maps with ATM search
            map_url = f"https://www.google.com/maps/search/atm+near+{location.replace(' ', '+')}"
            webbrowser.open(map_url)
            self.show_dialog("Map Opened", f"Opening map to find ATMs near {location}")
        else:
            self.show_dialog("Location Required", "Please enter a location first")
    
    def show_credit_info(self, instance):
        info = """Credit Score Information:

Credit Score Ranges:
1. 300-579: Poor (High Risk)
2. 580-669: Fair (Moderate Risk)  
3. 670-739: Good (Low Risk)
4. 740-799: Very Good (Very Low Risk)
5. 800-850: Excellent (Minimal Risk)

Tips to Improve Credit Score:
1. Pay all bills on time (35% impact)
2. Keep credit utilization below 30% (30% impact)
3. Don't close old credit accounts (15% impact)
4. Monitor your credit report regularly
5. Limit new credit inquiries (10% impact)
6. Maintain a mix of credit types (10% impact)

Benefits of Good Credit Score:
1. Lower interest rates on loans
2. Higher credit limits
3. Better credit card offers
4. Easier loan approvals
5. Lower insurance premiums"""
        
        self.credit_result.text = info
    


    def switch_screen(self, screen_name):
        if screen_name != "login" and not self.is_logged_in:
            self.switch_screen("login")
            return
        self.screen_manager.current = screen_name
    
    def toggle_theme(self):
        self.theme_cls.theme_style = "Light" if self.theme_cls.theme_style == "Dark" else "Dark"

if __name__ == "__main__":
    FinancialCalculatorApp().run()