# pip install pycrypto
# pip install cryptography
import datetime
from Crypto.Cipher import AES

person1 = "John"
person2 = "Alice"

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return (nonce, ciphertext, tag)

def decrypt_message(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode()

key = b"mysecretkey12345"  # 16-byte key for AES-128

message1 = "Hi Alice, how are you?"
message2 = "I'm doing well, thanks. How about you?"

encrypted_message1 = encrypt_message(message1, key)
encrypted_message2 = encrypt_message(message2, key)

signed_message1 = f"{person1}:\n{encrypted_message1}\n"
signed_message2 = f"{person2}:\n{encrypted_message2}\n"

print(signed_message1)
print(signed_message2)

# To decrypt the messages:
received_message1 = signed_message1.split("\n")[1]
received_message2 = signed_message2.split("\n")[1]

nonce1, ciphertext1, tag1 = encrypted_message1
nonce2, ciphertext2, tag2 = encrypted_message2

decrypted_message1 = decrypt_message(nonce1, ciphertext1, tag1, key)
decrypted_message2 = decrypt_message(nonce2, ciphertext2, tag2, key)

print(f"{person1}: {decrypted_message1}")
print(f"{person2}: {decrypted_message2}")


"""
import datetime

person1 = "John"
person2 = "Alice"

def sign_message(message, sender):
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"{message}\n\n{sender}\n{formatted_date}"

message1 = "Hi Alice, how are you?"
message2 = "I'm doing well, thanks. How about you?"

signed_message1 = sign_message(message1, person1)
signed_message2 = sign_message(message2, person2)

print(signed_message1)
print(signed_message2)
"""