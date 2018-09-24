from flask import g, request
from flask_restplus import Resource

from api.utils import token_required, FavouriteMovies, User


class UpdateUserDetails(Resource):

    @token_required
    def put(self):
        user_details = request.get_json()

        user = User.query.get_user(g.current_user.user_id).first()

        user.username = user_details['username']

        user.save()

        return {"response": "user updated successfully!"}, 200