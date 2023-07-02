"""
on-way
"""
import struct

def hash_4bit(message):
    """
    A hash function that generates a 4-bit hash value from the input message.
    """
    hash_value = hash(message) & 0b1111
    return hash_value

def hash_8bit(message):
    """
    A hash function that generates an 8-bit hash value from the input message.
    """
    hash_value = hash(message) & 0xFF
    return hash_value

def hash_16bit(message):
    """
    A hash function that generates a 16-bit hash value from the input message.
    """
    hash_value = hash(message) & 0xFFFF
    return hash_value

def hash_32bit(message):
    """
    A hash function that generates a 32-bit hash value from the input message.
    """
    hash_value = hash(message) & 0xFFFFFFFF
    return hash_value

def hash_64bit(message):
    """
    A hash function that generates a 64-bit hash value from the input message.
    """
    hash_value = hash(message) & 0xFFFFFFFFFFFFFFFF
    return hash_value

def hash_128bit(message):
    """
    A hash function that generates a 128-bit hash value from the input message.
    """
    hash_value = hash(message)
    hash_bytes = struct.pack('<QQ', hash_value & 0xFFFFFFFFFFFFFFFF, (hash_value >> 64) & 0xFFFFFFFFFFFFFFFF)
    hash_int = int.from_bytes(hash_bytes, byteorder='big', signed=False)
    return hash_int

def hash_256bit(message):
    """
    A hash function that generates a 256-bit hash value from the input message.
    """
    hash_value = hash(message)
    hash_bytes = struct.pack('<QQQQ', hash_value & 0xFFFFFFFFFFFFFFFF, (hash_value >> 64) & 0xFFFFFFFFFFFFFFFF, (hash_value >> 128) & 0xFFFFFFFFFFFFFFFF, (hash_value >> 192) & 0xFFFFFFFFFFFFFFFF)
    hash_int = int.from_bytes(hash_bytes, byteorder='big', signed=False)
    return hash_int

def hash_512bit(message):
    """
    A hash function that generates a 512-bit hash value from the input message.
    """
    hash_value = hash(message)
    hash_bytes = struct.pack('<QQQQQQQQ', hash_value & 0xFFFFFFFFFFFFFFFF, (hash_value >> 64) & 0xFFFFFFFFFFFFFFFF, (hash_value >> 128) & 0xFFFFFFFFFFFFFFFF, (hash_value >> 192) & 0xFFFFFFFFFFFFFFFF, (hash_value >> 256) & 0xFFFFFFFFFFFFFFFF, (hash_value >> 320) & 0xFFFFFFFFFFFFFFFF, (hash_value >> 384) & 0xFFFFFFFFFFFFFFFF, (hash_value >> 448) & 0xFFFFFFFFFFFFFFFF)
    hash_int = int.from_bytes(hash_bytes, byteorder='big', signed=False)
    return hash_int

# Example usage
message = "Hello, world!"
hash_4 = hash_4bit(message)
hash_8 = hash_8bit(message)
hash_16 = hash_16bit(message)
hash_32 = hash_32bit(message)
hash_64 = hash_64bit(message)
hash_128 = hash_128bit(message)
hash_256 = hash_256bit(message)
hash_512 = hash_512bit(message)
print(f"The 4-bit hash value of '{message}' is: {bin(hash_4)[2:].zfill(4)}")
print(f"The 8-bit hash value of '{message}' is: {hex(hash_8)[2:].zfill(2)}")
print(f"The 16-bit hash value of '{message}' is: {hex(hash_16)[2:].zfill(4)}")
print(f"The 32-bit hash value of '{message}' is: {hex(hash_32)[2:].zfill(8)}")
print(f"The 64-bit hash value of '{message}' is: {hex(hash_64)[2:].zfill(16)}")
print(f"The 128-bit hash value of '{message}' is: {hex(hash_128)[2:].zfill(32)}")
print(f"The 256-bit hash value of '{message}' is: {hex(hash_256)[2:].zfill(64)}")
print(f"The 512-bit hash value of '{message}' is: {hex(hash_512)[2:].zfill(128)}")