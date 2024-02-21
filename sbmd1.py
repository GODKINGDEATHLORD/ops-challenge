#!/usr/bin/env python3

# Script:                       sbmd1.py
# Author:                       Nicolaus Watson
# Date of latest revision:      2/20/2024
# Referenced:                   Python documentation, ChatGPT, Codefellows GitHub repo, https://www.howtogeek.com/112674/how-to-find-files-and-folders-in-linux-using-the-command-line/, https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/


import os
import platform
import subprocess
import logging

# Set up logging
logging.basicConfig(filename='malware_scan_log.txt', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def find_files_windows(filename, directory):
    """Find files in Windows."""
    try:
        command = f'where /r {directory} {filename}'
        results = subprocess.check_output(command, shell=True)
        files_found = results.decode().strip().split('\r\n')
        return files_found
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while searching for files: {e}")
        return []

def find_files_linux(filename, directory):
    """Find files in Linux."""
    try:
        command = f'find {directory} -name {filename}'
        results = subprocess.check_output(command, shell=True)
        files_found = results.decode().strip().split('\n')
        return files_found
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while searching for files: {e}")
        return []

def find_files(filename, directory):
    """Detect the OS and use the appropriate command to find files."""
    current_os = platform.system().lower()
    if current_os == 'windows':
        return find_files_windows(filename, directory)
    elif current_os == 'linux':
        return find_files_linux(filename, directory)
    else:
        logging.error(f"Unsupported OS: {current_os}")
        raise ValueError("This script only supports Windows and Linux")

def main():
    # User input for file name and directory
    filename = input("Enter the filename to search for: ")
    directory = input("Enter the directory to search in: ")

    # Find files
    logging.info(f"Search started for {filename} in {directory}")
    found_files = find_files(filename, directory)

    # Print and log results
    hits = len(found_files)
    if hits:
        print(f"Found {hits} file(s):")
        for file in found_files:
            print(file)
            logging.info(f"File found: {file}")
    else:
        print("No files found.")
        logging.info("No files found.")

    # Search summary
    print(f"Search completed. {hits} hit(s) found.")
    logging.info(f"Search completed. {hits} hit(s) found.")

if __name__ == "__main__":
    main()
