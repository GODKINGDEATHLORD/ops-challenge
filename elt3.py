#!/usr/bin/env python3

# Script:                       elt3.py
# Author:                       Nicolaus Watson
# Date of latest revision:      2/2/2024
# Purpose:                      Add log rotation capability to the existing Python script for enhanced logging management.
# Referenced:                   Python documentation, ChatGPT, Codefellows GitHub repo, https://www.blog.pythonlibrary.org/2014/02/11/python-how-to-create-rotating-logs/

import logging
from logging.handlers import RotatingFileHandler, SMTPHandler, StreamHandler
from cryptography.fernet import Fernet

# Configure logging to include log rotation and terminal output
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

log_file_handler = RotatingFileHandler('encryption_tool.log', maxBytes=5*1024*1024, backupCount=2)
log_file_handler.setFormatter(log_formatter)

stream_handler = StreamHandler()
stream_handler.setFormatter(log_formatter)

logger = logging.getLogger('root')
logger.setLevel(logging.DEBUG)
logger.addHandler(log_file_handler)
logger.addHandler(stream_handler)

# Configure email notifications for error logs (replace placeholders with actual values)
email_handler = SMTPHandler(
    mailhost=("smtp.example.com", 587),
    fromaddr="from@example.com",
    toaddrs=["to@example.com"],
    subject="Error Log Notification",
    credentials=("email@example.com", "password"),
    secure=()
)
email_handler.setLevel(logging.ERROR)
email_handler.setFormatter(log_formatter)
logger.addHandler(email_handler)

def write_key():
    """
    Generates a key and saves it into a file
    """
    try:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        logger.info("Key generated successfully and saved to key.key")
    except Exception as e:
        logger.error(f"Failed to generate or save the key: {e}")

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    try:
        return open("key.key", "rb").read()
    except FileNotFoundError:
        logger.error("key.key file not found")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading the key: {e}")
        raise

if __name__ == '__main__':
    try:
        write_key()
        key = load_key()
        message = "some secret message".encode()
        f = Fernet(key)
        encrypted = f.encrypt(message)
        decrypted_encrypted = f.decrypt(encrypted)
        print(f"""
              Original Message: {message}
              Encrypted Text: {encrypted}
              Decrypted Text: {decrypted_encrypted}
              """)
        logger.info("Encryption and decryption operations completed successfully")
    except Exception as e:
        logger.critical(f"An unexpected error occurred: {e}")
