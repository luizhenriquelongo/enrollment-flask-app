from flask import Flask

from config import Config
from app.routes import site, api
from app.config import start_database


app = Flask(__name__)
app.config.from_object(Config)

# Registering site routes
app.register_blueprint(site.login_bp)
app.register_blueprint(site.courses_bp)
app.register_blueprint(site.enrollment_bp)
app.register_blueprint(site.index_bp)
app.register_blueprint(site.user_bp)
app.register_blueprint(site.register_bp)
app.register_blueprint(api.blueprint, url_prefix='/api/v1')

start_database(app)
