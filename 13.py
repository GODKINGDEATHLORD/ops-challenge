#!/usr/bin/env python3

# Script:                       13.py
# Author:                       Nicolaus Watson
# Date of latest revision:      2/2/2024
# Purpose:                      Perform network scanning to ping an IP and scan its ports if it's alive using Scapy in Python.
# Execution:                    python 13.py
# Referenced:                   Scapy documentation, Python ipaddress module documentation, CHATGPT, Codefellows github repo

import ipaddress
from scapy.all import ICMP, IP, sr1, sr, RandShort, TCP

# Function to scan ports of a given IP
def tcp_port_scan(host_ip, port_range):
    print(f"Scanning ports on {host_ip}")
    open_ports = []
    for port in port_range:
        # Construct TCP packet with SYN flag
        pkt = IP(dst=host_ip)/TCP(sport=RandShort(), dport=port, flags="S")
        # Send the packet and wait for a reply
        response = sr1(pkt, timeout=1, verbose=0)
        
        # If a response is received
        if response:
            # If the response has a TCP layer and the SYN-ACK flag is set
            if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                # Port is open, send RST packet to graciously close the open connection
                send_rst = sr(IP(dst=host_ip)/TCP(sport=RandShort(), dport=port, flags="R"), timeout=1, verbose=0)
                open_ports.append(port)  # Add the port to the list of open ports
    
    # After scanning, report the open ports
    if open_ports:
        print(f"Open ports at {host_ip}: {open_ports}")
    else:
        print(f"No open ports found at {host_ip}.")

# Function to ping a host and call tcp_port_scan if the host is alive
def ping_and_scan(host_ip):
    print(f"Pinging {host_ip} - please wait...")
    # Send ICMP packet and wait for a reply
    icmp_response = sr1(IP(dst=host_ip)/ICMP(), timeout=2, verbose=0)
    
    # If no reply is received, the host is considered down or not responding
    if icmp_response is None:
        print(f"{host_ip} is down or not responding.")
    else:
        # If a reply is received, the host is up. Proceed to scan its ports.
        print(f"{host_ip} is alive, proceeding to scan ports...")
        port_range = range(1, 1025)  # Scanning the most common ports (1-1024)
        tcp_port_scan(host_ip, port_range)  # Call port scanning function

# Main function
if __name__ == "__main__":
    target_ip = input("Enter the IP address to target: ")  # User inputs the target IP address
    ping_and_scan(target_ip)  # Start the process by pinging and potentially scanning the target IP
