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
echo "Current Date: $day-$month-$year" >> test,txt

# End
# Notes >= overwrite >>= append or add on to  >= means carrot