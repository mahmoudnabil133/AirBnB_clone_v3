#!/usr/bin/python3
"doc for file"
from flask import Flask, render_template
from models import *
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    "return states"
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def close(exception):
    "close"
    storage.close()


if __name__ == '__main__':
    "main doc"
    app.run(debug=True, port='5000', host='0.0.0.0')
