# To run this script, you will need to have Python and Psutil installed on your system.
# You can install Psutil using `pip install psutil`.

import psutil

# Fetch various system times using Psutil
cpu_times = psutil.cpu_times()

# Save the information to a .txt file
with open('system_info.txt', 'w') as file:
    file.write(f"Time spent by normal processes executing in user mode: {cpu_times.user}\n")
    file.write(f"Time spent by processes executing in kernel mode: {cpu_times.system}\n")
    file.write(f"Time when system was idle: {cpu_times.idle}\n")
    file.write(f"Time spent by priority processes executing in user mode (nice): {cpu_times.nice}\n")
    file.write(f"Time spent waiting for I/O to complete: {cpu_times.iowait}\n")
    file.write(f"Time spent for servicing hardware interrupts: {cpu_times.irq}\n")
    file.write(f"Time spent for servicing software interrupts: {cpu_times.softirq}\n")
    file.write(f"Time spent by other operating systems running in a virtualized environment: {getattr(cpu_times, 'steal', 'N/A')}\n")
    file.write(f"Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel: {getattr(cpu_times, 'guest', 'N/A')}\n")

# For the email part, you will need to set up Sendmail or another SMTP server.
# Here is a placeholder for where you would add the email functionality.

# Email the .txt file using Sendmail (you will need to replace the placeholder code with your own Sendmail setup):
# Placeholder: Set up Sendmail or SMTP server details
# Placeholder: Send the email with the 'system_info.txt' attachment

print("System information has been saved to system_info.txt.")

# Resources ( I used chat gpt and looked over it, This will be my last time ill be relying on chatgpt,the way I have been. Ive still been reading through the challenge folder to better understand, I quit my job today so Ill have more time to learn)

# Question : what's a course that you recommend to do python
# How long you spent working on this assignment ? About 45 minutes to read through it, and try to understand. also to run the script , and add and take stuff away to see what it does
