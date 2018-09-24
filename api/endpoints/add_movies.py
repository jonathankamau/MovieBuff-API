from datetime import datetime
from flask import g, jsonify, request
from flask_restplus import Resource

from api.utils import FavouriteMovies, get_data_from_cache, token_required


class AddMovie(Resource):

    @token_required
    def get(self):

        return get_data_from_cache()

    @token_required
    def post(self):
        movie_selection = request.get_json()
        movie_list = get_data_from_cache()

        for movie in movie_list:

            if (movie_selection['id'] == movie['id']):
                existing_movie = FavouriteMovies.query.get_movie(
                    g.current_user.user_id,
                    movie['id']).first()

                if existing_movie:
                    response = jsonify(
                        {'message': 'Movie already exists in favourites list!'})
                    response.status_code = 400

                else:
                    new_movie = FavouriteMovies(
                        user_id=g.current_user.user_id,
                        movie_id=movie['id'],
                        movie_title=movie['title'],
                        popularity=movie['popularity'],
                        release_date=datetime.strptime(
                            movie['release_date'], '%Y-%m-%d'),
                        overview=movie['overview'])

                    try:
                        new_movie.save()
                    except new_movie.DocumentException:
                        response = jsonify(
                            {'message': 'Could not save new movie!'})
                        response.status_code = 400

                    model_object = FavouriteMovies.query.get_movie(
                        g.current_user.user_id, movie['id']).first()

                    response = jsonify({
                        'message': 'Movie added to favourites list!',
                        'movie title': model_object.movie_title
                        })

                    response.status_code = 200

        return response
