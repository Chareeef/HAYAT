#!/usr/bin/python3
"""Module containing our Flask app"""
from flask import Flask
from routes.routes import *  # Not sure

app = Flask(__name__)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
