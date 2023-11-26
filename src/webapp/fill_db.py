from flask import Blueprint, jsonify
from .models import Word, Category
from . import db

init_blueprint = Blueprint("init", __name__)

@init_blueprint.route("/init")
def initialize_database():
    db.create_all()

    predefined_categories = [
        {"english_name": "empty", "hungarian_name": "üres"},
        {"english_name": "color", "hungarian_name": "szín"},
        {"english_name": "greeting", "hungarian_name": "köszönés"},
        {"english_name": "food", "hungarian_name": "étel"},
        {"english_name": "animal", "hungarian_name": "állat"},
        {"english_name": "season", "hungarian_name": "évszak"},
        {"english_name": "nature", "hungarian_name": "természet"},
        {"english_name": "winter", "hungarian_name": "tél"},
        {"english_name": "autmn", "hungarian_name": "ősz"},
        {"english_name": "summer", "hungarian_name": "nyár"},
        {"english_name": "spring", "hungarian_name": "tavasz"},
    ]

    predefined_words = [
        {"english_word": "summer", "hungarian_word": "nyár", "category_name": "season"},
        {"english_word": "winter", "hungarian_word": "tél", "category_name": "season"},
        {"english_word": "spring", "hungarian_word": "tavasz", "category_name": "season"},
        {"english_word": "autumn", "hungarian_word": "ősz", "category_name": "season"},

        {"english_word": "snow", "hungarian_word": "hó", "category_name": "winter"},
        {"english_word": "skiing", "hungarian_word": "síelés", "category_name": "winter"},
        {"english_word": "snowman", "hungarian_word": "hóember", "category_name": "winter"},
        {"english_word": "cold", "hungarian_word": "hideg", "category_name": "winter"},
        {"english_word": "fireplace", "hungarian_word": "kandalló", "category_name": "winter"},
        {"english_word": "mittens", "hungarian_word": "kesztyű", "category_name": "winter"},
        {"english_word": "hot cocoa", "hungarian_word": "forró csokoládé", "category_name": "winter"},
        {"english_word": "scarf", "hungarian_word": "sál", "category_name": "winter"},
        {"english_word": "ice skating", "hungarian_word": "korcsolyázás", "category_name": "winter"},

        {"english_word": "leaf", "hungarian_word": "levél", "category_name": "autumn"},
        {"english_word": "harvest", "hungarian_word": "aratás", "category_name": "autumn"},
        {"english_word": "harvest", "hungarian_word": "ősz (UK)", "category_name": "autumn"},
        {"english_word": "pumpkin", "hungarian_word": "tök", "category_name": "autumn"},
        {"english_word": "sweater", "hungarian_word": "pulóver", "category_name": "autumn"},
        {"english_word": "cool", "hungarian_word": "hűvös", "category_name": "autumn"},
        {"english_word": "wind", "hungarian_word": "szél", "category_name": "autumn"},
        {"english_word": "falling leaves", "hungarian_word": "lehulló levelek", "category_name": "autumn"},

        {"english_word": "beach", "hungarian_word": "strand", "category_name": "summer"},
        {"english_word": "sun", "hungarian_word": "nap", "category_name": "summer"},
        {"english_word": "swimming", "hungarian_word": "úszás", "category_name": "summer"},
        {"english_word": "sunglasses", "hungarian_word": "napszemüveg", "category_name": "summer"},
        {"english_word": "sandcastle", "hungarian_word": "homokvár", "category_name": "summer"},
        {"english_word": "vacation", "hungarian_word": "vakáció", "category_name": "summer"},
        {"english_word": "barbecue", "hungarian_word": "grillezés", "category_name": "summer"},
        {"english_word": "sunscreen", "hungarian_word": "naptej", "category_name": "summer"},
        {"english_word": "shorts", "hungarian_word": "rövidnadrág", "category_name": "summer"},

        {"english_word": "flower", "hungarian_word": "virág", "category_name": "spring"},
        {"english_word": "rain", "hungarian_word": "eső", "category_name": "spring"},
        {"english_word": "butterfly", "hungarian_word": "pillangó", "category_name": "spring"},
        {"english_word": "sunshine", "hungarian_word": "napsütés", "category_name": "spring"},
        {"english_word": "blossom", "hungarian_word": "virágzás", "category_name": "spring"},
        {"english_word": "cherry blossom", "hungarian_word": "cseresznyevirág", "category_name": "spring"},
        {"english_word": "warmth", "hungarian_word": "meleg", "category_name": "spring"},
        {"english_word": "gardening", "hungarian_word": "kertészkedés", "category_name": "spring"},
        {"english_word": "picnic", "hungarian_word": "piknik", "category_name": "spring"},

        {"english_word": "cat", "hungarian_word": "macska", "category_name" : "animal"},
        {"english_word": "dog", "hungarian_word": "kutya", "category_name" : "animal"},
        {"english_word": "red", "hungarian_word": "piros", "category_name": "color"},
        {"english_word": "hello", "hungarian_word": "szia", "category_name": "greeting"},
        {"english_word": "pizza", "hungarian_word": "pizza", "category_name": "food"},
        {"english_word": "bird", "hungarian_word": "madár", "category_name": "animal"},
        {"english_word": "green", "hungarian_word": "zöld", "category_name": "color"},
        {"english_word": "goodbye", "hungarian_word": "viszlát", "category_name": "greeting"},
        {"english_word": "apple", "hungarian_word": "alma", "category_name": "food"},
        {"english_word": "elephant", "hungarian_word": "elefánt", "category_name": "animal"},
        {"english_word": "blue", "hungarian_word": "kék", "category_name": "color"},
        {"english_word": "thanks", "hungarian_word": "köszönöm"},
        {"english_word": "pasta", "hungarian_word": "tészta", "category_name": "food"},
        {"english_word": "sunflower", "hungarian_word": "napraforgó", "category_name": "nature"},
        {"english_word": "yellow", "hungarian_word": "sárga", "category_name": "color"},
        {"english_word": "bread", "hungarian_word": "kenyér", "category_name": "food"},
        {"english_word": "purple", "hungarian_word": "lila", "category_name": "color"},
        {"english_word": "cake", "hungarian_word": "torta", "category_name": "food"},
        {"english_word": "food", "hungarian_word": "étel", "category_name": "food"},
        {"english_word": "color", "hungarian_word": "szín"},
        {"english_word": "ice cream", "hungarian_word": "fagylalt", "category_name": "food"},
        {"english_word": "white", "hungarian_word": "fehér", "category_name": "color"},

        {"english_word": "house", "hungarian_word": "ház"},
        {"english_word": "tree", "hungarian_word": "fa"},
        {"english_word": "car", "hungarian_word": "autó"},
        {"english_word": "computer", "hungarian_word": "számítógép"},
        {"english_word": "water", "hungarian_word": "víz"},
        {"english_word": "moon", "hungarian_word": "hold"},
        {"english_word": "friend", "hungarian_word": "barát"},
        {"english_word": "family", "hungarian_word": "család"},
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
        {"english_word": "sky", "hungarian_word": "ég"},
        {"english_word": "art", "hungarian_word": "művészet"},
        {"english_word": "city", "hungarian_word": "város"},
        {"english_word": "home", "hungarian_word": "otthon"},
        {"english_word": "garden", "hungarian_word": "kert"},
        {"english_word": "fire", "hungarian_word": "tűz"},
        {"english_word": "movie", "hungarian_word": "film"},
        {"english_word": "travel", "hungarian_word": "utazás"},
        {"english_word": "history", "hungarian_word": "történelem"},
        {"english_word": "science", "hungarian_word": "tudomány"},
        {"english_word": "holiday", "hungarian_word": "ünnep"},
        {"english_word": "magic", "hungarian_word": "varázslat"},
        {"english_word": "sport", "hungarian_word": "sport"},
        {"english_word": "dream", "hungarian_word": "álom"},
        {"english_word": "money", "hungarian_word": "pénz"},
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
        for category_data in predefined_categories:
            new_category = Category(**category_data)
            db.session.add(new_category)
            print(category_data)

        # Loop through the predefined words and add them to the Word table
        for word_data in predefined_words:
            new_word = Word(**word_data)
            db.session.add(new_word)

        # Commit the changes
        db.session.commit()

        return jsonify({"message": "Database initialized successfully!"})

    except Exception as e:
        # Handle errors if any
        print(e)
        db.session.rollback()
        return jsonify({"error": str(e)})

