from flask import Flask

from config import Config
from app.routes import site
from app.routes import api
from app.config import start_database, start_api


app = Flask(__name__)
app.config.from_object(Config)

# Registering site routes
app.register_blueprint(site.login_bp)
app.register_blueprint(site.courses_bp)
app.register_blueprint(site.enrollment_bp)
app.register_blueprint(site.index_bp)
app.register_blueprint(site.user_bp)
app.register_blueprint(site.register_bp)

start_database(app)
start_api(app)
