#!/usr/bin/python3
"intro to flask"

from flask import Flask
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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
