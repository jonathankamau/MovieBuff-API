import json
from flask import g, jsonify
from flask_restplus import Resource

from api.utils import token_required
from api.utils import FavouriteMovies


class ViewFavouritesList(Resource):

    @token_required
    def get(self):
        favourite_list = []
        favourite_movies = FavouriteMovies.query.filter_by(
            user_id=g.current_user.user_id).all()

        if favourite_movies:
            for movie in favourite_movies:
                favourite_list.append({
                    "id": movie.movie_id,
                    "movie_title": movie.movie_title,
                    "description": movie.overview,
                    "popularity": movie.popularity
                })
                response = jsonify(
                    message='Your movie list has been retrieved successfully',
                    list=favourite_list
                )
                response.status_code = 200
        else:
            response = jsonify(
                    message='Movie list could not be found or is empty!',
                )
            response.status_code = 400

        return response
