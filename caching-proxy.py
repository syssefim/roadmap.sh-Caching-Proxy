from flask import Flask
import argparse
import requests
import json
import os


#argparse

# How to use: python3 caching-proxy.py --port <number> --origin <url>
# Example: python3 caching-proxy.py --port 3000 --origin http://dummyjson.com

# 1. Create the parser
parser = argparse.ArgumentParser(description="caching-proxy")

# 2. Add argument
parser.add_argument("--port", type=int, default=3000, help="the port to run flask on")
parser.add_argument("--origin", type=str, help="URL of the server to which the requests will be forwarded")


# 3. Parse the arguments
args = parser.parse_args()


#cache

CACHE_FILE = 'cache.json'





#flask

app = Flask(__name__)

@app.route("/")
def home():
    with open(CACHE_FILE, 'r') as f:
        data = json.load(f)

    if args.origin in data:
        print('X-Cache: HIT')
        return "hi"
    else:
        print('X-Cache: MISS')

        # Save request to cache

        return url_request.text


@app.route("/<path:subpage>")
def subpage(subpage):
    sub_url = requests.get(args.origin + "/" + subpage)
    return sub_url.text


if __name__ == "__main__":
    url_request = requests.get(args.origin)

    app.run(port=args.port)
