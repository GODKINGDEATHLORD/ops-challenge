#!/bin/bash

#  print network adapter information
function print_ip_info() {
    echo "Network Adapter Information:"
    ifconfig
}

#  system loop
while true; do
    clear
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
    read -p "Please enter your choice: " choice

    if [[ $choice == 1 ]]; then
        echo "Hello world!"
        read -p "Press Enter to continue"

    elif [[ $choice == 2 ]]; then
        ping -c 4 127.0.0.1
        read -p "Press Enter to continue"

    elif [[ $choice == 3 ]]; then
        print_ip_info
        read -p "Press Enter to continue"

    elif [[ $choice == 4 ]]; then
        echo "Exiting..."
        exit 0

    else
        echo "Invalid choice"
        read -p "Press Enter to continue"
    fi
done

# utilized chatgp