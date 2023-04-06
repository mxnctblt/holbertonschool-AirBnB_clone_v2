#!/usr/bin/python3
# 11. HBNB filters
""" script that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000

Routes:
    /hbnb_filters: HBnB HTML filters page
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.run(debug=True)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ display the main HBnB filters HTML page """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """ remove the current SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
