from flask import Flask
import argparse, requests, sqlite3

#argparse

# How to use: python3 caching-proxy.py --port <number> --origin <url>
# Example: python3 caching-proxy.py --port 3000 --origin http://dummyjson.com


# 1. Create the parser
parser = argparse.ArgumentParser(description="caching-proxy")   

# 2. Add argument
#parser.add_argument("name", help="the name of the person to greet")
parser.add_argument("--port", type=int, default=3000, help="the port to run flask on")
parser.add_argument("--origin", type=str, default="https://github.com/syssefim", help="URL of the server to which the requests will be forwarded")


# 3. Parse the arguments
args = parser.parse_args()

PORT = args.port
URL = args.origin



#sqlite

# Connect to a database file (or create it)
conn = sqlite3.connect('cache.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table if it doesn't already exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pages (
    origin_url TEXT,
    url_path TEXT,
    headers TEXT,
    body TEXT,
    PRIMARY KEY (origin_url, url_path)
    )
''')



#flask

app = Flask(__name__)

# @app.route("/")
# def home():
#     response = requests.get(URL)

    

#     return response.text

# @app.route("/<path:subpage>")
# def subpage(subpage):
#     sub_url = requests.get(URL + "/" + subpage)
#     return sub_url.text


@app.route("/")
@app.route("/<path:subpage>")
def page(subpage=""):
    response = requests.get(URL)

    sub_url = requests.get(URL + "/" + subpage)
    return sub_url.text



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
