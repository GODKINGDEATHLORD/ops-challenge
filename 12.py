#!/usr/bin/env python3

# Script:                       12.py
# Author:                       Nicolaus Watson
# Date of latest revision:      2/2/2024
# Purpose:                      To perform network scanning either by TCP port scanning or ICMP Ping sweep using Scapy in Python.
# Execution:                    python 12.py
# Referenced:                   Scapy documentation, Python ipaddress module documentation, CHATGPT

import os
import sys
import ipaddress
from scapy.all import ICMP, IP, sr1, TCP

# TCP Port Range Scanner from previous implementation
def tcp_port_scan(host_ip, port_range):
    # Your existing code for TCP Port Range Scanner
    # ...

# ICMP Ping Sweep
def icmp_ping_sweep(network_cidr):
    network = ipaddress.IPv4Network(network_cidr)
    hosts_count = 0

    for host in network.hosts():
        print(f"Pinging {host} - please wait...")
        response = sr1(IP(dst=str(host))/ICMP(), timeout=2, verbose=0)

        if response is None:
            print(f"{host} is down or not responding.")
        elif (
            response.haslayer(ICMP)
            and response.getlayer(ICMP).type == 3
            and response.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]
        ):
            print(f"{host} is actively blocking ICMP traffic.")
        else:
            print(f"{host} is responding.")
            hosts_count += 1

    print(f"{hosts_count}/{network.num_addresses - 2} hosts are online.")

# User menu
def user_menu():
    while True:
        print("\nChoose the scanning mode:")
        print("1 - TCP Port Range Scanner")
        print("2 - ICMP Ping Sweep")
        print("3 - Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            host_ip = input("Enter host IP: ")
            port_range = range(int(input("Enter start port: ")), int(input("Enter end port: ")) + 1)
            tcp_port_scan(host_ip, port_range)
        elif choice == '2':
            network_cidr = input("Enter network address with CIDR block (e.g., 10.10.0.0/24): ")
            icmp_ping_sweep(network_cidr)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    user_menu()
