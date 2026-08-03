from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hiii"


if __name__ == "__main__":
    app.run(port=3000)
