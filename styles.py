"""
Stylesheet and styling configurations for Financial Calculator App
"""

from kivymd.color_definitions import colors

class AppStyles:
    """App styling configurations"""
    
    # Color schemes
    DARK_THEME = {
        'primary': colors['Blue']['500'],
        'primary_dark': colors['Blue']['700'],
        'accent': colors['Amber']['500'],
        'background': colors['Grey']['900'],
        'surface': colors['Grey']['800'],
        'text_primary': colors['Grey']['100'],
        'text_secondary': colors['Grey']['400'],
        'success': colors['Green']['500'],
        'warning': colors['Orange']['500'],
        'error': colors['Red']['500']
    }
    
    LIGHT_THEME = {
        'primary': colors['Blue']['600'],
        'primary_dark': colors['Blue']['800'],
        'accent': colors['Amber']['600'],
        'background': colors['Grey']['50'],
        'surface': colors['Grey']['100'],
        'text_primary': colors['Grey']['900'],
        'text_secondary': colors['Grey']['600'],
        'success': colors['Green']['600'],
        'warning': colors['Orange']['600'],
        'error': colors['Red']['600']
    }
    
    # Typography
    FONT_SIZES = {
        'h1': '32sp',
        'h2': '28sp',
        'h3': '24sp',
        'h4': '20sp',
        'h5': '18sp',
        'h6': '16sp',
        'body1': '16sp',
        'body2': '14sp',
        'caption': '12sp'
    }
    
    # Spacing
    SPACING = {
        'xs': '4dp',
        'sm': '8dp',
        'md': '16dp',
        'lg': '24dp',
        'xl': '32dp',
        'xxl': '48dp'
    }
    
    # Component styles
    CARD_STYLE = {
        'elevation': 3,
        'radius': [8, 8, 8, 8],
        'padding': '16dp',
        'spacing': '12dp'
    }
    
    BUTTON_STYLE = {
        'height': '48dp',
        'radius': [8, 8, 8, 8],
        'elevation': 2
    }
    
    INPUT_STYLE = {
        'height': '56dp',
        'radius': [8, 8, 8, 8]
    }
    
    # Animation durations
    ANIMATION = {
        'fast': 0.2,
        'normal': 0.3,
        'slow': 0.5
    }

class CalculatorStyles:
    """Specific styles for calculator components"""
    
    RESULT_CARD = {
        'md_bg_color': (0.1, 0.1, 0.1, 0.1),
        'elevation': 2,
        'radius': [12, 12, 12, 12],
        'padding': '20dp'
    }
    
    INPUT_CARD = {
        'md_bg_color': (0.05, 0.05, 0.05, 0.05),
        'elevation': 1,
        'radius': [8, 8, 8, 8],
        'padding': '16dp'
    }
    
    FEATURE_CARD = {
        'elevation': 3,
        'radius': [12, 12, 12, 12],
        'padding': '16dp',
        'height': '80dp'
    }

class LoginStyles:
    """Login screen specific styles"""
    
    LOGIN_CARD = {
        'elevation': 8,
        'radius': [16, 16, 16, 16],
        'padding': '32dp',
        'md_bg_color': (0.05, 0.05, 0.05, 0.1)
    }
    
    LOGIN_BUTTON = {
        'height': '48dp',
        'radius': [24, 24, 24, 24],
        'elevation': 3
    }

# CSS-like styling for components
COMPONENT_STYLES = """
/* Card Components */
.calculator-card {
    elevation: 3;
    radius: 12dp;
    padding: 20dp;
    margin: 8dp;
    background-color: surface;
}

.feature-card {
    elevation: 2;
    radius: 8dp;
    padding: 16dp;
    height: 80dp;
    margin: 4dp;
}

.result-card {
    elevation: 1;
    radius: 8dp;
    padding: 16dp;
    background-color: primary;
    color: white;
}

/* Button Styles */
.primary-button {
    height: 48dp;
    radius: 24dp;
    elevation: 2;
    background-color: primary;
    color: white;
}

.secondary-button {
    height: 48dp;
    radius: 24dp;
    elevation: 1;
    background-color: surface;
    color: primary;
}

/* Input Styles */
.text-input {
    height: 56dp;
    radius: 8dp;
    padding: 16dp;
    margin: 8dp;
}

/* Layout Styles */
.main-layout {
    padding: 20dp;
    spacing: 16dp;
}

.card-layout {
    spacing: 12dp;
    padding: 16dp;
}

/* Typography */
.title-text {
    font-size: 24sp;
    font-weight: bold;
    color: primary;
}

.subtitle-text {
    font-size: 18sp;
    color: text-secondary;
}

.body-text {
    font-size: 16sp;
    color: text-primary;
}

.caption-text {
    font-size: 12sp;
    color: text-secondary;
}

/* Responsive Design */
@media (max-width: 600dp) {
    .main-layout {
        padding: 16dp;
    }
    
    .calculator-card {
        padding: 16dp;
        margin: 4dp;
    }
}

@media (min-width: 600dp) {
    .main-layout {
        padding: 24dp;
    }
    
    .calculator-card {
        padding: 24dp;
        margin: 8dp;
    }
}
"""

# Color palette for different calculation types
CALCULATION_COLORS = {
    'emi': colors['Blue']['500'],
    'rd': colors['Green']['500'],
    'fd': colors['Orange']['500'],
    'loan': colors['Red']['500'],
    'gst': colors['Purple']['500'],
    'currency': colors['Teal']['500'],
    'comparison': colors['Indigo']['500'],
    'credit': colors['Pink']['500']
}

# Icon mappings for different features
FEATURE_ICONS = {
    'emi': 'calculator',
    'rd': 'piggy-bank',
    'fd': 'bank',
    'loan': 'cash',
    'gst': 'percent',
    'currency': 'currency-usd',
    'comparison': 'compare',
    'holidays': 'calendar',
    'atm': 'map-marker',
    'credit': 'chart-line',
    'login': 'account',
    'logout': 'logout',
    'theme': 'theme-light-dark',
    'map': 'map',
    'calculate': 'calculator-variant'
}