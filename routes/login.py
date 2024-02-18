#!/ usr/bin/python3
"""
Our Project Flask Routes
"""
from app import app, bcrypt
from db import storage
from db.models.donor import Donor
from db.models.transfusion_center import TransfusionCenter
from flask import flash, render_template, jsonify, redirect, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from forms.login import DonorLoginForm, TCLoginForm


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Login page for both Donor and Transfusion Center"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    tc_form = TCLoginForm()
    donor_form = DonorLoginForm()

    if tc_form.validate_on_submit():
        email = tc_form.email.data.strip()
        password = tc_form.password.data
        tc = storage.session.query(
            TransfusionCenter).filter_by(email=email).first()

        if tc and bcrypt.check_password_hash(tc.password_hash, password):
            login_user(tc)
            flash('Logged in successfully !', 'success')

            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)

            return redirect(url_for('center_dashboard'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')

    elif donor_form.validate_on_submit():
        username = donor_form.username.data.strip()
        donor = storage.session.query(
            Donor).filter_by(username=username).first()

        if donor and bcrypt.check_password_hash(
                donor.password_hash, donor_form.password.data):
            login_user(donor)
            flash('Logged in successfully !', 'success')

            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)

            return redirect(url_for('home'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login.html', title='Login', tc_form=tc_form,
                           donor_form=donor_form)


@app.route('/logout', strict_slashes=False)
@login_required
def logout():
    """ Logout """
    logout_user()
    flash('Successfully logged out.', 'info')
    return redirect(url_for('home'))
