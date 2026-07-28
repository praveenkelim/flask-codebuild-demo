from flask import Flask
from calculator import add

app = Flask(__name__)

@app.route("/")
def home():
    return "AWS CodeBuild Demo"

@app.route("/add/<int:a>/<int:b>")
def addition(a, b):
    return str(add(a, b))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)