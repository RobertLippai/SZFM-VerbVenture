from flask import Blueprint, jsonify
from .models import Word
from . import db

init_blueprint = Blueprint("init", __name__)

@init_blueprint.route("/init")
def initialize_database():
    db.create_all()

    predefined_words = [
    {"english_word": "cat", "hungarian_word": "macska"},
    {"english_word": "dog", "hungarian_word": "kutya"},
    {"english_word": "house", "hungarian_word": "ház"},
    {"english_word": "tree", "hungarian_word": "fa"},
    {"english_word": "car", "hungarian_word": "autó"},
    {"english_word": "computer", "hungarian_word": "számítógép"},
    {"english_word": "water", "hungarian_word": "víz"},
    {"english_word": "sun", "hungarian_word": "nap"},
    {"english_word": "moon", "hungarian_word": "hold"},
    {"english_word": "friend", "hungarian_word": "barát"},
    {"english_word": "family", "hungarian_word": "család"},
    {"english_word": "food", "hungarian_word": "étel"},
    {"english_word": "love", "hungarian_word": "szeretet"},
    {"english_word": "happy", "hungarian_word": "boldog"},
    {"english_word": "sad", "hungarian_word": "szomorú"},
    {"english_word": "nature", "hungarian_word": "természet"},
    {"english_word": "music", "hungarian_word": "zene"},
    {"english_word": "language", "hungarian_word": "nyelv"},
    {"english_word": "time", "hungarian_word": "idő"},
    {"english_word": "work", "hungarian_word": "munka"},
    {"english_word": "play", "hungarian_word": "játék"},
    {"english_word": "school", "hungarian_word": "iskola"},
    {"english_word": "flower", "hungarian_word": "virág"},
    {"english_word": "beach", "hungarian_word": "strand"},
    {"english_word": "sky", "hungarian_word": "ég"},
    {"english_word": "color", "hungarian_word": "szín"},
    {"english_word": "art", "hungarian_word": "művészet"},
    {"english_word": "city", "hungarian_word": "város"},
    {"english_word": "bird", "hungarian_word": "madár"},
    {"english_word": "home", "hungarian_word": "otthon"},
    {"english_word": "garden", "hungarian_word": "kert"},
    {"english_word": "fire", "hungarian_word": "tűz"},
    {"english_word": "ice cream", "hungarian_word": "fagylalt"},
    {"english_word": "movie", "hungarian_word": "film"},
    {"english_word": "travel", "hungarian_word": "utazás"},
    {"english_word": "history", "hungarian_word": "történelem"},
    {"english_word": "science", "hungarian_word": "tudomány"},
    {"english_word": "holiday", "hungarian_word": "ünnep"},
    {"english_word": "magic", "hungarian_word": "varázslat"},
    {"english_word": "sport", "hungarian_word": "sport"},
    {"english_word": "dream", "hungarian_word": "álom"},
    {"english_word": "money", "hungarian_word": "pénz"},
    {"english_word": "rain", "hungarian_word": "eső"},
    {"english_word": "friendship", "hungarian_word": "barátság"},
    {"english_word": "health", "hungarian_word": "egészség"},
    {"english_word": "book", "hungarian_word": "könyv"},
    {"english_word": "happiness", "hungarian_word": "boldogság"},
    {"english_word": "ocean", "hungarian_word": "óceán"},
    {"english_word": "cloud", "hungarian_word": "felhő"},
    {"english_word": "mirror", "hungarian_word": "tükör"},
    {"english_word": "adventure", "hungarian_word": "kaland"},
    {"english_word": "star", "hungarian_word": "csillag"},
    {"english_word": "hobby", "hungarian_word": "hobbi"},
    {"english_word": "dance", "hungarian_word": "tánc"},
    {"english_word": "peace", "hungarian_word": "béke"},
    {"english_word": "mountain", "hungarian_word": "hegy"},
    {"english_word": "heart", "hungarian_word": "szív"},
    {"english_word": "road", "hungarian_word": "út"},
    {"english_word": "sleep", "hungarian_word": "alvás"},
    ]

    try:
        # Loop through the predefined words and add them to the Word table
        for word_data in predefined_words:
            new_word = Word(**word_data)
            db.session.add(new_word)

        # Commit the changes
        db.session.commit()

        return jsonify({"message": "Database initialized successfully!"})

    except Exception as e:
        # Handle errors if any
        db.session.rollback()
        return jsonify({"error": str(e)})

