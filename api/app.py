#!/usr/bin/python3
""" Flask Application """
from db import storage
from api.maps import blood_map
from os import environ
from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(blood_map)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
