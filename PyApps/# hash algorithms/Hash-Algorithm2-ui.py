"""
on-way
"""
import tkinter as tk
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

def generate_hash_values():
    """
    Generate hash values for the input message using the selected hash functions.
    """
    message = message_entry.get()
    hash_4 = hash_4bit(message)
    hash_8 = hash_8bit(message)
    hash_16 = hash_16bit(message)
    hash_32 = hash_32bit(message)
    hash_64 = hash_64bit(message)
    hash_128 = hash_128bit(message)
    hash_256 = hash_256bit(message)
    hash_512 = hash_512bit(message)
    hash_4_value.set(bin(hash_4)[2:].zfill(4))
    hash_8_value.set(hex(hash_8)[2:].zfill(2))
    hash_16_value.set(hex(hash_16)[2:].zfill(4))
    hash_32_value.set(hex(hash_32)[2:].zfill(8))
    hash_64_value.set(hex(hash_64)[2:].zfill(16))
    hash_128_value.set(hex(hash_128)[2:].zfill(32))
    hash_256_value.set(hex(hash_256)[2:].zfill(64))
    hash_512_value.set(hex(hash_512)[2:].zfill(128))

# Initialize the Tkinter application
root = tk.Tk()
root.title("Hash Generator")

# Create the message label and entry widget
message_label = tk.Label(root, text="Message:")
message_label.grid(row=0, column=0, padx=5, pady=5)
message_entry = tk.Entry(root, width=50)
message_entry.grid(row=0, column=1, padx=5, pady=5)

# Create the hash value labels and entry widgets
hash_4_label = tk.Label(root, text="4-bit hash value:")
hash_4_label.grid(row=1, column=0, padx=5, pady=5)
hash_4_value = tk.StringVar()
hash_4_entry = tk.Entry(root, width=6, textvariable=hash_4_value, state="readonly")
hash_4_entry.grid(row=1, column=1, padx=5, pady=5)

hash_8_label = tk.Label(root, text="8-bit hash value:")
hash_8_label.grid(row=2, column=0, padx=5, pady=5)
hash_8_value = tk.StringVar()
hash_8_entry = tk.Entry(root, width=6, textvariable=hash_8_value, state="readonly")
hash_8_entry.grid(row=2, column=1, padx=5, pady=5)

hash_16_label = tk.Label(root, text="16-bit hash value:")
hash_16_label.grid(row=3, column=0, padx=5, pady=5)
hash_16_value = tk.StringVar()
hash_16_entry = tk.Entry(root, width=6, textvariable=hash_16_value, state="readonly")
hash_16_entry.grid(row=3, column=1, padx=5, pady=5)

hash_32_label = tk.Label(root, text="32-bit hash value:")
hash_32_label.grid(row=4, column=0, padx=5, pady=5)
hash_32_value = tk.StringVar()
hash_32_entry = tk.Entry(root, width=10, textvariable=hash_32_value, state="readonly")
hash_32_entry.grid(row=4, column=1, padx=5, pady=5)

hash_64_label = tk.Label(root, text="64-bit hash value:")
hash_64_label.grid(row=5, column=0, padx=5, pady=5)
hash_64_value = tk.StringVar()
hash_64_entry = tk.Entry(root, width=18, textvariable=hash_64_value, state="readonly")
hash_64_entry.grid(row=5, column=1, padx=5, pady=5)

hash_128_label = tk.Label(root, text="128-bit hash value:")
hash_128_label.grid(row=6, column=0, padx=5, pady=5)
hash_128_value = tk.StringVar()
hash_128_entry = tk.Entry(root, width=34, textvariable=hash_128_value, state="readonly")
hash_128_entry.grid(row=6, column=1, padx=5, pady=5)

hash_256_label = tk.Label(root, text="256-bit hash value:")
hash_256_label.grid(row=7, column=0, padx=5, pady=5)
hash_256_value = tk.StringVar()
hash_256_entry = tk.Entry(root, width=66, textvariable=hash_256_value, state="readonly")
hash_256_entry.grid(row=7, column=1, padx=5, pady=5)

hash_512_label = tk.Label(root, text="512-bit hash value:")
hash_512_label.grid(row=8, column=0, padx=5, pady=5)
hash_512_value = tk.StringVar()
hash_512_entry = tk.Entry(root, width=130, textvariable=hash_512_value, state="readonly")
hash_512_entry.grid(row=8, column=1, padx=5, pady=5)

# Create the generate button
generate_button = tk.Button(root, text="Generate Hash Values", command=generate_hash_values)
generate_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()