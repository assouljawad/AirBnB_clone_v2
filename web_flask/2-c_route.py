#!/usr/bin/python3
"""cript that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_world_2():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_world_3(text):
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
