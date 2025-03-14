import re

def check_password_strength(password):
    strength_score = 0
    feedback = []
    
    # Check length
    if len(password) >= 12:
        strength_score += 2
    elif len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    # Check for digits
    if re.search(r'\d', password):
        strength_score += 1
    else:
        feedback.append("Include at least one digit.")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        feedback.append("Include at least one special character.")
    
    # Check for common passwords
    common_passwords = ["password", "123456", "qwerty", "letmein", "123456789", "password1"]
    if password.lower() in common_passwords:
        feedback.append("Avoid using common passwords.")
    
    # Strength feedback
    if strength_score >= 5:
        return "Strong Password! ✅"
    elif strength_score >= 3:
        return "Moderate Password. Consider improving it. ⚠️\n" + "\n".join(feedback)
    else:
        return "Weak Password! ❌\n" + "\n".join(feedback)

# Example Usage
password = input("Enter a password to check its strength: ")
print(check_password_strength(password))
