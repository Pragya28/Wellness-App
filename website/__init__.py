"""
    This is initialization file for flask app website
"""

from os import path, environ, remove, makedirs
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_cors import CORS



db = SQLAlchemy()
csrf = CSRFProtect()
cors = CORS()


def create_app(test_config=None):
    """
        Creates the app
    """

    app = Flask(__name__)

    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
    )

    if test_config is not None:
        app.config.from_file(test_config, load=json.load)
        db_name = app.config["DB_NAME"]
    else:
        app.config["SECRET_KEY"] = environ.get("SECRET_KEY")
        db_name = environ.get("DB_NAME")
        app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_name}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    csrf.init_app(app)
    cors.init_app(app,
        origins=[
            "https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css",
            "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.1/font/bootstrap-icons.css",
            "https://netdna.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css",
            "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        ],
        methods=["GET", "POST"]
    )

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User

    create_database(app, db_name)
    
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app, db_name):
    """
        Creates database for the app if it does not exists
    """

    if not path.exists(f"website/{db_name}"):
        db.create_all(app=app)
        print("Database created")
