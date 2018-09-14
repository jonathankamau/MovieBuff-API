from flask import jsonify, request
from flask_restplus import Resource
from api.models import User
from api.schemas import reg_schema

class CreateAccount(Resource):

    def post(self):
        user_details = request.get_json()
        result, errors = reg_schema.load(user_details)

        if errors:
            return jsonify(errors)
        else:
            user = User.query.get_username(result['username']).first()
            print(user_details['username'])
            if user:
                return {"message": "User already exists!"}, 400
            else:
                new_user = User(first_name=result['first_name'],
                                last_name=result['last_name'],
                                username=result['username'],
                                password=result['password'])

                new_user.save()
                return {"response": "user created successfully!"}, 200
