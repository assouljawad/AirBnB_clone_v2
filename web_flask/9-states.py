#!/usr/bin/python3
"""cript that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def hello_world():
    states = storage.all(State)
    return render_template('9-states.html', states=states, id=False)


@app.route("/states/<id>", strict_slashes=False)
def hello_world_2(id):
    states = storage.all(State)
    cities = False
    state = ""
    for key, value in states.items():
        if value.id == id:
            cities = states[key].cities
            state = states[key].name
            break
    return render_template('9-states.html', state=state,
                           cities=cities, id=True)
    # return ("render")


@app.teardown_appcontext
def teardown_request(error):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
