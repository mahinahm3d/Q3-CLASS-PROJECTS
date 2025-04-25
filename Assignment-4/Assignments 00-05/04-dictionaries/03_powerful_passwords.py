import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    hashed_input = hash_password(password_to_check)
    return stored_logins.get(email) == hashed_input

if __name__ == "__main__":
    stored_logins = {
        "user@example.com": hash_password("mysecurepasswordis5674"),
        "khanasiya@example.com": hash_password("it'sokaynottobeokay22")
    }
    
    email = input("Enter email: ")
    password = input("Enter password: ")
    
    if login(email, password, stored_logins):
        print("Login successful! ✅")
    else:
        print("Login failed! ❌ Incorrect email or password.")