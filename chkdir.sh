#!/bin/bash

# Array of file or dirctory names to check and create
items_to_check=("Howsitgoingifyourereadingthissaywassupincomments" "Raymond.txt" "Caoagdan" "Thisisntcreepyimjustbored.txt")

# Loop through the items in the array
for item in "${items_to_check[@]}"; do
    # Check if the item exists
    if [ ! -e "$item" ]; then
        # If it doet exist, create it
        if [[ "$item" == *.* ]]; then
            # If it has a file extension, create a file
            touch "$item"
            echo "File '$item' didn't exist and has been created."
        else
            # If file doesnt exist, create a directory
            mkdir -p "$item"
            echo "'$item' didn't exist and has been created."
        fi
    else
        echo "'$item' already exists."
    fi
done
# Still using my bank of information but im getting better with scripts
echo "I hope this suffices"

