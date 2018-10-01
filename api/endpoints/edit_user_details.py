from flask import g, request
from flask_restplus import Resource

from api.utils import token_required, FavouriteMovies, User


class UpdateUserDetails(Resource):

    @token_required
    def put(self):
        user_details = request.get_json()

        user = User.query.filter_by(
            user_id=g.current_user.user_id).first_or_404()

        user.username = user_details['username']

        user.save()

        return {"response": "user updated successfully!"}, 200