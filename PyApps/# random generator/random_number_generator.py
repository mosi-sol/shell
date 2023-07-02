import random

def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(bit_length):
    """Generate a random prime number with the specified bit length."""
    while True:
        n = random.getrandbits(bit_length)
        if is_prime(n):
            return n

def hex_to_binary(hex_str):
    """Convert a hexadecimal string to binary."""
    binary_str = bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)
    return binary_str

def hex_to_int(hex_str):
    """Convert a hexadecimal string to an integer."""
    int_value = int(hex_str, 16)
    return int_value

def caesar_hash(message, hash_key, prime):
    """Compute the Caesar cipher hash value of the message."""
    # Convert message to numerical value
    num_value = sum(ord(char) for char in message)

    # Apply Caesar cipher
    hash_code = (num_value + hash_key) % prime

    # Convert hash code to hexadecimal format
    hex_digits = []
    while hash_code > 0:
        hex_digit = hex(hash_code % 16)[2:]
        hex_digits.append(hex_digit)
        hash_code //= 16
    hex_value = ''.join(hex_digits[::-1]).zfill(4)

    return hex_value

# ========================================
# Random generator usage
def random_generator():
    message = "Willy Seen in tiny moon!"
    prime = generate_prime(16)
    hash_key = random.randint(1, prime-1)
    hex_value = caesar_hash(message, hash_key, prime)

    binary_value = hex_to_binary(hex_value)
    int_value = hex_to_int(hex_value)

    print("Prime: ", prime)
    print("Hash key: ", hash_key)
    print("Hex value: ", hex_value)
    print("Binary value: ", binary_value)
    print("Integer value: ", int_value)
    print("Final random number (dice 1 to 6): ", (int_value % 6)+1)

random_generator()