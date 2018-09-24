import json
from flask import g
from flask_restplus import Resource

from api.utils import token_required
from api.utils import FavouriteMovies
from sqlalchemy import inspect

class ViewFavouritesList(Resource):


    @token_required
    def get(self):
        favourite_list = []
        favourite_movies = FavouriteMovies.query.get_user(
            g.current_user.user_id).all()

        for movie in favourite_movies:
            favourite_list.append({
                "movie_title": movie.movie_title,
                "description": movie.overview,
                "popularity": movie.popularity
            })
    
        return favourite_list
