#!/bin/bash

# get_ip_info.sh
# Script to fetch detailed IP information

# Sample Output:
# -------------------------------------------------
# MacBook-Air:bits-and-scripts anish$ ./get_ip_info.sh 
# Public IPv4: 143.244.44.163
# Hostname   : unn-143-244-44-163.datapacket.com
# City       : New York City
# Region     : New York
# Country    : US
# Location   : 40.7143,-74.0060
# Org / ISP  : AS212238 Datacamp Limited
# Timezone   : America/New_York
# Public IPv6: 2a02:6ea0:c412:2217::12
# -------------------------------------------------

ipinfo=$(curl -s https://ipinfo.io/json)

if command -v jq > /dev/null; then
  echo "Public IPv4: $(echo "$ipinfo" | jq -r '.ip')"
  echo "Hostname   : $(echo "$ipinfo" | jq -r '.hostname')"
  echo "City       : $(echo "$ipinfo" | jq -r '.city')"
  echo "Region     : $(echo "$ipinfo" | jq -r '.region')"
  echo "Country    : $(echo "$ipinfo" | jq -r '.country')"
  echo "Location   : $(echo "$ipinfo" | jq -r '.loc')"
  echo "Org / ISP  : $(echo "$ipinfo" | jq -r '.org')"
  echo "Timezone   : $(echo "$ipinfo" | jq -r '.timezone')"
else
  echo "Please install 'jq' to parse JSON."
fi

ipv6=$(curl -s -6 https://api64.ipify.org)
[[ -n "$ipv6" ]] && echo "Public IPv6: $ipv6" || echo "Public IPv6: Not available"

