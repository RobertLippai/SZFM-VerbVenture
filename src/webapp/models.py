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
    category_name = db.Column(db.String(10), db.ForeignKey('category.english_name'), default="none", nullable=False)

    category = db.relationship('Category', backref='words')

    __table_args__ = (
        db.UniqueConstraint('english_word', 'hungarian_word', name='unique_commit'),
    )

    def serialize(self, filter=""):
        return {
            'id': self.id,
            'english_word': self.english_word,
            'hungarian_word': self.hungarian_word,
            'category': self.category_name,
            'matched_by_category': filter.lower() in [self.category.english_name.lower(), self.category.hungarian_name.lower()] if self.category else False
        }

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    english_name = db.Column(db.String(10), unique=True, nullable=False)
    hungarian_name = db.Column(db.String(10), unique=True, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'english_name': self.english_name,
            'hungarian_name': self.hungarian_name,
        }
