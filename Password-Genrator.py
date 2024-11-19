import random
import string

def check_password_complexity(password):
    """Check if the password meets the complexity requirements."""
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if has_upper and has_lower and has_digit and has_special:
        return True
    return False

def generate_password():
    print("Password Generator")
    
    # Prompt user for password length
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
        if length < 4:
            print("Password length should be at least 4 for better security.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    # Define the character pools for password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password contains at least one of each type for better security
    all_characters = lowercase + uppercase + digits + special_characters
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Add random characters to reach the desired length
    if length > 4:
        password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to randomize its order
    random.shuffle(password)

    # Convert the list to a string
    password = ''.join(password)

    # Display the generated password and success message
    print("\nYour generated password is: ", password)
    print("Your password has been successfully generated!")

def main():
    print("Welcome to the Password Tool!")
    print("1. Generate a new password")
    print("2. Validate an existing password")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        generate_password()
    elif choice == "2":
        password = input("Enter the password to validate: ")
        if check_password_complexity(password):
            print("Your password is strong and meets the requirements!")
        else:
            print("Your password does NOT meet the complexity requirements.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the tool
main()
