from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from .forms import LoginForm, RegistrationForm
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user:
            if user.check_password(password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print('Form is valid')
        if form.errors:
            print('Form errors:', form.errors)
            flash('Form validation error: {}'.format(
                form.errors), category='error')
        try:
            user = User(email=form.email.data,
                        name=form.name.data, role=form.role.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash('Registration successful!', category='success')
            return redirect(url_for('views.home'))
        except Exception as e:
            db.session.rollback()
            print('Error:', e)
            flash('Error: ' + str(e), category='error')
    return render_template('register.html', title='Register', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
