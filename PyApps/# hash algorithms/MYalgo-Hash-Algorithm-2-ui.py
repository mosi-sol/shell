import tkinter as tk
import hashlib

# one-way hash algorithm, used offset
def hasher(message, offset):
    # Convert the offset from hex to integer
    offset_int = int(offset, 16)
    # Add the offset to each character in the message
    offset_message = "".join([chr(ord(c) + offset_int) for c in message])
    # Generate the hash of the offset message using SHA-256
    hash_object = hashlib.sha256(offset_message.encode())
    hash_hex = hash_object.hexdigest()
    return "Offset message: " + offset_message + "\nHash: 0x" + hash_hex

# Create the main window
root = tk.Tk()
root.title("Hasher | Offset max is utf-8 length (- to +)")
root.geometry("800x600") # Set the width to 800 pixels and the height to 600 pixels

# Create the message label and entry field
msg_label = tk.Label(root, text="Message:")
msg_label.pack(side=tk.TOP)
msg_entry = tk.Entry(root, width=50)
msg_entry.pack(side=tk.TOP)

# Create the offset label and entry field
offset_label = tk.Label(root, text="Offset (in hex):")
offset_label.pack(side=tk.TOP)
offset_entry = tk.Entry(root, width=50)
offset_entry.pack(side=tk.TOP)

# Define a function to run the hasher and display the output
def run_hasher():
    message = msg_entry.get()
    offset = offset_entry.get()
    output = hasher(message, offset)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, output)

# Create the button to run the hasher
hash_button = tk.Button(root, text="Hash", command=run_hasher)
hash_button.pack(side=tk.TOP)

# Create the text widget to display the output
output_text = tk.Text(root, width=50, height=10)
output_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Make the text widget scrollable
output_scroll = tk.Scrollbar(output_text)
output_scroll.pack(side=tk.RIGHT, fill=tk.Y)
output_text.config(yscrollcommand=output_scroll.set)
output_scroll.config(command=output_text.yview)

# Allow the user to copy the output by selecting it and pressing Ctrl+C
def copy_output(event):
    root.clipboard_clear()
    root.clipboard_append(output_text.selection_get())

output_text.bind("<Control-c>", copy_output)

# Run the main loop
root.mainloop()
