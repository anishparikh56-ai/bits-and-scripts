#!/bin/bash

# get_my_ip.sh
# Simple script to get public IPv4 address

# Sample Output:
# --------------------------------------
# MacBook-Air:bits-and-scripts anish$ ./get_my_ip.sh 
# Your public IP address is: 143.244.44.163
# --------------------------------------

ip=$(curl -s https://api.ipify.org)
echo "Your public IP address is: $ip"

