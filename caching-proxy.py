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
parser.add_argument("--origin", type=str, default="https://github.com", help="URL of the server to which the requests will be forwarded")


# 3. Parse the arguments
args = parser.parse_args()

PORT = args.port
URL = args.origin









#flask

app = Flask(__name__)


@app.route("/")
@app.route("/<path:subpage>")
def page(subpage=""):
    # Connect to a database file (or create it)
    conn = sqlite3.connect('cache.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Create a table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pages (
        url TEXT,
        response TEXT
        )
    ''')

    # Check cache
    cursor.execute(
        "SELECT * FROM pages WHERE url = ?", 
        (URL + ("" if URL.endswith("/") else "/") + subpage,)
    )

    
    row = cursor.fetchone()

    if row:
        print("X-Cache: HIT")
        return "X-Cache: HIT"
    else:
        print("X-Cache: MISS")
        sub_url = requests.get(URL + ("" if URL.endswith("/") else "/") + subpage)
        cursor.execute(
            "INSERT OR REPLACE INTO pages (url, response) VALUES (?, ?)",
            (URL + ("" if URL.endswith("/") else "/") + subpage, sub_url.text)
        )
        conn.commit()
        return sub_url.text



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
