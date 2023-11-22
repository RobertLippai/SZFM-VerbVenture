from sqlalchemy import text

def fill_word_table(db, Word):
    english_words = [
        'apple',
        'banana',
        'cat',
        'dog',
        'elephant',
        'flower',
        'guitar',
        'house',
        'ice cream',
        'jazz'
    ]

    hungarian_words = [
        'alma',
        'banán',
        'macska',
        'kutya',
        'elefánt',
        'virág',
        'gitár',
        'ház',
        'fagylalt',
        'dzsessz'
    ]

    data = [{'english_word': eng, 'hungarian_word': hun} for eng, hun in zip(english_words, hungarian_words)]

    with db.session.begin() as session:
        for word_data in data:
            word = Word(**word_data)
            session.add(word)

def query_word_table(db):
    with db.engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM Word"))
        for row in result:
            print(row)
