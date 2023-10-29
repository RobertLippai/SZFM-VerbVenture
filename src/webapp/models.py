from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin): # a UserMixin csak a felhasználói fiók bejelntkezéshez kell, a flask_login modul miatt!
    id = db.Column(db.Integer, primary_key=True) # Int type, primary key
    username = db.Column(db.String(150), unique=True) # Strings needs to have a max length set
    password = db.Column(db.String(150))
    preferred_background = db.Column(db.String(150), default="background_image.jpg")