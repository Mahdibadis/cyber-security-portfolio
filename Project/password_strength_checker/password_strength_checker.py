import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak password ❌"
    elif score == 3 or score == 4:
        return "Medium password ⚠️"
    else:
        return "Strong password ✅"

if __name__ == "__main__":
    user_password = input("Enter a password to test: ")
    result = check_password_strength(user_password)
    print(result)

