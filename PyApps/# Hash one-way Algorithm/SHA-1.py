import math

# Define the SHA-1 helper functions
def left_rotate(x, amount):
    return ((x << amount) & 0xffffffff) | (x >> (32 - amount))

def pad_message(message):
    # Append the bit '1' to the message
    padded_message = message + b'\x80'

    # Pad the message until its length modulo 512 is 448
    padded_message += b'\x00' * ((56 - (len(message) + 1) % 64) % 64)

    # Append the length of the original message (in bits) as a 64-bit big-endian integer
    padded_message += int.to_bytes(len(message) * 8, 8, byteorder='big')

    return padded_message

# Define the SHA-1 hash function
def sha1(message):
    # Initialize the hash values
    h0, h1, h2, h3, h4 = 0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0

    # Pad the message
    padded_message = pad_message(message)

    # Process the message in 512-bit chunks
    for i in range(0, len(padded_message), 64):
        chunk = padded_message[i:i+64]

        # Initialize the round constants
        k = [0x5a827999, 0x6ed9eba1, 0x8f1bbcdc, 0xca62c1d6]

        # Initialize the message schedule
        w = [0] * 80
        for j in range(16):
            w[j] = int.from_bytes(chunk[j*4:j*4+4], byteorder='big')
        for j in range(16, 80):
            w[j] = left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)

        # Initialize the hash values for this chunk
        a, b, c, d, e = h0, h1, h2, h3, h4

        # Perform the main hash computation
        for j in range(80):
            if j < 20:
                f = lambda x, y, z: (x & y) | (~x & z)
                k_ = k[0]
            elif j < 40:
                f = lambda x, y, z: x ^ y ^ z
                k_ = k[1]
            elif j < 60:
                f = lambda x, y, z: (x & y) | (x & z) | (y & z)
                k_ = k[2]
            else:
                f = lambda x, y, z: x ^ y ^ z
                k_ = k[3]

            temp = (left_rotate(a, 5) + f(b, c, d) + e + k_ + w[j]) & 0xffffffff
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        # Update the hash values for this chunk
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

    # Concatenate the hash values and return the result as a 40-character hexadecimal string
    return '{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4)
    
# ======================================
message = b'This is a test message'
hash = sha1(message)
print(hash)  # Output: '0e5c4ea7a065f7a272a41e6fb2b2f3f1b6c9c98e'