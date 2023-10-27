#!/bin/bash

# Script Name:                  TMNT.sh
# Author:                       Nick Watson
# Date of latest revision:      10/24/2023
# Purpose:                      To make Teenage Mutant Ninja Turtle portfolios

# Create directories
mkdir Leonardo
mkdir Raphael
mkdir Donatello
mkdir Micheangelo

# Create an array with directory names
directories=("Leonardo" "Raphael" "Donatello" "Micheangelo")

# Main
# Loop through the array and create a .txt file in each directory
for dir in "${directories[@]}"; do
    touch "$dir/file.txt"
done
