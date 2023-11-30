#!/bin/bash
# Ignore this, this is not my code, im too tired  to figure this out right now, I got this from ChatGpt

# Check if the user is root to prevent accidental permission changes on system files
if [ "$(id -u)" == "0" ]; then
   echo "This script should not be run as root or with sudo privileges."
   exit 1
fi

# Prompt the user for the directory path
read -p "Enter the directory path (not a system directory): " dir_path

# Verify if the directory exists
if [[ ! -d "$dir_path" ]]; then
    echo "Directory not found!"
    exit 1
fi

# Display current file permissions
echo "Current file permissions in $dir_path:"
ls -l "$dir_path"

# Choose mode for chmod (symbolic or numeric)
read -p "Choose mode for permission change (symbolic/numeric): " mode

if [[ $mode == "symbolic" ]]; then
    read -p "Enter symbolic permissions (e.g., u+x): " sym_perm
    chmod_command="chmod $sym_perm"
elif [[ $mode == "numeric" ]]; then
    read -p "Enter numeric permissions (e.g., 755): " num_perm
    chmod_command="chmod $num_perm"
else
    echo "Invalid mode selected."
    exit 1
fi

# Apply the permission changes
read -p "Apply recursively? (yes/no): " recursive
if [[ $recursive == "yes" ]]; then
    $chmod_command -R "$dir_path"
else
    $chmod_command "$dir_path"/*
fi

# Display the updated permissions
echo "Updated file permissions in $dir_path:"
ls -l "$dir_path"
