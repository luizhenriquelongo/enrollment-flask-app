from flask_restplus import Api

from app.api.v1.user import api as user_ns

api = Api(
    title='',
    version='1.0',
    description='',
)

api.add_namespace(user_ns, path='/api/v1/users')
