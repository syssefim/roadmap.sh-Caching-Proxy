from flask import Flask
import argparse, requests

#argparse

# How to use: python3 caching-proxy.py --port <number> --origin <url>
# Example: python3 caching-proxy.py --port 3000 --origin http://dummyjson.com


# 1. Create the parser
parser = argparse.ArgumentParser(description="caching-proxy")   

# 2. Add argument
#parser.add_argument("name", help="the name of the person to greet")
parser.add_argument("--port", type=int, default=3000, help="the port to run flask on")
parser.add_argument("--origin", type=str, help="URL of the server to which the requests will be forwarded")


# 3. Parse the arguments
args = parser.parse_args()







#flask

app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get(args.origin)

    return response.text

@app.route("/<path:subpage>")
def subpage(subpage):
    sub_url = requests.get(args.origin + "/" + subpage)
    return sub_url.text



if __name__ == "__main__":
    app.run(port=args.port)
