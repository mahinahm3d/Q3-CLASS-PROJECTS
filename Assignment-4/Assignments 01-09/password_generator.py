import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

print("========== Password Generator ==========\n")
num_passwords = int(input("Number of Passwords? "))
password_length = int(input("Password length? "))

print("\nHere are your passwords:")
for i in range(num_passwords):
    password = generate_password(password_length)
    print(f"{i+1}. {password}")