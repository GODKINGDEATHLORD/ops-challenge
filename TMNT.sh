#!/bin/bash

# Script Name:                  TMNT.sh
# Author:                       Nick Watson
# Date of latest revision:      10/24/2023
# Purpose:                      To make Teenage Mutant Ninja Turtle portfolios

#                               What we did here is we created for different folders using the "mkdir" command , then we created an array with the folder names we could refer to them later, anfter that we created a file in each of them called "file.txt". This could have been any  type of file though. So we looped through the array by going through the list one by one. THe " for dir in"${directores[@]}" told the computer to go throught the folders one at a time. Touch creates the file

# Create directories
mkdir Leonardo
mkdir Raphael
mkdir Donatello
mkdir Micheangelo

# Create an array with directory names
directories=("Leonardo" "Raphael" "Donatello" "Micheangelo")

# Loop through the array and create a .txt file in each directory
for dir in "${directories[@]}"; do
    touch "$dir/file.txt"
done
