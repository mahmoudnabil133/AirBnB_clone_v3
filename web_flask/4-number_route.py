#!/usr/bin/python3
"intro to flask"

from flask import Flask, abort
app = Flask('--name--')


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def desplay(text):
    new_text = text.replace('_', ' ')
    return f'C {new_text}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text=None):
    if not text:
        new_text = 'is cool'
    else:
        new_text = text.replace('_', ' ')
    return f'Python {new_text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
