"""
on-way
"""
import random
import tkinter as tk

def hash_message(message):
    n = int(message)
    a = n % 10
    b = n % 100 // 10
    c = n % 1000 // 100
    d = n // 1000
    phi = (a + 1) * (b + 1) * (c + 1) * (d + 1)  # compute Euler's totient function
    pi = 3.14159  # approximate value of pi
    hash_value = int((phi * pi) / 1.41421)  # square root of 2
    return hash_value

def hash_to_hex(hash_value):
    hex_string = hex(hash_value)[2:].zfill(8)
    return hex_string

def generate_hash():
    message = message_entry.get()
    try:
        hash_value = hash_message(message)
        hex_string = hash_to_hex(hash_value)
        result_label.config(text=f"The hash value of '{message}' is: {hex_string}")
    except ValueError:
        result_label.config(text="Error: Input message must be a valid integer")

# Create the main window
window = tk.Tk()
window.title("Hash Generator")
window.geometry("600x200")

# Create the input frame
input_frame = tk.Frame(window)
input_frame.pack(side=tk.TOP, padx=10, pady=10)

# Create the input label and entry
message_label = tk.Label(input_frame, text="Enter a 4-digit integer message:")
message_label.pack(side=tk.LEFT, padx=10)
message_entry = tk.Entry(input_frame)
message_entry.pack(side=tk.LEFT, padx=10)

# Create the button to generate the hash value
generate_button = tk.Button(input_frame, text="Generate Hash", command=generate_hash)
generate_button.pack(side=tk.LEFT, padx=10)

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack(side=tk.TOP, padx=10, pady=10)

# Start the main event loop
window.mainloop()