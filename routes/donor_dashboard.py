#!/ usr/bin/python3
"""
Our Project Flask Routes
"""
from app import app
from db import storage
from flask import flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required


@app.route('/donor_profile', strict_slashes=False)
@login_required
def donor_profile():
    """Render Donor Profile page"""
    pass
