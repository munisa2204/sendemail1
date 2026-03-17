from random import randint

def generate_otp():
    return randint(111111, 999999)

print(generate_otp())