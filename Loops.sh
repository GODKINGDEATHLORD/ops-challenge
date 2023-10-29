#!/bin/bash

# Script:                     Loops.sh  
# Author:                     Nick Watson  
# Date of latest revision:    10/28/2023
# Purpose:                    Loop


while true; do
    # Display a list of running processes
    echo -e "\nList of running processes:"
    ps aux

    # Ask the user for a PID to kill
    read -p "Enter the PID of the process to terminate (or Ctrl+C to exit): " target_pid
    if [ -n "$target_pid" ]; then
        if [ "$target_pid" -ne $$ ]; then
            kill -15 "$target_pid"
            echo "Process with PID $target_pid has been terminated."
        else
            echo "You cannot terminate this script's process."
        fi
    fi
done

