from flask import jsonify, request
from flask_restplus import Resource
from werkzeug.security import generate_password_hash, check_password_hash


from api.utils import UserDetails, reg_schema, login_schema


class Users(Resource):

    def post(self, operation):
        if operation == 'register':
            user_details = request.get_json()
            result, errors = reg_schema.load(user_details)

            if errors:
                return jsonify(errors)
            else:
                user = UserDetails.query.filter_by(
                    username=result['username']).first()

                if user:
                    return {"message": "User already exists!"}, 400
                else:
                    new_user = UserDetails(firstname=result['first_name'],
                                           lastname=result['last_name'],
                                           username=result['username'],
                                           password=generate_password_hash(
                                           result['password']))

                    new_user.save()
                    return {"response": "user created successfully!"}, 201

        elif operation == 'login':
            user_details = request.get_json()
            result, errors = login_schema.load(user_details)

            if errors:
                return jsonify(errors)
            else:
                user = UserDetails.query.filter_by(
                    username=result['username']).first()
                if check_password_hash(user.password, 
                                       user_details['password']):

                    token = user.generate_token()
                    # gives message response

                    return {'token': token,
                            'message': "You have logged in successfully"
                            }, 200
                else:
                    return {'error': 'invalid username or password!'}, 400


    def put(self):
        user_details = request.get_json()

        user = User.query.filter_by(
            id=g.current_user.id).first_or_404()

        user.username = user_details['username']

        user.save()

        return {"response": "user updated successfully!"}, 201
