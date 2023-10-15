from flask import Flask

# Initializing the web app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '6r4r94rjnfs knfkjwenf'

    # Importing and registering the endpoints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
