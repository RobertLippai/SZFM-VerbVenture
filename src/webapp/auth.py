# We will place the endpoints here
# This is only used for login, logout, register
from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import user_manager
from .models import User
from bcrypt import hashpw, checkpw, gensalt
from flask_login import login_user, logout_user, current_user
auth = Blueprint('auth', __name__)

# Landing Page
# Access it like this: (url_for('views.landing_page'))
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.landing_page'))

    if request.method == 'POST':
        user_name = request.form.get('userName')
        password = request.form.get('password')
        print(user_name, password)

        # Check if the user is in the database
        user = User.find_user_by_username(user_name, user_manager.load_users_from_file())

        if user:
            # Check if the password matches
            if checkpw(password.encode('utf8'), user.password.encode('utf8')):
                flash('Sikeres bejelentkezés!', category='succes')
                login_user(user, remember=True) # Megjegyzi a bejelentkezést, addig amíg a szerver újra nem indul
                return redirect(url_for('views.landing_page'))  # blueprint.function name
            else:
                flash('Helytelen jelszó, próbáld újra!', category='error')
        else:
            flash('Nincs ilyen felhasználó regisztrálva!', category='error')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))  # blueprint.function name

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('views.landing_page'))

    if request.method == 'POST':
        user_name = request.form.get('userName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        print(user_name, password1, password2)

        # Check if the user already exists, and other checks
        user = User.find_user_by_username(user_name, user_manager.load_users_from_file())

        if user:
            flash('Email already in use!', category='error')
        # ellenőrzéseket csinálunk
        elif len(user_name) < 4:
            flash('A felhasználónévnek legalább 6 karakter hosszúnak kell lennie.', category='error')
        elif password1 != password2:
            flash('A jelszavak nem eggyeznek meg!', category='error')
        elif len(password1) < 7:
            flash('A jelszó legalább 7 karakterből kell, hogy álljon!', category='error')
        else:
            # Register and add to the database
            new_user = User(9, user_name, hashpw(password1.encode('utf8'), gensalt()).decode())
            user_manager.add_user_to_file(new_user)
            login_user(new_user, remember=True)  # Bejelnetkezteti a felhasználót a regisztrálás után
            flash('Sikeres regisztráció!', category='succes')
            # Redirect to home page
            return redirect(url_for('views.landing_page')) # blueprint.function name


    return render_template("register.html")