from flask import Blueprint
from flask_restplus import Api, apidoc

from app.api.v1.user import api as user_ns

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(
    api_v1,
    title='UTA API',
    version='1.0',
    description='API to interact with courses and users from UTA webpage.'
)

api.add_namespace(user_ns, path='/users')


@api.documentation
def swagger_ui():
    return apidoc.ui_for(api)
