import random
import string

def generate_password(length):
    """Generate a random password with the specified length"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    length = int(input("Enter the length of the password you'd like to generate: "))
    if length <= 0:
        print("Length must be greater than zero. Try again.\n")
    else:
        password = generate_password(length)
        print(f"Your random password is: {password}\n")
        break
