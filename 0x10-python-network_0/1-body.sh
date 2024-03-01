#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Get the URL from the command line argument
url=$1

# Send a GET request using curl and save the response body to a temporary file
temp_file=$(mktemp)
curl -s -o "$temp_file" -w "%{http_code}" "$url"

# Read the status code from the response
status_code=$(tail -n 1 "$temp_file")

# Check if the status code is 200
if [ "$status_code" -eq 200 ]; then
  # Display the body of the response
  sed '$d' "$temp_file"
fi

# Clean up the temporary file
rm "$temp_file"
