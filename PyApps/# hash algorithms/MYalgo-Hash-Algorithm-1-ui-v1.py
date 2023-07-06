import tkinter as tk

MARGIN_BYTES = 4  # Set the margin value to 4 bytes
KEY = b'\x12\x34\x56\x78'  # Set the key to a random byte sequence of 4 bytes

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

def generate_hash():
    # Get the user input from the text box
    message = input_box.get()

    # Generate the hash value for the input message
    hash_value = xor_hash(message.encode())

    # Determine the output format (hexadecimal or binary)
    output_format = output_var.get()

    # Convert the hash value to the selected output format
    if output_format == 'Hexadecimal':
        hash_str = '0x' + hash_value.hex()
    else:
        hash_str = ' '.join(format(b, '08b') for b in hash_value)

    # Update the output label with the hash value
    output_label.config(text=hash_str)

# Create the main window
root = tk.Tk()
root.title("XOR Hash Generator")
root.geometry("600x200")

# Create the input text box
input_label = tk.Label(root, text="Enter a message to hash:")
input_label.pack(pady=10)
input_box = tk.Entry(root, width=50)
input_box.pack()

# Create the output dropdown menu
output_label = tk.Label(root, text="")
output_label.pack(pady=10)
output_var = tk.StringVar(value='Hexadecimal')
output_dropdown = tk.OptionMenu(root, output_var, 'Hexadecimal', 'Binary')
output_dropdown.pack()

# Create the generate hash button
generate_button = tk.Button(root, text="Generate Hash", command=generate_hash)
generate_button.pack(pady=10)

# Start the main event loop
root.mainloop()
