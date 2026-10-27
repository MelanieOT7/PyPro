
def analyze_password(password: str) -> str:

    if not password:
        return "Weak"
    
    if len(password) < 8 or password.isalpha() or password.isdigit():
        return "Weak"
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*" for char in password)
    
    if has_upper and has_lower and has_number and has_special:
        return "Strong"
    
    return "Medium"