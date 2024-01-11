#!/usr/bin/env python3

# imports datetime mode & os(gives you access to a bunch of commands that are specific to the operating system)
import datetime, os
# define timestamp and assign timestamp to variable now 
def timestamp():
    now = datetime.datetime.now()
    return now 

# Am i being run on the  command line or am I being imported?
if __name__ == '__main__':
# Prints the os function that we now have control over due to the import in line 4 and we are pinging the local host and time stamp
#  , and we tell it to ping once which is -c, and to wait 2 seconds before printing
    print(os.system("ping -i 2 localhost")) 
    print(timestamp())




# Requirements
# In Python, create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.

# The script must:

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# Evaluate the response as either success or failure.
# Assign success or failure to a status variable.
# For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
# Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8

# Stretch Goals (Optional Objectives)
# In Python, add the below features to your uptime sensor tool.

# The script must:

# Save the output to a text file as a log of events.
# Accept user input for target IP address.

