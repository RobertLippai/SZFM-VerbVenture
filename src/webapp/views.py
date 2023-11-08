# We will place the endpoints here
# ex. landing page, dictionary etc...
from flask import Blueprint, render_template
from flask_login import current_user, login_required

from webapp.progress_handler import calculate_scores, get_grade

views = Blueprint("views", __name__)


# Landing Page
# Access it like this: (url_for('views.landing_page'))
@views.route("/")
@login_required
def landing_page():
    return render_template("landing_page.html", user=current_user)


@views.route("/progress")
@login_required
def progress():
    scores = calculate_scores(current_user.username)
    # scores = (10, 20, 30, 40, 50)
    (szokirako, szokartyak, egeszitsdki, listening, parositas, sum) = scores
    grade = get_grade(sum)
    return render_template(
        "elorehaladas.html",
        user=current_user,
        szokirako_score=szokirako,
        szokartyak_score=szokartyak,
        egeszitsdki_score=egeszitsdki,
        listening_score=listening,
        parositas_score=parositas,
        sum_score=sum,
        grade_letter=grade,
    )
