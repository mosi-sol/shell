import hashlib

# one-way hash algorithm, used offset
def hasher(message = "Hello, world!", offset = "2f"):
    # Convert the offset from hex to integer
    offset_int = int(offset, 16)
    # Add the offset to each character in the message
    offset_message = "".join([chr(ord(c) + offset_int) for c in message])
    # Generate the hash of the offset message using SHA-256
    hash_object = hashlib.sha256(offset_message.encode())
    hash_hex = hash_object.hexdigest()
    print("Offset message: ", offset_message)
    print("Hash: ", "0x"+hash_hex)
    

# test one-way hash algorithm, used offset
# Define the string to be hashed
message = "Secret message"
# Define the offset (in hex)
offset = "d7" # 2f,5a => this is the hexadecimal offset
hasher(message, offset)
