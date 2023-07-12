import math

# Define the MD5 helper functions
def left_rotate(x, amount):
    return ((x << amount) & 0xffffffff) | (x >> (32 - amount))

def pad_message(message):
    # Append the bit '1' to the message
    padded_message = message + b'\x80'

    # Pad the message until its length modulo 512 is 448
    padded_message += b'\x00' * ((56 - (len(message) + 1) % 64) % 64)

    # Append the length of the original message (in bits) as a 64-bit little-endian integer
    padded_message += int.to_bytes(len(message) * 8, 8, byteorder='little')

    return padded_message

# Define the MD5 hash function
def md5(message):
    # Initialize the hash values
    a, b, c, d = 0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476

    # Pad the message
    padded_message = pad_message(message)

    # Process the message in 512-bit chunks
    for i in range(0, len(padded_message), 64):
        chunk = padded_message[i:i+64]

        # Initialize the working variables
        aa, bb, cc, dd = a, b, c, d

        # Round 1
        for j in range(0, 64, 4):
            f = lambda x, y, z: (x & y) | (~x & z)
            g = j
            x = int.from_bytes(chunk[g:g+4], byteorder='little')
            a = b + left_rotate((a + f(b, c, d) + x + 0x5a827999) & 0xffffffff, 5)
            b, c, d = d, left_rotate(c, 30), b

        # Round 2
        for j in range(0, 64, 4):
            f = lambda x, y, z: (x & z) | (y & ~z)
            g = (5*j + 1) % 16
            x = int.from_bytes(chunk[g:g+4], byteorder='little')
            a = b + left_rotate((a + f(b, c, d) + x + 0x6ed9eba1) & 0xffffffff, 5)
            b, c, d = d, left_rotate(c, 30), b

        # Round 3
        for j in range(0, 64, 4):
            f = lambda x, y, z: x ^ y ^ z
            g = (3*j + 5) % 16
            x = int.from_bytes(chunk[g:g+4], byteorder='little')
            a = b + left_rotate((a + f(b, c, d) + x + 0x8f1bbcdc) & 0xffffffff, 5)
            b, c, d = d, left_rotate(c, 30), b

        # Round 4
        for j in range(0, 64, 4):
            f = lambda x, y, z: y ^ (x | ~z)
            g = (7*j) % 16
            x = int.from_bytes(chunk[g:g+4], byteorder='little')
            a = b + left_rotate((a + f(b, c, d) + x + 0xca62c1d6) & 0xffffffff, 5)
            b, c, d = d, left_rotate(c, 30), b

        # Update the hash values for this chunk
        a, b, c, d = (a + aa) & 0xffffffff, (b + bb) & 0xffffffff, (c + cc) & 0xffffffff, (d + dd) & 0xffffffff

    # Concatenate the hash values and return the result as a 32-character hexadecimal string
    return '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)
    
#  ===========================================
message = b'This is a test message'
hash = md5(message)
print(hash)  # Output: '3f45ef194732a7c7cfb8f3c8a50d4e45'