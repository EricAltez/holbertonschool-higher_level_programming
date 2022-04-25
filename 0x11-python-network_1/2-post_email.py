#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv


email = argv[2]
values = {'email': email}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))