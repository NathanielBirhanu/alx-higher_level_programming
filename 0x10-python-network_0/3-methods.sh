#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Get the URL from the command line argument
url=$1

# Send an OPTIONS request using curl and save the response headers to a temporary file
temp_file=$(mktemp)
curl -s -o "$temp_file" -I "$url"

# Extract the Allow header from the response headers
allow_header=$(grep -i "^Allow:" "$temp_file")

# Extract the HTTP methods from the Allow header
http_methods=$(echo "$allow_header" | awk -F ": " '{print $2}')

# Display the HTTP methods
echo "$http_methods"

# Clean up the temporary file
rm "$temp_file"
