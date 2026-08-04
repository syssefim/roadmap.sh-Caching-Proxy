from flask import Flask
import argparse, requests

#argparse

# How to use: python3 caching-proxy.py num

# 1. Create the parser
parser = argparse.ArgumentParser(description="caching-proxy")

# 2. Add argument
#parser.add_argument("name", help="the name of the person to greet")
parser.add_argument("--port", type=int, default=3000, help="the port to run flask on")
parser.add_argument("--origin", type=str, help="URL of the server to which the requests will be forwarded")


# 3. Parse the arguments
args = parser.parse_args()

#print(f"Hi, {args.name}")







#flask

app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get(args.origin)

    return response.text


if __name__ == "__main__":
    app.run(port=args.port)
