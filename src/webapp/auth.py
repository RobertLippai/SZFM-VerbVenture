# We will place the endpoints here
# This is only used for login, logout, register
from flask import Blueprint, render_template, redirect, url_for

auth = Blueprint('auth', __name__)

# Landing Page
# Access it like this: (url_for('views.landing_page'))
@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return redirect(url_for('auth.login'))  # blueprint.function name

@auth.route('/register')
def register():
    return render_template("register.html")