import time

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

# Initializing the database
db = SQLAlchemy()
DB_NAME = "database.db" # creates the db where the  __init__.py is located


# Initializing the web app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '6r4r94rjnfs knfkjwenf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # path of the database
    db.init_app(app) #  initializing the database with our application

    # Importing and registering the endpoints
    from .views import views
    from .auth import auth
    from .settings import settings
    from .fill_db import init_blueprint

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(settings, url_prefix='/')
    app.register_blueprint(init_blueprint, url_prefix='/')

    from .models import User, Word, Category #  relative import
    from .fill_db import initialize_database

    with app.app_context():
        db.create_all()
        Category.__table__.drop(db.engine)
        Word.__table__.drop(db.engine)
        time.sleep(2)
        initialize_database()

    login_manager = LoginManager()
    # Where to redirect the user if he isn't logged in
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Ennek az oldalnak az eléréséhez be kell jelentkezned!'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        #return User.find_user_by_id(int(id), load_users_from_file())
        return User.query.get(int(id)) # get similar to filterby, but searches for primary key

    return app