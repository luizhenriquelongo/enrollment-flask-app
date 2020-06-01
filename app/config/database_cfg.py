from flask_mongoengine import MongoEngine


db = MongoEngine()


def start_database(app):
    db.init_app(app)
