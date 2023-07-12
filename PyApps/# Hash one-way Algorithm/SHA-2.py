import math

# Define the SHA-256 helper functions
def right_rotate(x, amount):
    return (x >> amount) | (x << (32 - amount))

def sigma_0(x):
    return right_rotate(x, 7) ^ right_rotate(x, 18) ^ (x >> 3)

def sigma_1(x):
    return right_rotate(x, 17) ^ right_rotate(x, 19) ^ (x >> 10)

def ch(x, y, z):
    return (x & y) ^ (~x & z)

def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def pad_message(message):
    # Append the bit '1' to the message
    padded_message = message + b'\x80'

    # Pad the message until its length modulo 512 is 448
    padded_message += b'\x00' * ((56 - (len(message) + 1) % 64) % 64)

    # Append the length of the original message (in bits) as a 64-bit big-endian integer
    padded_message += int.to_bytes(len(message) * 8, 8, byteorder='big')

    return padded_message

# Define the SHA-256 hash function
def sha256(message):
    # Initialize the hash values
    h0, h1, h2, h3, h4, h5, h6, h7 = (
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    )

    # Initialize the round constants
    k = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
        0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
        0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
        0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
        0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
        0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
        0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
        0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
    ]

    # Pad the message
    padded_message = pad_message(message)

    # Process the message in 512-bit chunks
    for i in range(0, len(padded_message), 64):
        chunk = padded_message[i:i+64]

        # Initialize the message schedule
        w = [0] * 64
        for j in range(16):
            w[j] = int.from_bytes(chunk[j*4:j*4+4], byteorder='big')
        for j in range(16, 64):
            s0 = sigma_0(w[j-15])
            s1 = sigma_1(w[j-2])
            w[j] = (w[j-16] + s0 + w[j-7] + s1) & 0xffffffff

        # Initialize the hash values for this chunk
        a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7

        # Perform the main hash computation
        for j in range(64):
            S1 = right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25)
            ch_ = ch(e, f, g)
            temp1 = (h + S1 + ch_ + k[j] + w[j]) & 0xffffffff
            S0 = right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22)
            maj_ = maj(a, b, c)
            temp2 = (S0 + maj_) & 0xffffffff

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xffffffff
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xffffffff

        # Update the hash values for this chunk
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff
        h5 = (h5 + f) & 0xffffffff
        h6 = (h6 + g) & 0xffffffff
        h7 = (h7 + h) & 0xffffffff

    # Concatenate the hash values and return the result as a 64-character hexadecimal string
    return '{:08x}{:08x}{:08x}{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4, h5, h6, h7)
    
# ======================================
message = b'This is a test message'
hash = sha256(message)
print(hash)  # Output: 'f2cf4f8b9ea4aefc4d1e79bfb00f2a0f3d0c7b66c7243d3e1a6df8495b9f6a36'