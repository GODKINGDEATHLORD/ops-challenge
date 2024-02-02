#!/usr/bin/env python3

# Script:                       16.py
# Author:                       Nicolaus Watson
# Date of latest revision:      2/2/2024
# Purpose:                      To perform a brute force wordlist attack or check if a password exists in a wordlist.
# Execution:                    python 16.py
# Referenced:                   Python documentation, PyAutoGUI. codefellows demo , chatgpt

import time

# Function: Dictionary Iterator (Offensive Mode)
# Iterates through a user-specified wordlist file and prints each word with a delay.
def dictionary_iterator():
    filepath = input("Enter your dictionary filepath:\n")  # Prompt the user for the file path of the dictionary.
    
    try:
        # Try to open the specified file with the appropriate encoding.
        with open(filepath, encoding="ISO-8859-1") as file:
            # Read the file line by line.
            for line in file:
                word = line.strip()  # Remove newline characters at the end of each line to get the word.
                print(word)  # Print the word.
                time.sleep(1)  # Wait for 1 second before moving to the next word.
    except FileNotFoundError:
        # If the file is not found, inform the user.
        print("File not found. Please check the file path and try again.")

# Function: Password Recognized (Defensive Mode)
# Searches a user-specified wordlist file for a user-specified string and indicates whether the string is found.
def password_recognized():
    user_string = input("Enter the password to search for:\n")  # Prompt the user for the password to search for.
    filepath = input("Enter your dictionary filepath:\n")  # Prompt the user for the file path of the dictionary.
    
    try:
        # Try to open the specified file with the appropriate encoding.
        with open(filepath, encoding="ISO-8859-1") as file:
            # Read the entire file's contents and check if the user's string is present.
            if user_string in file.read():
                # If the string is found, notify the user.
                print(f"The string '{user_string}' was found in the word list.")
            else:
                # If the string is not found, notify the user.
                print(f"The string '{user_string}' was NOT found in the word list.")
    except FileNotFoundError:
        # If the file is not found, inform the user.
        print("File not found. Please check the file path and try again.")

# Main function: Entry point of the script.
if __name__ == "__main__":
    while True:
        # Present a menu to the user.
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Exit
Please enter a number: 
""")
        # Execute the corresponding function based on user input.
        if mode == "1":
            dictionary_iterator()
        elif mode == "2":
            password_recognized()
        elif mode == '3':
            # Exit the loop and end the script if the user chooses to exit.
            break
        else:
            # Inform the user if they make an invalid selection.
            print("Invalid selection...")
