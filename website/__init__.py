from flask import Flask
from os import urandom, path, makedirs


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET KEY'] = urandom(16)
    app.config.from_mapping(
        DATABASE=path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is not None:
        app.config.from_mapping(test_config)

    try:
        makedirs(app.instance_path)
    except OSError:
        pass

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
