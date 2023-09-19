from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user

# code taken from and modified https://www.programcreek.com/python/example/99647/flask_login.current_user.is_authenticated


def check_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != 'admin':
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('views.home'))
        return f(*args, **kwargs)
    return decorated_function
