import json
import requests
from datetime import datetime
from flask import jsonify, request
from flask_restplus import Resource

from api.utils.models import FavouriteMovies
from api.utils.cache import get_data_from_cache


class AddMovie(Resource):

    def get(self):

        print(get_data_from_cache())
        return get_data_from_cache()

    def post(self):
        movie_selection = request.get_json()
        print('original', get_data_from_cache())

        for movie in get_data_from_cache():
            if movie['id'] == movie_selection['id']:
                existing_movie = FavouriteMovies.query.get_movie(
                    movie['id']).first()

                if existing_movie:
                    return {"response": "Movie already exists in favourites list!"}

                new_movie = FavouriteMovies(
                    movie_id=movie['id'],
                    movie_title=movie['title'],
                    popularity=movie['popularity'],
                    release_date=datetime.strptime(
                        movie['release_date'], '%Y-%m-%d'),
                    overview=movie['overview'])

                try:
                    new_movie.save()
                except new_movie.DocumentException:
                    return {"response": "Could not save new movie!"}, 400

                model_object = FavouriteMovies.query.get_movie(
                    movie['id']).first()

                return {"response": " Movie added to favourites list!", 
                        "Movie Title added": model_object.movie_title}, 200
            else:
                return {"response": " Could not find movie!"}, 400
