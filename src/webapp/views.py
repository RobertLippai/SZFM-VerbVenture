# We will place the endpoints here
# ex. landing page, dictionary etc...
from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

# Landing Page
# Access it like this: (url_for('views.landing_page'))
@views.route('/')
@login_required
def landing_page():
    return render_template("landing_page.html", user=current_user)

