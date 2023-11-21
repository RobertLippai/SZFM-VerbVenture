# We will place the endpoints here
# ex. landing page, dictionary etc...
from sqlite3 import IntegrityError
from flask import Blueprint, jsonify, render_template
from flask_login import current_user, login_required

from webapp.progress_handler import calculate_scores, get_grade
from .models import Word
from . import db  # imports from __init__.py
import json
from sqlalchemy import exc

views = Blueprint("views", __name__)


# Landing Page
# Access it like this: (url_for('views.landing_page'))
@views.route("/home")
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
    return jsonify(data)


@views.route("/word_cards")
@login_required
def word_cards():
    words = ["dog", "you", "did", "yes", "but", "never", "far", "apple"]
    return render_template("szokartya.html", user=current_user, words=words)


@views.route("/words_pair")
@login_required
def words_pair():
    leftWords = ["kutya", "láb", "betű", "háború", "víz", "ló", "állat", "igazság"]
    rightWords = ["dog", "leg", "word", "war", "water", "horse", "animal", "truth"]

    return render_template('szoparosit.html', user=current_user, leftWords=leftWords, rightWords=rightWords)


@views.route("/complete_it")
@login_required
def complete_it():
    return render_template('complete_it.html', user=current_user)


from .fill_db import fill_word_table, query_word_table


@views.route("/fillWordTable")
def filll():
    fill_word_table(db, Word)
    return "ok"


@views.route("/dropWordTable")
def dropT():
    Word.__table__.drop(db.engine)
    return "ok"


@views.route("/add_word/<eng>/<hun>")
def add_word(eng, hun):
    newWord = Word(
        english_word=eng,
        hungarian_word=hun
    )

    try:
        db.session.add(newWord)
        db.session.commit()
        return jsonify(str("Word has been added to the DB: " + eng + " " + hun))
    except exc.IntegrityError:
        return jsonify("Unique constraint failed!")
    except:
        return jsonify("There was an error.")


@views.route("/getWords")
@login_required
def getWords():
    words = Word.query.all()
    for word in words:
        print(word.english_word + " " + word.hungarian_word)

    return jsonify(w=[word.serialize() for word in words])


@views.route("/getWords/<filterBy>")
@login_required
def getWordByEng(filterBy):
    words = Word.query.filter_by(
        english_word=filterBy
    ).all()

    for word in words:
        print(word.english_word + " " + word.hungarian_word)

    return jsonify(w=[word.serialize() for word in words])


@views.route("/dictionary")
@login_required
def dictionary():
    words = Word.query.all()
    for word in words:
        print(word.english_word + " " + word.hungarian_word)

    return render_template('dictionary.html', user=current_user)


