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
parser.add_argument("--origin", type=str, default="https://github.com/syssefim", help="URL of the server to which the requests will be forwarded")


# 3. Parse the arguments
args = parser.parse_args()

PORT = args.port
URL = args.origin



#redis

# # 1. Connect to Redis
# r = redis.Redis(host='localhost', port=6379, db=0)

# def get_response(url=""):
#     cache_key = URL + url

#     # 2. Check the Cache
#     cached_data = r.get(cache_key)
    
#     if cached_data:
#         print("✅ X-Cache: HIT")
#         return json.loads(cached_data)
        
#     print("❌ X-Cache: MISS")

#     response = requests.get(args.origin)
#     response_data = response.text

#     r.set(cache_key, json.dumps(user_data), ex=86400)

#     return response_data


#flask

app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get(URL)

    return response.text

@app.route("/<path:subpage>")
def subpage(subpage):
    sub_url = requests.get(URL + "/" + subpage)
    return sub_url.text



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
