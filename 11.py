#!/usr/bin/env python

# 11.py
# Author: Nick Watson
# Date of latest revision: 01/31/2024
# Purpose: TCP Port Range Scanner using Scapy
# References:  codefellows github repo, chatgpt 

from scapy.all import *
import random

# Define the target IP
target_ip = "192.168.1.1"

# Define the port range to scan
port_range = [22, 23, 80, 443]

# Iterate over the range of ports
for dst_port in port_range:
    # Randomize source port
    src_port = random.randint(1025, 65535)
    
    # Create a TCP SYN packet
    tcp_syn_packet = IP(dst=target_ip)/TCP(sport=src_port, dport=dst_port, flags='S')
    
    # Send the packet and wait for a response
    response = sr1(tcp_syn_packet, timeout=1, verbose=0)
    
    # Check if response is received
    if response is not None:
        # Check for SYN-ACK (0x12) flag - indicating port is open
        if response[TCP].flags == 0x12:
            # Send RST packet to graciously close the connection
            send_rst = sr(IP(dst=target_ip)/TCP(sport=src_port, dport=dst_port, flags='R'), timeout=1, verbose=0)
            print(f"Port {dst_port} is open.")
        
        # Check for RST (0x14) flag - indicating port is closed
        elif response[TCP].flags == 0x14:
            print(f"Port {dst_port} is closed.")
        
        else:
            print(f"Port {dst_port} response with unexpected flags: {response[TCP].flags}")
    else:
        # No response received, port is likely filtered and silently dropped
        print(f"Port {dst_port} is filtered (no response).")
