#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Get the URL from the command line argument
url=$1

# Send a GET request using curl with the custom header and save the response body to a temporary file
temp_file=$(mktemp)
curl -s -o "$temp_file" -H "X-School-User-Id: 98" "$url"

# Display the body of the response
cat "$temp_file"

# Clean up the temporary file
rm "$temp_file"
