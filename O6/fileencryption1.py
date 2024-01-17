#!/usr/bin/env python3
from cryptography.fernet import Fernet
import os

def write_key():
    """
    Generates a key and saves it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

def encrypt_file(file_path, key):
    """
    Encrypts the target file and replaces it with the encrypted version
    """
    with open(file_path, "rb") as file:
        data = file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    """
    Decrypts the target file and replaces it with the decrypted version
    """
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def encrypt_message(message, key):
    """
    Encrypts the string and prints the ciphertext to the screen
    """
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    print(f"Encrypted Message: {encrypted_message.decode()}")

def decrypt_message(encrypted_message, key):
    """
    Decrypts the string and prints the cleartext to the screen
    """
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message.encode())
    print(f"Decrypted Message: {decrypted_message.decode()}")

if __name__ == '__main__':
    # generate and write a new key
    write_key()
    key = load_key()

    # prompt the user to select a mode
    mode = int(input("""Select mode:
                     1. Encrypt a file
                     2. Decrypt a file
                     3. Encrypt a message
                     4. Decrypt a message
                     > """))

    if mode == 1 or mode == 2:
        file_path = input("Enter the filepath to the target file: ")
        if not os.path.exists(file_path):
            print("File not found.")
            exit()
    elif mode == 3 or mode == 4:
        message = input("Enter the cleartext string: ")

    if mode == 1:
        encrypt_file(file_path, key)
        print(f"{file_path} encrypted successfully.")
    elif mode == 2:
        decrypt_file(file_path, key)
        print(f"{file_path} decrypted successfully.")
    elif mode == 3:
        encrypt_message(message, key)
    elif mode == 4:
        decrypt_message(message, key)