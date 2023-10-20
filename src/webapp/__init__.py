from flask import Flask

from .user_manager import *
from flask_login import LoginManager

# Initializing the web app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '6r4r94rjnfs knfkjwenf'

    # Importing and registering the endpoints
    from .views import views
    from .auth import auth
    from .settings import settings

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(settings, url_prefix='/')

    login_manager = LoginManager()
    # Where to redirect the user if he isn't logged in
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Ennek az oldalnak az eléréséhez be kell jelentkezned!'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.find_user_by_id(int(id), load_users_from_file())

    return app

