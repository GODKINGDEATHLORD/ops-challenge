#!/usr/bin/env python3

# References: https://gist.github.com/bockor/50fb07e0edaccbd879f2f4af8c428857 , https://gist.github.com/bockor/50fb07e0edaccbd879f2f4af8c428857, 
# https://realpython.com/python-f-strings/ , Also worked with Aaron Imbrock
# imports datetime mode & os(gives you access to a bunch of commands that are specific to the operating system)
# imports secure mail transfer protocol library   from 7-10 built in to python formally known as standard library
from datetime import datetime 
import sys
import time
import smtplib
import subprocess
# Not part of python, downloaded and installed using pip( publically accessable on the internet)
# from pythonping import ping
# will reference these two variables on line 27,    sys.argv scans the list , and then you reference it in order, 
# ip = 'localhost' 
ping_count = 1
ip = sys.argv[1]
admin_email = 'joebobfredjohnjrthethird@gmail.com'
sender_email = sys.argv[2]
sender_pw = sys.argv[3]
email_message = 'test'
# we define a function called timestamp and which returns the current time , from datetime its referencing the file called datetime 
def timestamp():
    now = datetime.now()
    return now 
# the variable 's' represents the conversation with the gmail server 
def sendemail(
        message=email_message, 
        sender_email='joebobfredjohnjrthethird@gmail.com',
        sender_password=sender_pw, 
        receiver_email=admin_email):
    # Creates SMTP session ( initiates a convo) ( who we want to talk to, and what port they are listening on)
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # Start TLS for security ( encrypting conversation )
    s.starttls()

    # Authentication (I claim to be x, and this is my credentials)
    s.login(sender_email, sender_password)

    # Sending the mail ( we send the message to gmail, which we have authenticated , and the gmail server sends it to who we want to talk to )
    s.sendmail(sender_email, receiver_email, message)

    # Terminating the session ( formally ending the conversation with the gmail server )
    s.quit()   
    print('email sent')

def ping_ip(ip):
    try:
        output = subprocess.check_output("ping -c 1" + ip, shell=True)
        return True
    except subprocess.CalledProcessError: 
        return False
    
    # Am i being run on the  command line or am I being imported? will this be  will this be a script or a library 
if __name__ == '__main__':
#  the return value of timestamp() gets assigned to the variable time_stamp    'doesnt ask us to send an email if its down, but ask us to send an
#    email if it changes, was this intended'
   status_message = ''
   time_stamp = timestamp()
   state = 'up'
   new_state = 'up'

# while loop( wont stop unless we create a measure to break out of it), while the boolean check is true, run the code that well write, 
# and will wait two seconds before spitting it out again
   while True: 
        # print(os.system("ping -c 1 localhost")) the output of ping got assigned to result here
        result = ping_ip(ip)
        if result:
            status_message = 'Network Active'
            new_state = 'up'
        else:
            new_state = 'down'
            status_message = 'Network Down'
# go through this again
        if new_state != state:
            message = f"""
                hostname {ip}
                previous status {state}
                new status {new_state}
                time {time_stamp}

                IMPORTANT NOTES:

                """
            print(message)
            sendemail(message)

        state = new_state
# so itll print the value of time_stamp, along with the value of status and the ip address , and were using something called f strings
# and we told it to take 2 seconds before outputing the results( it makes it so the while loop does not loop for 2 seconds )
        print(f"{time_stamp} {status_message} to {ip}")
        time.sleep(2) 
       
# Requirements
# In Python, add the below features to your uptime sensor tool.

# The script must:

# Ask the user for an email address and password to use for sending notifications.
# Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
# Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.
# Important Notes

# DO NOT commit your email password in plain text within your script to GitHub as this easily becomes public.
# Create a new “burner” account for this exercise. Do not use an existing email account.
# Stretch Goals (Optional Objectives)
# In Python, add the below features to your uptime sensor tool.

# Append all status changes to an event log. Each event must include a timestamp, event code, any host IP addresses involved, and a human readable description.
# Check for BURNER_EMAIL_ADDRESS and BURNER_EMAIL_PASSWORD environment variables (eg: loaded from .profile). If found, the script skips requesting credentials via user input.
# Alternatively, send the notification email from a cloud mailer service (like Mailgun, or AWS SES), instead of SMTP through your burner address.