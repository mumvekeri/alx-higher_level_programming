#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status """

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print("- Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
except urllib.error.HTTPError as e:
    print("Error fetching the URL:", e)
except urllib.error.URLError as e:
    print("URL error:", e)
