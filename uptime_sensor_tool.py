#!/usr/bin/env python3

# imports datetime mode & os(gives you access to a bunch of commands that are specific to the operating system)
from datetime import datetime 
import os
import time

from pythonping import ping
# will reference these two variables on line 27
ip = 'localhost'
count = 1

# define timestamp and assign timestamp to variable now , from datetime its referencing the file called datetime 
def timestamp():
    now = datetime.now()
    return now 

# Am i being run on the  command line or am I being imported?
if __name__ == '__main__':
# Prints the os function that we now have control over due to the import in line 4 and we are pinging the local host and time stamp
#  , and we tell it to ping once which is -c, and to wait 2 seconds before printing
   status = ''
   timestamp = timestamp()
# while loop( wont stop unless we create a measure to break out of it), while the boolean check is true, run the code that well write, 
# and will wait two seconds before spitting it out again
   while True: 
        # print(os.system("ping -c 1 localhost")) the output of ping got assigned to result here
        result = ping(ip, count)
        if result.success():
            status = 'Network Active'
        else:
            status = 'Network Down'

        time.sleep(2) 
        print(f"{timestamp} {status} to {ip}")

# Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8



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

