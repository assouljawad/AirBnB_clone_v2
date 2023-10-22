#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hello_world():
    """"/hbnb_filters: display a HTML page 10-hbnb_filters.html"""
    states = storage.all(State)
    amenity = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states,
                           amenity=amenity)


@app.teardown_appcontext
def teardown_request(error):
    """remove the current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
