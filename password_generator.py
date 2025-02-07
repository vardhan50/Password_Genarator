import random

def generate_password(x):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()?"
    password = ""
    
    for _ in range(length):
        password += random.choice(characters)  # Randomly pick a character
    
    return password

# Example usage
length=int(input("Enter the password length:"))
print("Generated Password:", generate_password(length))
