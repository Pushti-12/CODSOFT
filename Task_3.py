import random
import string

def password_generator():
    print("----- Password Generator -----")
    length = int(input("Enter the desired password length: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"\nYour Generated Password is: {password}")

password_generator()
