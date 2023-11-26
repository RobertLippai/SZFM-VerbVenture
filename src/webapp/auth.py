# We will place the endpoints here
# This is only used for login, logout, register
from bcrypt import checkpw, gensalt, hashpw
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user

from webapp.progress_handler import add_starting_entry_of

from . import db  # imports from __init__.py
from .models import User

auth = Blueprint("auth", __name__)


# Landing Page
# Access it like this: (url_for('views.landing_page'))
@auth.route("/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("views.landing_page"))

    if request.method == "POST":
        user_name = request.form.get("userName")
        password = request.form.get("password")
        print(user_name, password)

        # Check if the user is in the database
        # user = User.find_user_by_username(user_name, user_manager.load_users_from_file())
        user = User.query.filter_by(
            username=user_name
        ).first()  # visszadja az összes felhasználót akinek az az emailje

        if user:
            # Check if the password matches
            if checkpw(password.encode("utf8"), user.password.encode("utf8")):
                # flash('Sikeres bejelentkezés!', category='succes')
                login_user(
                    user, remember=True
                )  # Megjegyzi a bejelentkezést, addig amíg a szerver újra nem indul
                return redirect(
                    url_for("views.landing_page")
                )  # blueprint.function name
            else:
                flash("Hibás felhasználónév vagy jelszó!", category="error")
        else:
            flash("Hibás felhasználónév vagy jelszó!", category="error")

    return render_template("login.html")


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))  # blueprint.function name


@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("views.landing_page"))

    if request.method == "POST":
        user_name = request.form.get("userName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        print(user_name, password1, password2)

        # Check if the user already exists, and other checks
        # user = User.find_user_by_username(user_name, user_manager.load_users_from_file())
        user = User.query.filter_by(
            username=user_name
        ).first()  # returns all the users with the same name

        if user:
            flash("Ez a felhasználónév már használatban van!", category="error")
        # ellenőrzéseket csinálunk
        elif len(user_name) < 4:
            flash(
                "A felhasználónévnek legalább 6 karakter hosszúnak kell lennie.",
                category="error",
            )
        elif password1 != password2:
            flash("A jelszavak nem eggyeznek meg!", category="error")
        elif len(password1) < 7:
            flash(
                "A jelszó legalább 7 karakterből kell, hogy álljon!", category="error"
            )
        else:
            # Register and add to the database
            # new_user = User(9, user_name, hashpw(password1.encode('utf8'), gensalt()).decode())
            new_user = User(
                username=user_name,
                password=hashpw(password1.encode("utf8"), gensalt()).decode(),
            )

            add_starting_entry_of(user_name)

            db.session.add(new_user)
            db.session.commit()
            flash("Sikeres regisztráció!", category="succes")
            # Redirect to home page
            return redirect(url_for("auth.login"))  # blueprint.function name

    return render_template("register.html")
