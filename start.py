from flask import Flask
import argparse

#argparse

# 1. Create the parser
parser = argparse.ArgumentParser(description="a simple greet")

# 2. Add argument
#parser.add_argument("name", help="the name of the person to greet")
parser.add_argument("flask_port", help="the port to run flask on")

# 3. Parse the arguments
args = parser.parse_args()

#print(f"Hi, {args.name}")







#flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hiii"


if __name__ == "__main__":
    app.run(port=args.flask_port)
