#!/bin/bash

# If they didnt run it as super user
if [ "$EUID" -ne 0 ]; then
    echo "type sudo bash sysinfo.sh and it will work"
    exit 1
fi

# Display system information
echo "Computer Name:"
lshw -c system | grep "product\|vendor\|serial\|width\|description"
echo
echo "CPU:"
lshw -c cpu | grep "product\|vendor\|description"
echo
echo "RAM:"
lshw -c memory | grep "description\|size"
echo
echo "Display Adapter:"
lshw -c display | grep "description\|product\|vendor\|width\|clock"
echo
echo "Network Adapter:"
lshw -c network | grep "description\|product\|vendor\|logical name\|serial\|size\|capacity\|width\|clock"

exit 0
