#!/bin/bash

# Script:                     Login History  
# Author:                     Nicolaus Watson  
# Date of latest revision:    10/26/2023  
# Purpose:                    To check login history 

# Declaration of functions

# Basic function
login_history () {
  last | head -3 # last five logins
  echo This is the login history 
}

# Main
login_history
login_history
login_history


# End
