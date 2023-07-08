# pip install pycrypto
# pip install cryptography
import datetime
from Crypto.Cipher import AES
import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, master):
        self.master = master
        master.title('Message Encryption')

        self.message_label = tk.Label(master, text='Message:')
        self.message_label.grid(row=0, column=0, padx=5, pady=5)

        self.message_entry = tk.Entry(master, width=50)
        self.message_entry.grid(row=0, column=1, padx=5, pady=5)

        self.key_label = tk.Label(master, text='Encryption Key:')
        self.key_label.grid(row=1, column=0, padx=5, pady=5)

        self.key_entry = tk.Entry(master, width=50)
        self.key_entry.grid(row=1, column=1, padx=5, pady=5)

        self.encrypt_button = tk.Button(master, text='Encrypt', command=self.encrypt_message)
        self.encrypt_button.grid(row=2, column=0, padx=5, pady=5)

        self.decrypt_button = tk.Button(master, text='Decrypt', command=self.decrypt_message)
        self.decrypt_button.grid(row=2, column=1, padx=5, pady=5)

        self.output_text = tk.Text(master, width=50, height=5)
        self.output_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Create the menu bar
        self.menu_bar = tk.Menu(master)

        # Create the Info menu
        self.info_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.info_menu.add_command(label='About', command=self.show_info)

        # Create the Version menu
        self.version_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.version_menu.add_command(label='Version', command=self.show_version)

        # Add menus to the menu bar
        self.menu_bar.add_cascade(label='Info', menu=self.info_menu)
        self.menu_bar.add_cascade(label='Version', menu=self.version_menu)

        # Configure the menu bar
        master.config(menu=self.menu_bar)

    def encrypt_message(self):
        key = self.key_entry.get().encode()
        if len(key) != 16:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, 'Error: Key must be 16 bytes long.')
            return
        message = self.message_entry.get()

        encrypted_message = encrypt_message(message, key)

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f'Encrypted message: {encrypted_message}')

    def decrypt_message(self):
        key = self.key_entry.get().encode()
        if len(key) != 16:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, 'Error: Key must be 16 bytes long.')
            return
        message = self.message_entry.get()

        try:
            nonce, ciphertext, tag = eval(message)
            decrypted_message = decrypt_message(nonce, ciphertext, tag, key)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f'Decrypted message: {decrypted_message}')
        except Exception as e:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f'Error: {e}')

    def show_info(self):
        messagebox.showinfo('About', 'This program encrypts and decrypts messages using the AES encryption algorithm. Enter a message and a 16-byte encryption key to encrypt the message. To decrypt a message, enter the encrypted message and the same encryption key that was used to encrypt the message.')

    def show_version(self):
        messagebox.showinfo('Version', 'Message Encryption v2.0\nCreated by [Mosi-sol@github]')

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return (nonce, ciphertext, tag)

def decrypt_message(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()