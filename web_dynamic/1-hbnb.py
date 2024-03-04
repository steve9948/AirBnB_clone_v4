#!/usr/bin/python3
"""
Flask App integrating with AirBnB HTML Template
"""
from flask import Flask, render_template
from models import storage
import uuid

# Flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

# Teardown function to close SQLAlchemy session after each request
@app.teardown_appcontext
def teardown_db(exception):
    """Closes the SQLAlchemy Session after each request."""
    storage.close()

# Route for rendering a custom template with data from the database
@app.route('/1-hbnb/')
def hbnb_filters(the_id=None):
    """Handles requests to a custom template."""
    state_objs = storage.all('State').values()
    states = {state.name: state for state in state_objs}
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = {user.id: f"{user.first_name} {user.last_name}" for user in storage.all('User').values()}
    cache_id = str(uuid.uuid4())
    return render_template('1-hbnb.html', states=states, amens=amens, places=places, users=users, cache_id=cache_id)

# Main function to run the Flask app
if __name__ == "__main__":
    """Runs the Flask app."""
    app.run(host=host, port=port)

