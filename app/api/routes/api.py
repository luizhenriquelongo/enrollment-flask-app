from flask import Blueprint, jsonify
from flask_restplus import Resource, Api

from app.database.models import User


api_bp = Blueprint('api', __name__)
api = Api(api_bp)


@api.route('/user')
class GetAndPost(Resource):

    def get(self):
        return jsonify(User.objects.all())

    def post(self):
        data = api.payload
        user_data = {
            'user_id': User.objects.count() + 1,
            'email': data['email'],
            'first_name': data['first_name'],
            'last_name': data['last_name']
        }

        user = User(**user_data)
        user.set_password(data['password'])
        user.save()
        return jsonify(user)


@api.route('/user/<id>')
class GetUpdateDelete(Resource):

    def get(self, id):
        return jsonify(User.objects(user_id=id))

    def put(self, id):
        data = api.payload
        User.objects(user_id=id).update(**data)
        return jsonify(User.objects(user_id=id))

    def delete(self, id):
        User.objects(user_id=id).delete()
        return jsonify("User deleted!")
