import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Combine character sets based on user specifications
    all_characters = ""
    if use_uppercase:
        all_characters += uppercase_letters
    if use_lowercase:
        all_characters += lowercase_letters
    if use_digits:
        all_characters += digits
    if use_special:
        all_characters += special_characters

    if not all_characters:
        raise ValueError("At least one character set must be selected")
    
    # Generate a password using the combined character set
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    try:
        # Get user specifications
        length = int(input("Enter the desired password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        num_passwords = int(input("How many passwords would you like to generate? "))
       

        # Generate and display the passwords
        for i in range(num_passwords):
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
            print(f"Generated password {i + 1}: {password}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
