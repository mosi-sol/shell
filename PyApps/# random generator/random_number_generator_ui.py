import random
import tkinter as tk

def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(bit_length):
    """Generate a random prime number with the specified bit length."""
    while True:
        n = random.getrandbits(bit_length)
        if is_prime(n):
            return n

def hex_to_binary(hex_str):
    """Convert a hexadecimal string to binary."""
    binary_str = bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)
    return binary_str

def hex_to_int(hex_str):
    """Convert a hexadecimal string to an integer."""
    int_value = int(hex_str, 16)
    return int_value

def caesar_hash(message, hash_key, prime):
    """Compute the Caesar cipher hash value of the message."""
    # Convert message to numerical value
    num_value = sum(ord(char) for char in message)

    # Apply Caesar cipher
    hash_code = (num_value + hash_key) % prime

    # Convert hash code to hexadecimal format
    hex_digits = []
    while hash_code > 0:
        hex_digit = hex(hash_code % 16)[2:]
        hex_digits.append(hex_digit)
        hash_code //= 16
    hex_value = ''.join(hex_digits[::-1]).zfill(4)

    return hex_value

class RandomGeneratorUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Generator")
        
        # Create input widgets
        self.message_label = tk.Label(self.master, text="Message:")
        self.message_entry = tk.Entry(self.master)
        self.bit_length_label = tk.Label(self.master, text="Bit length:")
        self.bit_length_entry = tk.Entry(self.master)
        
        # Create output widgets
        self.prime_label = tk.Label(self.master, text="Prime:")
        self.prime_value = tk.StringVar()
        self.prime_output = tk.Label(self.master, textvariable=self.prime_value)
        self.hash_key_label = tk.Label(self.master, text="Hash key:")
        self.hash_key_value = tk.StringVar()
        self.hash_key_output = tk.Label(self.master, textvariable=self.hash_key_value)
        self.hex_value_label = tk.Label(self.master, text="Hex value:")
        self.hex_value_value = tk.StringVar()
        self.hex_value_output = tk.Label(self.master, textvariable=self.hex_value_value)
        self.binary_value_label = tk.Label(self.master, text="Binary value:")
        self.binary_value_value = tk.StringVar()
        self.binary_value_output = tk.Label(self.master, textvariable=self.binary_value_value)
        self.int_value_label = tk.Label(self.master, text="Integer value:")
        self.int_value_value = tk.StringVar()
        self.int_value_output = tk.Label(self.master, textvariable=self.int_value_value)
        self.final_value_label = tk.Label(self.master, text="Final random number (dice 1 to 6):")
        self.final_value_value = tk.StringVar()
        self.final_value_output = tk.Label(self.master, textvariable=self.final_value_value)
        
        # Create button
        self.generate_button = tk.Button(self.master, text="Generate", command=self.generate_random)
        
        # Grid layout
        self.message_label.grid(row=0, column=0, sticky="w")
        self.message_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")
        self.bit_length_label.grid(row=1, column=0, sticky="w")
        self.bit_length_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")
        self.prime_label.grid(row=2, column=0, sticky="w")
        self.prime_output.grid(row=2, column=1, padx=5, pady=5, sticky="we")
        self.hash_key_label.grid(row=3, column=0, sticky="w")
        self.hash_key_output.grid(row=3, column=1, padx=5, pady=5, sticky="we")
        self.hex_value_label.grid(row=4, column=0, sticky="w")
        self.hex_value_output.grid(row=4, column=1, padx=5, pady=5, sticky="we")
        self.binary_value_label.grid(row=5, column=0, sticky="w")
        self.binary_value_output.grid(row=5, column=1, padx=5, pady=5, sticky="we")
        self.int_value_label.grid(row=6, column=0, sticky="w")
        self.int_value_output.grid(row=6, column=1, padx=5, pady=5, sticky="we")
        self.final_value_label.grid(row=7, column=0, sticky="w")
        self.final_value_output.grid(row=7, column=1, padx=5, pady=5, sticky="we")
        self.generate_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        
        # Set default values
        self.message_entry.insert(0, "Willy Seen in tiny moon!")
        self.bit_length_entry.insert(0, "16")
        self.prime_value.set("")
        self.hash_key_value.set("")
        self.hex_value_value.set("")
        self.binary_value_value.set("")
        self.int_value_value.set("")
        self.final_value_value.set("")
    
    def generate_random(self):
        # Get input values
        message = self.message_entry.get()
        bit_length = int(self.bit_length_entry.get())
        
        # Generate random number
        prime = generate_prime(bit_length)
        hash_key = random.randint(1, prime-1)
        hex_value = caesar_hash(message, hash_key, prime)
        binary_value = hex_to_binary(hex_value)
        int_value = hex_to_int(hex_value)
        final_value = (int_value % 6) + 1
        
        # Set output values
        self.prime_value.set(str(prime))
        self.hash_key_value.set(str(hash_key))
        self.hex_value_value.set(hex_value)
        self.binary_value_value.set(binary_value)
        self.int_value_value.set(str(int_value))
        self.final_value_value.set(str(final_value))

# Create and run the UI
if __name__ == "__main__":
    root = tk.Tk()
    app = RandomGeneratorUI(root)
    root.mainloop()