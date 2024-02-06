#!/usr/bin/python3
""" Flask Application """
from db import storage
from api.maps import blood_map
from os import environ
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(blood_map)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True)
