def crc(data):
    # Define the generator polynomial (CRC-32)
    generator = 0xEDB88320
    # Calculate the initial CRC value
    crc_value = 0xFFFFFFFF
    # Iterate over each byte of data
    for byte in data:
        # XOR the byte with the current CRC value
        crc_value ^= byte
        # Iterate over each bit of the byte
        for _ in range(8):
            # If the least significant bit is 1, XOR with the generator polynomial
            if crc_value & 1:
                crc_value = (crc_value >> 1) ^ generator
            # Otherwise, shift right by one bit
            else:
                crc_value >>= 1
    # Return the final CRC value
    return crc_value ^ 0xFFFFFFFF
    
# ======================================
data = b"Hello, world!"
print(crc(data))