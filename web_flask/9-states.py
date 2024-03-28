#!/usr/bin/python3
"doc for file"
from flask import Flask, render_template
from models import *
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_cities(id=None):
    "return states"
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    if id:
        id = 'State.' + id
        try:
            sorted_states = states[id]
        except Exception as e:
            pass
    return render_template(
        '9-states.html', states=sorted_states, id=id, dec=states
        )


@app.teardown_appcontext
def close(exception):
    "close"
    storage.close()


if __name__ == '__main__':
    "main doc"
    app.run(debug=True, port='5000', host='0.0.0.0')
