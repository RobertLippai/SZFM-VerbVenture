from . import db
from flask_login import UserMixin

class User(db.Model,
           UserMixin):  # a UserMixin csak a felhasználói fiók bejelntkezéshez kell, a flask_login modul miatt!
    id = db.Column(db.Integer, primary_key=True)  # Int type, primary key
    username = db.Column(db.String(150), unique=True)  # Strings needs to have a max length set
    password = db.Column(db.String(150))
    preferred_background = db.Column(db.String(150), default="background_image.jpg")


class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Int type, primary key
    english_word = db.Column(db.String(150))
    hungarian_word = db.Column(db.String(150))

    __table_args__ = (
        db.UniqueConstraint('english_word', 'hungarian_word', name='unique_commit'),
    )

    def serialize(self):
        return {
            'id': self.id,
            'english_word': self.english_word,
            'hunarian_word': self.hungarian_word,
        }