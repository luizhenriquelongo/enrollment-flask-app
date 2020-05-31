from flask import Flask

from config import Config
from app.routes import (
    login_bp,
    courses_bp,
    enrollment_bp,
    index_bp,
    register_bp,
    user_bp
)
from app.database import start_database


app = Flask(__name__)
app.config.from_object(Config)

# Registering routes
app.register_blueprint(login_bp)
app.register_blueprint(courses_bp)
app.register_blueprint(enrollment_bp)
app.register_blueprint(index_bp)
app.register_blueprint(user_bp)
app.register_blueprint(register_bp)

start_database(app)
