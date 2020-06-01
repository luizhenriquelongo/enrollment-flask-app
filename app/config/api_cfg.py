from flask_restplus import Api


api = Api()


def start_api(app):
    api.init_app(app)