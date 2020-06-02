from flask import jsonify
from flask_restplus import Resource, Namespace

from app.database.models import User


api = Namespace('users', description='Users related operations')


@api.route('/')
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


@api.route('/<id>')
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
