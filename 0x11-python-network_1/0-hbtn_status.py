#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urllib package
"""

import urllib.request

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print("- Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print("Error fetching the URL:", e)
    except urllib.error.URLError as e:
        print("URL error:", e)
