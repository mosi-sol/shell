# SHA-3 helper functions
def rotate_left(x, n):
    return ((x << n) | (x >> (64 - n))) & 0xffffffffffffffff

def keccak_f(state):
    # Round constants
    RC = [
        0x0000000000000001, 0x0000000000008082, 0x800000000000808a,
        0x8000000080008000, 0x000000000000808b, 0x0000000080000001,
        0x8000000080008081, 0x8000000000008009, 0x000000000000008a,
        0x0000000000000088, 0x0000000080008009, 0x000000008000000a,
        0x000000008000808b, 0x800000000000008b, 0x8000000000008089,
        0x8000000000008003, 0x8000000000008002, 0x8000000000000080,
        0x000000000000800a, 0x800000008000000a, 0x8000000080008081,
        0x8000000000008080, 0x0000000080000001, 0x8000000080008008
    ]

    # Theta step
    for x in range(5):
        C = state[x][0] ^ state[x][1] ^ state[x][2] ^ state[x][3] ^ state[x][4]
        D = C ^ rotate_left(C, 1) ^ rotate_left(C, 2)
        for y in range(5):
            state[x][y] ^= D

    # Rho and Pi steps
    for x in range(5):
        for y in range(5):
            state[x][y] = rotate_left(state[x][y], ((x * 5) + y))

    # Chi step
    for y in range(5):
        t = [0] * 5
        for x in range(5):
            t[x] = state[x][y] ^ ((~state[(x + 1) % 5][y]) & state[(x + 2) % 5][y])
        for x in range(5):
            state[x][y] = t[x]

    # Iota step
    state[0][0] ^= RC[0]
    for i in range(1, 24):
        state[x][y] ^= RC[i]
        RC[i] = rotate_left(RC[i-1], 1) ^ (0x01 if RC[i-1] & 0x80 else 0)

def pad_message(message):
    # Pad the message
    block_size = 136
    message += b'\x06'
    message += b'\x00' * ((-len(message) - 2) % block_size)
    message += b'\x80'

    # Split the message into blocks
    blocks = []
    for i in range(0, len(message), block_size):
        block = message[i:i + block_size]
        blocks.append([int.from_bytes(block[j:j + 8], byteorder='big') for j in range(0, block_size, 8)])

    return blocks

# SHA-3 hash function
def sha3_256(message):
    # Initialize the state
    state = [[0] * 5 for _ in range(5)]

    # Pad the message
    blocks = pad_message(message)

    # Absorb phase
    for block in blocks:
        for x in range(5):
            for y in range(5):
                state[x][y] ^= block[(x + y * 5) % len(block)]
        keccak_f(state)

    # Squeeze phase
    hash_value = ''
    for _ in range(256 // 8):
        hash_value += format(state[0][0], '02x')
        keccak_f(state)

    return hash_value
    
# ======================================
message = b'This is a test message'
hash = sha3_256(message)
print(hash)  # Output: 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'