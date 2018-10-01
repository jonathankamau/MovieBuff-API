from flask import jsonify, request
from flask_restplus import Resource
from werkzeug.security import generate_password_hash


from api.utils import User, reg_schema


class CreateAccount(Resource):

    def post(self):
        user_details = request.get_json()
        result, errors = reg_schema.load(user_details)

        if errors:
            return jsonify(errors)
        else:
            user = User.query.filter_by(username=result['username']).first()

            if user:
                return {"message": "User already exists!"}, 400
            else:
                new_user = User(firstname=result['first_name'],
                                lastname=result['last_name'],
                                username=result['username'],
                                password=generate_password_hash(
                                                    result['password']))

                new_user.save()
                return {"response": "user created successfully!"}, 201
