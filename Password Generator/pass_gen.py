import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        print("Error: No character types selected.")
        return ""

    # Ensure at least one character type is included in the password
    password = [
        random.choice(string.ascii_uppercase) if use_upper else '',
        random.choice(string.ascii_lowercase) if use_lower else '',
        random.choice(string.digits) if use_digits else '',
        random.choice(string.punctuation) if use_special else ''
    ]
    password = [ch for ch in password if ch]  # Filter out empty strings

    # Fill the rest of the password length
    password += [random.choice(characters) for _ in range(length - len(password))]

    # Shuffle to avoid predictable characters at start
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Strong Password Generator")

    length = int(input("Enter password length (minimum 4): "))
    if length < 4:
        print("Minimum password length is 4.")
        return

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_lower, use_digits, use_special)

    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()

