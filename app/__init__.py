from flask import Flask
from .config import Config
from .models import db
from .handlers import blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app
