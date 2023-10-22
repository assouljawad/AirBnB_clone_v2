#!/usr/bin/python3
"""cript that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def hello_world():
    states = storage.all(State)
    ls = []
    for value in states.values():
        ls.append(value.__dict__)
    ls = sorted(ls, key=lambda x: x['name'])
    return render_template('7-states_list.html', states=ls)


@app.teardown_appcontext
def teardown_request(error):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
