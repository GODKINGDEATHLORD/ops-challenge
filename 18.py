#!/usr/bin/env python3

# Script:                       18.py
# Author:                       Nicolaus Watson
# Date of latest revision:      2/2/2024
# Purpose:                      To perform a brute force wordlist attack, check if a password exists in a wordlist, perform SSH brute force, and brute force password-locked ZIP files.
# Referenced:                   Python documentation, Paramiko documentation, zipfile documentation, ChatGpt, Codefellows github repo 

# pip install zipfile

import time
import paramiko
import zipfile

# Offensive mode: Dictionary Iterator
# ... (Previous code remains unchanged)

# Defensive mode: Password Recognized
# ... (Previous code remains unchanged)

# Function: SSH Brute Force
# ... (Previous code remains unchanged)

# Function: ZIP Brute Force
# Tries to open a password-protected ZIP file using each word in the provided word list until successful.
def zip_brute_force():
    zip_filepath = input("Enter the path of the ZIP file:\n")
    password_list_filepath = input("Enter your dictionary filepath (e.g., rockyou.txt):\n")
    
    # Initialize the ZipFile object
    with zipfile.ZipFile(zip_filepath) as zip_file:
        with open(password_list_filepath, 'r', encoding="ISO-8859-1") as file:
            for line in file:
                password = line.strip().encode('utf-8')  # Passwords need to be encoded as bytes
                try:
                    # Try to extract the ZIP file with the current password
                    zip_file.extractall(pwd=password)
                    print(f"Success! Password: {password.decode('utf-8')}")
                    break  # Break out of the loop if the password is found
                except zipfile.BadZipFile:
                    # If the file is not a zip file or it is corrupted
                    print(f"Bad Zip File: {zip_filepath}")
                    break
                except zipfile.BadPassword:
                    # If the password is wrong, continue to the next one
                    pass
                except Exception as e:
                    # Handle other exceptions
                    print(f"An error occurred: {e}")
                    break

# Main function
if __name__ == "__main__":
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - SSH Brute Force
4 - ZIP File Brute Force
5 - Exit
Please enter a number: 
""")
        if mode == "1":
            dictionary_iterator()
        elif mode == "2":
            password_recognized()
        elif mode == '3':
            ssh_brute_force()
        elif mode == '4':
            zip_brute_force()
        elif mode == '5':
            break
        else:
            print("Invalid selection...")
