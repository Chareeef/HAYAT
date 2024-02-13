#!/ usr/bin/python3
"""
Routes to permit the logged in Donor to follow or unfollow a Transfusion Center
"""
from app import app
from db import storage
from db.models.donor import Donor
from flask import abort, redirect, request, url_for
from flask_login import current_user, login_required


@app.route('/follow_center/<string:center_id>', methods=['POST'],
           strict_slashes=False)
@login_required
def follow_center(center_id):
    """Follow the center for the current donor"""
    if not isinstance(current_user, Donor):
        abort(401)

    center = storage.get('TC', center_id)

    if not center:
        abort(404)

    if center not in current_user.followed_centers:
        current_user.followed_centers.append(center)
        storage.commit()

    return redirect(url_for('donor_dashboard'))


@app.route('/unfollow_center/<string:center_id>', methods=['POST'],
           strict_slashes=False)
@login_required
def unfollow_center(center_id):
    """Unfollow the center for the current donor"""
    if not isinstance(current_user, Donor):
        abort(401)

    center = storage.get('TC', center_id)

    if not center:
        abort(404)

    if center in current_user.followed_centers:
        current_user.followed_centers.remove(center)
        storage.commit()

    return redirect(request.referrer)
