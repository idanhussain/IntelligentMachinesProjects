## Decryptor
import bcrypt


# Function to hash a password
def hash_password(password):
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password


# Function to check a password
def check_password(hashed_password, user_password):
    # Check if the provided password matches the hashed password
    return bcrypt.checkpw(user_password.encode("utf-8"), hashed_password)


# Example usage
signupPass = input("Signup Password: ")

# Hash the password
hashed = hash_password(signupPass)
print(f"Hashed password: {hashed}")

loginPass = input("Login password: ")

# Verify the password
if check_password(hashed, loginPass):
    print("Password is correct!")
else:
    print("Password is incorrect!")
