"""
on-way
"""
import random

def hash_message(message):
    if not message.isdigit():
        raise ValueError("Input message must be a valid integer")
    n = int(message)
    a = n % 10
    b = n % 100 // 10
    c = n % 1000 // 100
    d = n // 1000
    phi = (a + 1) * (b + 1) * (c + 1) * (d + 1)  # compute Euler's totient function
    pi = 3.14159  # approximate value of pi
    hash_value = int((phi * pi) / 1.41421)  # square root of 2
    return hash_value

def hash_to_hex(hash_value):
    hex_string = hex(hash_value)[2:].zfill(8)
    return hex_string
    
# ==========================
# Example usage
message = str(random.randint(1000, 9999))  # generate a random 4-digit integer
hash_value = hash_message(message)
print(f"The hash value of '{message}' is: {hash_value}\n")
hex_string = hash_to_hex(hash_value)
print(f"The hex-hash value of '{message}' is: {hex_string}")