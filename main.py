import re
import random
import string

def generate_suggestion():
    characters = (
        random.choice(string.ascii_uppercase) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.digits) +
        random.choice("!@#$%^&*(),.?\":{}|<>")
    )
    remaining_chars = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*(),.?\":{}|<>", k=4))
    return ''.join(random.sample(characters + remaining_chars, 8))

def validate_password(password):
    checks = {
        "At least 8 characters": len(password) >= 8,
        "At least one uppercase letter": bool(re.search(r'[A-Z]', password)),
        "At least one lowercase letter": bool(re.search(r'[a-z]', password)),
        "At least one digit": bool(re.search(r'\d', password)),
        "At least one special character": bool(re.search(r'[!@#$%^&*(),.?\":{}|<>]', password))
    }
    
    for requirement, passed in checks.items():
        print(f"{'✅' if passed else '❌'} {requirement}")
    
    return all(checks.values())

if input("Generate a strong password? (yes/no): ").strip().lower() == "yes":
    print("Suggested Password:", generate_suggestion())

while True:
    password = input("Enter password: ")
    
    if validate_password(password):
        print("✅ Password is valid.")
        break
    else:
        print("❌ Password is invalid. Please try again.")
        if input("Generate a strong password? (yes/no): ").strip().lower() == "yes":
            print("Suggested Password:", generate_suggestion())
