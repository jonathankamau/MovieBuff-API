from flask import g, request
from flask_restplus import Resource

from api.utils import token_required
from api.utils import FavouriteMovies


class DeleteMovie(Resource):


    @token_required
    def delete(self):
        movie_id = request.args.get('id', type=int)
        
        selected_movie = FavouriteMovies.query.filter_by(
                    user_id=g.current_user.user_id, 
                    movie_id=movie_id).first_or_404()

        movie_name = selected_movie.movie_title

        selected_movie.delete()

        return {"response": "Movie deleted",
                "Movie Title that has been deleted": movie_name}, 200
