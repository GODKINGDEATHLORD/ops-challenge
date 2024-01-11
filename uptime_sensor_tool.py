#!/usr/bin/env python3

# References: https://gist.github.com/bockor/50fb07e0edaccbd879f2f4af8c428857 , https://gist.github.com/bockor/50fb07e0edaccbd879f2f4af8c428857, 
# https://realpython.com/python-f-strings/ , Also worked with Aaron Imbrock
# imports datetime mode & os(gives you access to a bunch of commands that are specific to the operating system)
from datetime import datetime 
import sys
import time

from pythonping import ping
# will reference these two variables on line 27,    sys.argv will give contents within contents 
# ip = 'localhost'
count = 1
ip = sys.argv[1]


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

        print(f"{timestamp} {status} to {ip}")
        time.sleep(2) 
       
