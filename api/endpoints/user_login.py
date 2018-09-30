from flask import jsonify, request
from flask_restplus import Resource
from werkzeug.security import check_password_hash

from api.utils import User, login_schema


class UserLogin(Resource):

    def post(self):
        user_details = request.get_json()
        result, errors = login_schema.load(user_details)

        if errors:
            return jsonify(errors)
        else:
            user = User.query.get_username(result['username']).first()
            if check_password_hash(user.password, user_details['password']):
                token = user.generate_token()
                # gives message response

                return {'token': token,
                            'message': "You have logged in successfully"}, 200
            else:
                return {'error': 'invalid username or password!'}, 400
