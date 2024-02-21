#!/usr/bin/env python3

# Script:                       sbmd2.py
# Author:                       Nicolaus Watson
# Date of latest revision:      2/20/2024
# Purpose:                      Continue development of the malware detection tool to include hashing and logging.
# Referenced:                   Python documentation, ChatGPT, Codefellows GitHub repo,
#                               https://www.howtogeek.com/112674/how-to-find-files-and-folders-in-linux-using-the-command-line/,
#                               https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/,
#                               Hashlib Official Documentation, Python Program to Find Hash of File

import os
import hashlib
import logging
from datetime import datetime
import platform

# Set up logging with rotation
logging.basicConfig(filename='malware_scan_log.txt', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Initialize a 2D array to store file data
file_data_array = []

def generate_md5_hash(file_path):
    """Generate MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        logging.error(f"An error occurred while hashing the file: {file_path} with error: {e}")
        return None

def scan_directory(directory):
    """Recursively scan each file and folder in the directory."""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_size = os.path.getsize(file_path)
            md5_hash = generate_md5_hash(file_path)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file_info = (timestamp, file_path, md5_hash, file_size)
            file_data_array.append(file_info)
            print(f"Timestamp: {timestamp}, File: {filename}, Size: {file_size} bytes, MD5: {md5_hash}, Path: {file_path}")
            logging.info(f"Scanned File: {file_info}")

def main():
    # User input for directory
    directory = input("Enter the directory to scan: ")
    logging.info(f"Scan started for directory: {directory}")

    # Start directory scan
    scan_directory(directory)

    # Search summary
    print(f"Scan completed. {len(file_data_array)} file(s) scanned.")
    logging.info(f"Scan completed. {len(file_data_array)} file(s) scanned.")

if __name__ == "__main__":
    main()
