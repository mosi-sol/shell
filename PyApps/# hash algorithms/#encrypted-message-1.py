# python zk.py -m "Hi Alice, how are you?" -k "mysecretkey12345" -e

# python zk.py -m "(b'\\x9d\\x8b\\x1d\\xf1#\\x88\\x9c\\x9c\\xd7\\x9b\\xea\\x06\\x88\\x82\\x03\\xae', b'\\x8e\\xdc\\x11^\\x87\\x8f\\xc5\\x9c\\x0e\\x94\\x9e\\x0b\\x4d\\x4e\\x87\\x12\\x7e\\xca\\x91\\x5d\\n\\x9b\\xdc\\x7f\\xa6\\xdf\\x46\\x8c\\x2b\\x8c\\x8d\\x82', b'^\\x1b\\x13!\\x8b\\x8b\\x10\\xc6\\xd6\\x8b\\xb2\\x9c\\xb5\\xb7\\x8a\\xd9\\x1c')" -k "mysecretkey12345" -d

# pip install pycrypto
# pip install cryptography
import argparse
import datetime
from Crypto.Cipher import AES

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
    parser = argparse.ArgumentParser(description='Encrypt and decrypt messages using AES-128 encryption.')
    parser.add_argument('-m', '--message', type=str, help='The message to encrypt or decrypt.')
    parser.add_argument('-k', '--key', type=str, help='The secret key to use for encryption or decryption.')
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the message.')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the message.')
    args = parser.parse_args()

    if args.encrypt and args.decrypt:
        print('Error: You can only encrypt or decrypt a message at a time.')
        exit()

    if not args.message or not args.key:
        print('Error: You must provide a message and a key.')
        exit()

    key = args.key.encode()
    message = args.message

    if args.encrypt:
        encrypted_message = encrypt_message(message, key)
        print(f'Encrypted message: {encrypted_message}')
    elif args.decrypt:
        try:
            nonce, ciphertext, tag = eval(message)
            decrypted_message = decrypt_message(nonce, ciphertext, tag, key)
            print(f'Decrypted message: {decrypted_message}')
        except Exception as e:
            print(f'Error: {e}')
            exit()