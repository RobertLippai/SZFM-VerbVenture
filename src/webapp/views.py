# We will place the endpoints here
# ex. landing page, dictionary etc...
from flask import Blueprint, jsonify, render_template
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


@views.route("/download-data", methods=["GET"])
@login_required
def download_data():
    scores = calculate_scores(current_user.username)
    (szokirako, szokartyak, egeszitsdki, listening, parositas, sum) = scores
    grade = get_grade(sum)
    data = {
        "Felhasználó": current_user.username,
        "Összesítés": {"Százalék": str(sum) + "%", "Osztályzat": grade},
        "Elért eredmények": {
            "Szókirakó": str(szokirako) + "%",
            "Szókártyák": str(szokartyak) + "%",
            "Egészítsd Ki": str(egeszitsdki) + "%",
            "Listening": str(listening) + "%",
            "Szópárosítás": str(parositas) + "%",
        },
    }
    sortedData = {k: data[k] for k in ["Felhasználó", "Összesítés", "Elért eredmények"]}
    return jsonify(sortedData)
