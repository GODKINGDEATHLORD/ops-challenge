#!/usr/bin/env python3

# Import libraries
import os

# Declaration of variables
# Read user input here into a variable
user_path = input("Please enter the directory path: ")

# Declaration of functions
# Declare a function here
def list_directories(path):
    """Function to print all directories, sub-directories, and files"""
    for (root, dirs, files) in os.walk(path):
        # Add a print command here to print ==root==
        print("Root:", root)
        # Add a print command here to print ==dirs==
        print("Directories:", dirs)
        # Add a print command here to print ==files==
        print("Files:", files)

# Main
# Pass the variable into the function here
list_directories(user_path)

# Stretch Goal #1: Save the output to a .txt file
output_file = 'directory_listing.txt'
with open(output_file, 'w') as file:
    for (root, dirs, files) in os.walk(user_path):
        file.write(f"Root: {root}\n")
        file.write(f"Directories: {dirs}\n")
        file.write(f"Files: {files}\n\n")

# Stretch Goal #2: Open the .txt file with Libre Office Writer
os.system(f"libreoffice --writer {output_file}")

# End


# Resources Chatgpt & github 