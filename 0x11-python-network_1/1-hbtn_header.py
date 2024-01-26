#!/usr/bin/python3
import urllib.request
import sys

# Check if a URL is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        # Check if the 'X-Request-Id' header is present in the response
        if 'X-Request-Id' in response.headers:
            request_id = response.headers['X-Request-Id']
            print("X-Request-Id:", request_id)
        else:
            print("X-Request-Id not found in the response headers.")
except urllib.error.HTTPError as e:
    print("HTTP Error:", e)
except urllib.error.URLError as e:
    print("URL Error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
