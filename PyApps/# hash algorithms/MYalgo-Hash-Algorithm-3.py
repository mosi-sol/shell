import hashlib

def hash_hex(hex_input):
    # Convert hexadecimal input to bytes
    byte_input = bytes.fromhex(hex_input)

    # Use SHA-256 algorithm to generate hash
    hash_object = hashlib.sha256(byte_input)

    # Get hex representation of hash
    hex_hash = hash_object.hexdigest()

    return hex_hash
    

def hash_offset_xor(input_str, offset):
    # Convert input string to bytes
    input_bytes = input_str.encode('utf-8')
    
    # Apply offset to each byte
    offset_bytes = bytes([(b + offset) % 256 for b in input_bytes])
    
    # Apply xor to each byte with the offset
    xor_bytes = bytes([b ^ offset for b in offset_bytes])
    
    # Return the hexadecimal representation of the xor_bytes
    return xor_bytes.hex()

# Example usage
def run():
	input_str = "hello world"
	offset = 10
	hash_result = hash_offset_xor(input_str, offset)
	res = hash_hex(hash_result)
	print(hash_result)
	print("0x"+res)

run()
