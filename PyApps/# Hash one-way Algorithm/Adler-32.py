def adler32(data):
    MOD_ADLER = 65521
    a = 1
    b = 0
    for byte in data:
        a = (a + byte) % MOD_ADLER
        b = (b + a) % MOD_ADLER
    return (b << 16) | a
    
# ======================================
data = b"Hello, world!"
hash_value = adler32(data)
print(hex(hash_value))