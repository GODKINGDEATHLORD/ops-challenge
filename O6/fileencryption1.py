#!/usr/bin/env python3
from cryptography.fernet import Fernet

# much of this code was taken from examples provided in
# https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
# 
# mkdir OC06          
# python3 -m venv .venv ( create virtual enviorment, so we dont polute or python library)
# source .venv/bin/activate    ( changes the path to use local python3) 
# pip install cryptography
# pip freeze > requirements.txt

# README.md
# This script requires installation of the `cryptography` pipy module
# ```bash
# python3 -m venv .venv   ( create virtual enviorments)
# source .venv/bin/activate (change path to use local enviorment )
# pip install -r requirements.txt (install python modules)

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

def encrypt_file():
    pass

def decrypt_file():
    pass

def encrypt_message():
    pass
    
def decrypt_message():
    pass

if __name__ == '__main__':

    # generate and write a new key
    write_key()
    key = load_key()
    message = "some secret message".encode()
    # initialize the Fernet class
    f = Fernet(key)
    encrypted = f.encrypt(message)
    decrypted_encrypted = f.decrypt(encrypted)
    print(f"""
        Original Message: {message}
        Encrypted Text: {encrypted}
        Decrypted Text: {decrypted_encrypted}
        """)











# Requirements
# In Python, create a script that utilizes the cryptography library to:

# Prompt the user to select a mode:
# Encrypt a file (mode 1)
# Decrypt a file (mode 2)
# Encrypt a message (mode 3)
# Decrypt a message (mode 4)
# If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
# If mode 3 or 4 are selected, prompt the user to provide a cleartext string.
# Depending on the selection, perform one of the below functions. You’ll need to create four functions:

# Encrypt the target file if in mode 1.
# Delete the existing target file and replace it entirely with the encrypted version.
# Decrypt the target file if in mode 2.
# Delete the encrypted target file and replace it entirely with the decrypted version.
# Encrypt the string if in mode 3.
# Print the ciphertext to the screen.
# Decrypt the string if in mode 4.
# Print the cleartext to the screen.`