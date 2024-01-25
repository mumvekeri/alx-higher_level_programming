#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request with a custom header
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
