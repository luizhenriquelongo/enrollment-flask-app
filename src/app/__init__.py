from os import environ

from flask import Flask

from app.database import db
from app.website.routes import blueprints
from app.api.v1 import api_v1
from config import Config


def create_app():
    app = Flask(
        __name__,
        template_folder='website/templates',
        static_folder='website/static'
    )
    app.config.from_object(Config)
    db.init_app(app)

    # Registering website routes
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    app.register_blueprint(api_v1)

    return app
