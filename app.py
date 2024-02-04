#!/usr/bin/python3
"""Module containing our Flask app"""
from flask import Flask, render_template
# from routes.[...] import *

app = Flask(__name__)


@app.route('/', strict_slashes=False)
@app.route('/home/', strict_slashes=False)
def home():
    """Home route"""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
