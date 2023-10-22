#!/usr/bin/python3
"""cript that starts a Flask web application"""
from flask import Flask, render_template
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


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_world_4(text='is cool'):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def hello_world_5(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def hello_world_6(n):
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def hello_world_7(n):
    text = 'odd'
    if n % 2 == 0:
        text = 'even'
    return render_template('6-number_odd_or_even.html', n=n, text=text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
