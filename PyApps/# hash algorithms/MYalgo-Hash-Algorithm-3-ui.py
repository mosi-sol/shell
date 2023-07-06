import hashlib
import tkinter as tk

class HashUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input_label = tk.Label(self, text="Input:")
        self.input_label.pack()

        self.input_text = tk.Text(self, height=10)
        self.input_text.pack()

        self.offset_label = tk.Label(self, text="Offset:")
        self.offset_label.pack()

        self.offset_slider = tk.Scale(self, from_=0, to=255, orient=tk.HORIZONTAL)
        self.offset_slider.pack()

        self.hash_button = tk.Button(self, text="Generate Hash", command=self.generate_hash)
        self.hash_button.pack()

        self.output_label = tk.Label(self, text="Output:")
        self.output_label.pack()

        self.output_text = tk.Text(self, height=10)
        self.output_text.pack()

        self.output_text.bind("<Control-a>", lambda event: self.output_text.tag_add(tk.SEL, "1.0", tk.END))
        self.output_text.bind("<Control-c>", lambda event: self.output_text.event_generate("<Control-a>"))
        self.output_text.bind("<Control-c>", lambda event: self.output_text.event_generate("<<Copy>>"), add="+")

    def generate_hash(self):
        input_str = self.input_text.get("1.0", tk.END).strip()
        offset = self.offset_slider.get()

        hash_result = hash_offset_xor(input_str, offset)
        res = hash_hex(hash_result)

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, "Input: {}\nOffset: {}\nHash Result: 0x{}\n".format(input_str, offset, res))

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

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hash Generator")
    app = HashUI(master=root)
    app.mainloop()
