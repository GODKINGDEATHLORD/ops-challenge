#!/bin/bash

# Script:                     array.sh  
# Author:                     Nicolaus Watson  
# Date of latest revision:    10/26/2023  
# Purpose:                    Demo array
# Execution:                  bash array.sh or ./array.sh chmod -x array.sh
# Additional Sources:         X

# Declaration of variables 

snack="skittles"
#        index 0      index 1
snacks=("skittles" "pop tarts" "snickers" "tamales" "myself")


# Basic function
login_history () {
  last | head -3 # last five logins
  echo this is the login history 
}

# Main
login_history
login_history
login_history


# End
