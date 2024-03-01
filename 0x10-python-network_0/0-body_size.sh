#!/bin/bash
# This script takes a URL as input, sends a request to that URL, and displays the size of the response body in bytes

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Get the URL from the command line argument
url=$1

# Send a GET request using curl with silent mode and save the response body to a temporary file
temp_file=$(mktemp)
curl -s -o "$temp_file" "$url"

# Get the size of the response body in bytes
size=$(stat -c "%s" "$temp_file")

# Display the size
echo "$size"

# Clean up the temporary file
rm "$temp_file"
