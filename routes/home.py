#!/ usr/bin/python3
"""
Our Project Flask Routes
"""
from app import app
from db import storage
from flask import render_template, request
from forms.tc_filter import TCFilter


@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
@app.route('/home', methods=['GET', 'POST'], strict_slashes=False)
def home():
    """Render Home page with the transfusion centers filter"""

    tc_filter = TCFilter()
    center = None

    colors = {
        'Stable': 'green',
        'Soon Shortage': 'orange',
        'Critic': 'red'
    }

    if request.method == 'POST':
        center_id = dict(request.form).get('center')
        center = storage.get('TransfusionCenter', center_id)

    return render_template('index.html',
                           title='Home',
                           tc_filter=tc_filter,
                           colors=colors,
                           center=center)
