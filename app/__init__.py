from flask import Flask

from config import Config
from app.database import db
from app.website.routes import site_blueprints
from app.api.v1 import api


app = Flask(
    __name__,
    template_folder='website/templates',
    static_folder='website/static'
)
app.config.from_object(Config)

# Registering website routes
for site_blueprint in site_blueprints:
    app.register_blueprint(site_blueprint)

api.init_app(app)
db.init_app(app)
