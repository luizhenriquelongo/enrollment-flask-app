from flask import Flask

from config import Config
from app.database.config import start_database
from app.website.routes import site_blueprints
from app.api.routes import api_blueprints


app = Flask(
    __name__,
    template_folder='website/templates',
    static_folder='website/static'
)
app.config.from_object(Config)

# Registering website routes
for site_blueprint in site_blueprints:
    app.register_blueprint(site_blueprint)

# Registering api routes
for api_blueprint in api_blueprints:
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

start_database(app)
