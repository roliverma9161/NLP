import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return "Weak: Include at least one uppercase letter."
    if not re.search(r"[0-9]", password):
        return "Weak: Include at least one number."
    if not re.search(r"[@$!%*?&]", password):
        return "Medium: Consider adding a special character (@, $, !, etc.)."
    
    return "Strong password!"

print(check_password_strength("Python2026!"))