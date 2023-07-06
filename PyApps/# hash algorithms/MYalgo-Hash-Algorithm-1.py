MARGIN_BYTES = 4  # Set the margin value to 4 bytes
KEY = b'\x12\x34\x56\x78'  # Set the key to a random byte sequence of 4 bytes

def generate_hash():
    while True:
        # Ask the user for a message to hash
        message = input("Enter a message to hash (or 'exit' to quit): ")
        if message == 'exit':
            break

        # Generate the hash value for the input message
        hash_value = xor_hash(message.encode())

        # Print the hash value as a hexadecimal string
        #print(f"Hash value for '{message}': {hash_value.hex()}")
        print(f"Hash value for '{message}': 0x{hash_value.hex()}")

def xor_hash(data):
    # Pad the input data with zeros to make its length a multiple of the margin value
    data_len = len(data)
    padding_len = (MARGIN_BYTES - (data_len % MARGIN_BYTES)) % MARGIN_BYTES
    padded_data = data + b'\x00' * padding_len

    # Split the padded data into margin-sized blocks and XOR them with the key
    hash_blocks = [bytes(x ^ y for x, y in zip(padded_data[i:i+MARGIN_BYTES], KEY))
                   for i in range(0, len(padded_data), MARGIN_BYTES)]

    # Concatenate the XORed blocks to form the final hash value
    return b''.join(hash_blocks)
    
# ==========================================

generate_hash()
