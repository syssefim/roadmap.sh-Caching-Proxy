#!/usr/bin/env python3
from flask import Flask
import argparse, requests, sqlite3, sys, os

#global variable(s)
CACHE_DB_NAME = "cache.db"
PORT = 3000 # default port
URL = "https://github.com/" #default origin

def main():
    global PORT, URL

    #argparse

    # 1. Create the parser
    parser = argparse.ArgumentParser(description="caching-proxy")

    # 2. Add the arguments
    parser.add_argument(
        "--port",
        type=int,
        default=None,
        help="Port on which the proxy server will run"
    )

    parser.add_argument(
        "--origin",
        type=str,
        default=None,
        help="The origin URL to forward requests to"
    )

    parser.add_argument(
        "--clear-cache",
        action="store_true",
        help="Clear the cache database"
    )

    # 3. Parse the arguments
    args = parser.parse_args()

    # 4. Handle the input logic
    if args.clear_cache:
        if args.port is not None or args.origin is not None:
            parser.error("--clear-cache cannot be used with --port or --origin")

        print("Clearing proxy db cache...")

        if os.path.exists(CACHE_DB_NAME):
            os.remove(CACHE_DB_NAME)

        sys.exit()
    else:
        PORT = args.port if args.port is not None else PORT
        URL = args.origin if args.origin is not None else URL 
        app.run(port=PORT)











#flask + sqlite

app = Flask(__name__)


@app.route("/")
@app.route("/<path:subpage>")
def page(subpage=""):
    # Connect to a database file (or create it)
    conn = sqlite3.connect(CACHE_DB_NAME)

    conn.row_factory = sqlite3.Row

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Create a table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pages (
        url TEXT PRIMARY KEY,
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
        return row["response"]
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
    main()