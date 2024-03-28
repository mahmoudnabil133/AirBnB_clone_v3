#!/usr/bin/env python3
from flask import Flask, render_template

posts = [
    {
        'title': 'Post1',
        'auther':'mahmoud',
        'content': 'its my berthday happy berthday to me shut shut shut',
        'date': '17/12/2023'
    },
    {
        'title': 'Post2',
        'auther':'Hesham',
        'content': 'good bye ramadan',
        'date': '7/4/2024'
    }
]
app = Flask('--name--')

@app.route('/')
def hello():
    return render_template('home.html', posts=posts)
@app.route('/hoda')
def great():
    return render_template('hoda.html', title='haha this is new title')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
