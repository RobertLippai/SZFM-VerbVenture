# We will place the endpoints here
# ex. landing page, dictionary etc...
import random
from sqlite3 import IntegrityError
from flask_login import current_user, login_required
from flask import Blueprint, jsonify, render_template, flash, request

from webapp.progress_handler import calculate_scores, get_grade, update_score_of_user_of_game
from .models import Word, Category
from . import db  # imports from __init__.py
import json
from sqlalchemy import exc, func

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
    translations = {
        "cat": "macska",
        "dog": "kutya",
        "you": "te",
        "did": "csinálta",
        "yes": "igen",
        "never": "soha",
        "far": "messze",
        "apple": "alma"
    }
    new_translations = {
        "mouse": "egér",
        "blue": "kék",
        "picture": "kép",
        "browser": "kereső",
        "question": "kérdés",
        "pen": "toll",
        "purple": "lila",
        "plant": "növény",
    }
    return render_template("szokartya.html", user=current_user, words=translations.keys(), translations=translations, new_words=new_translations.keys(), new_translations=new_translations)

@views.route("/words_pair")
@login_required
def words_pair():
    words_data = Word.query.order_by(func.random()).limit(16)

    pairs = [{'left': word.hungarian_word, 'right': word.english_word} for word in words_data]

    def shuffle_and_extract(pair_list):
        words_left = [pair['left'] for pair in pair_list]
        words_right = [pair['right'] for pair in pair_list]
        random.shuffle(words_left)
        random.shuffle(words_right)
        return words_left, words_right, pair_list

    main_leftWords, main_rightWords, main_correctPairs = shuffle_and_extract(pairs[:8])
    new_leftWords, new_rightWords, new_correctPairs = shuffle_and_extract(pairs[-8:])

    print(pairs)

    return render_template('szoparosit.html', user=current_user, leftWords=main_leftWords, rightWords=main_rightWords,
                           correctPairs=main_correctPairs, new_leftWords=new_leftWords, new_rightWords=new_rightWords,
                           new_correctPairs=new_correctPairs)

@views.route("/pop_up/<string:text>/<string:game>/<string:wonpoints>/<string:tries>")
@login_required
def popup(text, game, wonpoints, tries):
    print("args ==================", text, game, wonpoints, tries)
    flash(text, 'succes')
    update_score_of_user_of_game(username=current_user.username, game=game, wonpoints=int(wonpoints), tries=int(tries))
    return render_template('popup_window.html', user=current_user)
    
    
@views.route("/complete_it")
@login_required
def complete_it():
    return render_template('complete_it.html', user=current_user)

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

    return jsonify([word.serialize() for word in words])


@views.route("/getWords/<filterBy>")
@login_required
def getWordsByFilter(filterBy):
    filterBy = filterBy.lower()
    words = Word.query.join(Category).filter(
        (Word.english_word.ilike(f"%{filterBy}%")) |
        (Word.hungarian_word.ilike(f"%{filterBy}%")) |
        (Category.english_name == filterBy) |
        (Category.hungarian_name == filterBy)
    ).all()

    return jsonify([word.serialize(filterBy) for word in words])


@views.route("/dictionary")
@login_required
def dictionary():
    words = Word.query.all()
    for word in words:
        print(word.english_word + " " + word.hungarian_word)

    return render_template('dictionary.html', user=current_user)


