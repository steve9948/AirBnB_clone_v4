#!/usr/bin/python3
"""
Flask App integrating with Airbnb HTML Template
"""
from flask import Flask, render_template
from models import storage
import uuid

app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

@app.teardown_appcontext
def teardown_db(exception):
    """Closes SQLAlchemy session after each request."""
    storage.close()

@app.route('/0-hbnb/')
def hbnb_filters(the_id=None):
    """Renders a custom template with states, cities, amenities, places, and users."""
    states = {state.name: state for state in storage.all('State').values()}
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = {user.id: f"{user.first_name} {user.last_name}" for user in storage.all('User').values()}
    cache_id = str(uuid.uuid4())
    return render_template('1-hbnb.html', states=states, amens=amens, places=places, users=users, cache_id=cache_id)

if __name__ == "__main__":
    """Runs the Flask app."""
    app.run(host=host, port=port)

