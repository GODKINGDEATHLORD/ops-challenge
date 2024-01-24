#!/usr/bin/env python

# import argparse   # not yet
import os       # stdlib's come first (top of the file, listed alphabetically)
import sys

import scapy    # third-party (aka pypi installed come second)

if len(sys.argv) != 2:
    print("Usage: arping2tex <net>\n  eg: arping2tex 192.168.1.0/24")
    sys.exit(1)
    
# Requirements

# In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:

# [x]  Utilize the scapy library
# [x]  Define host IP
# [x]  Define port range or specific set of ports to scan
#     Test each port in the specified range using a for loop
#         If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
#         If flag 0x14 received, notify user the port is closed.
#         If no flag is received, notify the user the port is filtered and silently dropped.
flags = sys.argv

host_ip = flags[1]
port_range = flags[2:]


if __name__ == "__main__":
    print(f"The host IP is: {host_ip}")
    print(f"the port range is: {port_range}")






