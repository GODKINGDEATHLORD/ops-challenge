#!/bin/bash

# Script:
# Author:
# Purpose:
# Variables:

# echo `date`

echo $(date)

# variables 

year=`date +%Y`
echo $year

month=`date +%m`
echo $month

day=`date +%d`
echo $day

echo "Current Date: $day-$month-$year"
echo "Append this to the file test.txt"
echo "Current Date: $day-$month-$year" >> test.txt

# Copies /var/log/syslog to the current working directory
destination_filename="syslog_backup_$(date +%Y%m%d).txt"
echo "Copying /var/log/syslog to current directory as $destination_filename"
cp /var/log/syslog "./$destination_filename"


# End
# Notes >= overwrite >>= append or add on to  >= means carrot