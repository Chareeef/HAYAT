#!/ usr/bin/python3
"""
Our Project Flask Home Routes
"""
from app import app
from db import storage
from flask import redirect, render_template, request, url_for
from flask_login import current_user
from forms.tc_filter import TCFilter


@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
@app.route('/home', methods=['GET', 'POST'], strict_slashes=False)
def home():
    """Render Home page with the transfusion centers filter"""
    if not current_user.is_authenticated and request.path == '/':
        return redirect(url_for('about'))

    tc_filter = TCFilter()
    center = None

    if request.method == 'POST':
        center_id = dict(request.form).get('center')
        center = storage.get('TransfusionCenter', center_id)

    return render_template('index.html',
                           title='Home',
                           tc_filter=tc_filter,
                           center=center)


@app.route('/about', strict_slashes=False)
def about():
    """Render the landing page"""
    return render_template('landing_page.html',
                           title='About')
