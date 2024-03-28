#!/usr/bin/python3
"intro to flask"

from flask import Flask, render_template
app = Flask(__name__)


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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    "try this"
    return (render_template('5-number.html', number=int(n)))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_even(n):
    """ num_odd_even method: display a HTML page only if n is an integer
        route /number_odd_or_even with the integer n """
    return (render_template('6-number_odd_or_even.html', n=n))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
