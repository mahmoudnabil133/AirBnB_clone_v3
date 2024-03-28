#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.city import City
from models.review import Review
app = Flask(__name__)

@app.route('/hbnb',  strict_slashes=False)
def hbnb():
    states = storage.all(State)
    amens = storage.all(Amenity)
    places = storage.all(Place)
    users = storage.all(User)
    reviews = storage.all(Review)
    cities = storage.all(City)
    sorted_places = sorted(places.values(), key=lambda x:x.name)
    sorted_states = sorted(states.values(), key=lambda x:x.name)
    sorted_amens = sorted(amens.values(), key=lambda x:x.name)
    sorted_users = sorted(users.values(), key=lambda x:x.first_name)
    sorted_reviews = sorted(reviews.values(), key=lambda x:x.id)
    sorted_cities = sorted(cities.values(), key=lambda x:x.name)
    return render_template('100-hbnb.html', states=sorted_states, amens=sorted_amens, places=sorted_places, users=users, cities=cities, reviews=reviews)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
