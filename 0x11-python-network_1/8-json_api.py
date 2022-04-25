#!/usr/bin/python3
"""
Takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    if (len(argv) > 1):
        sq = {"q": argv[1]}
    else:
        sq = {"q": ""}

    x = requests.post("http://0.0.0.0:5000/search_user", data=sq)
    try:
        res = x.json()
        if len(res) == 0:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except Exception:
        print("Not a valid JSON")
