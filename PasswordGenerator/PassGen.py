import random

def generate_password(password_length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    generated_password = "".join(random.choice(characters) for _ in range(password_length))
    return generated_password
