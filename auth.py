"""
Authentication module for Financial Calculator App
Handles user login, session management, and security
"""

import hashlib
import json
import os
from datetime import datetime, timedelta

class AuthManager:
    """Handles authentication and user management"""
    
    def __init__(self):
        self.users_file = "users.json"
        self.sessions_file = "sessions.json"
        self.default_users = {
            "admin": {
                "password": self.hash_password("123"),
                "role": "admin",
                "created": datetime.now().isoformat(),
                "last_login": None
            }
        }
        self.init_users()
    
    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def init_users(self):
        """Initialize users file if it doesn't exist"""
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w') as f:
                json.dump(self.default_users, f, indent=2)
    
    def load_users(self):
        """Load users from file"""
        try:
            with open(self.users_file, 'r') as f:
                return json.load(f)
        except:
            return self.default_users
    
    def save_users(self, users):
        """Save users to file"""
        try:
            with open(self.users_file, 'w') as f:
                json.dump(users, f, indent=2)
            return True
        except:
            return False
    
    def authenticate(self, username, password):
        """Authenticate user credentials"""
        users = self.load_users()
        
        if username in users:
            stored_password = users[username]["password"]
            if stored_password == self.hash_password(password):
                # Update last login
                users[username]["last_login"] = datetime.now().isoformat()
                self.save_users(users)
                return True
        
        return False
    
    def create_user(self, username, password, role="user"):
        """Create new user account"""
        users = self.load_users()
        
        if username in users:
            return False, "User already exists"
        
        users[username] = {
            "password": self.hash_password(password),
            "role": role,
            "created": datetime.now().isoformat(),
            "last_login": None
        }
        
        if self.save_users(users):
            return True, "User created successfully"
        else:
            return False, "Failed to create user"
    
    def change_password(self, username, old_password, new_password):
        """Change user password"""
        users = self.load_users()
        
        if username not in users:
            return False, "User not found"
        
        if users[username]["password"] != self.hash_password(old_password):
            return False, "Invalid current password"
        
        users[username]["password"] = self.hash_password(new_password)
        
        if self.save_users(users):
            return True, "Password changed successfully"
        else:
            return False, "Failed to change password"
    
    def get_user_info(self, username):
        """Get user information"""
        users = self.load_users()
        
        if username in users:
            user_info = users[username].copy()
            del user_info["password"]  # Don't return password
            return user_info
        
        return None
    
    def is_admin(self, username):
        """Check if user is admin"""
        user_info = self.get_user_info(username)
        return user_info and user_info.get("role") == "admin"

class SessionManager:
    """Manages user sessions"""
    
    def __init__(self):
        self.sessions = {}
        self.session_timeout = timedelta(hours=24)  # 24 hour session
    
    def create_session(self, username):
        """Create new session for user"""
        session_id = hashlib.md5(f"{username}{datetime.now()}".encode()).hexdigest()
        
        self.sessions[session_id] = {
            "username": username,
            "created": datetime.now(),
            "last_activity": datetime.now()
        }
        
        return session_id
    
    def validate_session(self, session_id):
        """Validate if session is still active"""
        if session_id not in self.sessions:
            return False
        
        session = self.sessions[session_id]
        
        # Check if session has expired
        if datetime.now() - session["last_activity"] > self.session_timeout:
            del self.sessions[session_id]
            return False
        
        # Update last activity
        session["last_activity"] = datetime.now()
        return True
    
    def get_session_user(self, session_id):
        """Get username from session"""
        if self.validate_session(session_id):
            return self.sessions[session_id]["username"]
        return None
    
    def destroy_session(self, session_id):
        """Destroy user session"""
        if session_id in self.sessions:
            del self.sessions[session_id]
            return True
        return False
    
    def cleanup_expired_sessions(self):
        """Remove expired sessions"""
        current_time = datetime.now()
        expired_sessions = []
        
        for session_id, session in self.sessions.items():
            if current_time - session["last_activity"] > self.session_timeout:
                expired_sessions.append(session_id)
        
        for session_id in expired_sessions:
            del self.sessions[session_id]
        
        return len(expired_sessions)

class SecurityUtils:
    """Security utility functions"""
    
    @staticmethod
    def validate_password_strength(password):
        """Validate password strength"""
        if len(password) < 6:
            return False, "Password must be at least 6 characters long"
        
        if not any(c.isdigit() for c in password):
            return False, "Password must contain at least one digit"
        
        if not any(c.isalpha() for c in password):
            return False, "Password must contain at least one letter"
        
        return True, "Password is strong"
    
    @staticmethod
    def sanitize_input(input_string):
        """Sanitize user input to prevent injection attacks"""
        if not isinstance(input_string, str):
            return str(input_string)
        
        # Remove potentially dangerous characters
        dangerous_chars = ['<', '>', '"', "'", '&', ';', '(', ')', '|', '`']
        sanitized = input_string
        
        for char in dangerous_chars:
            sanitized = sanitized.replace(char, '')
        
        return sanitized.strip()
    
    @staticmethod
    def log_security_event(event_type, username, details=""):
        """Log security events"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "event_type": event_type,
            "username": username,
            "details": details
        }
        
        try:
            # Append to security log file
            with open("security.log", "a") as f:
                f.write(json.dumps(log_entry) + "\n")
        except:
            pass  # Fail silently if logging fails

# Global instances
auth_manager = AuthManager()
session_manager = SessionManager()

# Demo function to test authentication
def demo_auth():
    """Demo authentication functionality"""
    print("=== Authentication Demo ===")
    
    # Test login
    print("Testing login with admin/123:")
    result = auth_manager.authenticate("admin", "123")
    print(f"Login result: {result}")
    
    # Test wrong password
    print("\\nTesting login with admin/wrong:")
    result = auth_manager.authenticate("admin", "wrong")
    print(f"Login result: {result}")
    
    # Test user creation
    print("\\nCreating new user 'testuser':")
    result, message = auth_manager.create_user("testuser", "password123")
    print(f"Create user result: {result}, Message: {message}")
    
    # Test session management
    print("\\nTesting session management:")
    session_id = session_manager.create_session("admin")
    print(f"Created session: {session_id}")
    
    is_valid = session_manager.validate_session(session_id)
    print(f"Session valid: {is_valid}")
    
    username = session_manager.get_session_user(session_id)
    print(f"Session user: {username}")

if __name__ == "__main__":
    demo_auth()