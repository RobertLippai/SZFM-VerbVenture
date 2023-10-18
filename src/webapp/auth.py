# We will place the endpoints here
# This is only used for login, logout, register
from flask import Blueprint, render_template, redirect, url_for, request, flash

auth = Blueprint('auth', __name__)

# Landing Page
# Access it like this: (url_for('views.landing_page'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form.get('userName')
        password = request.form.get('password')
        print(user_name, password)

        flash('Helytelen jelszó, próbáld újra!', category='error')
        flash('Nincs ilyen felhasználó regisztrálva!', category='error')
        flash('Sikeres bejelentkezés!', category='succes')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return redirect(url_for('auth.login'))  # blueprint.function name

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form.get('userName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        print(user_name, password1, password2)

        # Checks
        if len(user_name) < 4:
            flash('A felhasználónévnek legalább 6 karakter hosszúnak kell lennie.', category='error')
        elif password1 != password2:
            flash('A jelszavak nem eggyeznek meg!', category='error')
        elif len(password1) < 7:
            flash('A jelszó legalább 7 karakterből kell, hogy álljon!', category='error')
        else:
            # Register user...
            flash('Sikeres regisztráció!', category='succes')
            #return redirect(url_for('views.landing_page'))
            return redirect(url_for('auth.login'))

    return render_template("register.html")