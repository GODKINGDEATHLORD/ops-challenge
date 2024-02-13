#!/usr/bin/env python3

# Script:                       elt1.py
# Author:                       Nicolaus Watson
# Date of latest revision:      2/13/2024






#!/usr/bin/env python3
import logging
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(filename='encryption_tool.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def write_key():
    """
    Generates a key and save it into a file
    """
    try:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        logging.info("Key generated successfully and saved to key.key")
    except Exception as e:
        logging.error(f"Failed to generate or save the key: {e}")

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    try:
        return open("key.key", "rb").read()
    except FileNotFoundError:
        logging.error("key.key file not found")
        raise
    except Exception as e:
        logging.error(f"An error occurred while loading the key: {e}")
        raise


if __name__ == '__main__':
    try:
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
        logging.info("Encryption and decryption operations completed successfully")
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
