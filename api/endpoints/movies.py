from datetime import datetime
from flask import g, jsonify, request
from flask_restplus import Resource

from api.utils import (FavouriteMovies, MovieDetails,
                       get_data_from_cache, token_required)


class Movies(Resource):

    @token_required
    def get(self):
        favourite_list = []
        
        favourite_movies = FavouriteMovies.query.filter_by(
            user_id=g.current_user.id).all()

        if favourite_movies:
            for movie in favourite_movies:
                favourite_list.append({
                    "id": movie.movie_details.movie_id,
                    "movie_title": movie.movie_details.movie_title,
                    "description": movie.movie_details.overview,
                    "vote_average": movie.movie_details.vote_average
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

    @token_required
    def post(self):
        movie_selection = request.get_json()
        movie_list = get_data_from_cache()
        
        for movie in movie_list:
            if (movie_selection['id'] == movie['id']):
                existing_movie = MovieDetails.query.filter_by(
                    movie_id=movie['id']).first()

                if existing_movie:
                    user_movie = FavouriteMovies(
                        user_id=g.current_user.id,
                        movie_id=existing_movie.id,
                        ranking_number=None
                    )

                    user_movie.save()

                    return {"message": "Movie added to favourites list!"}, 201

                else:
                    new_movie = MovieDetails(
                        movie_id=movie['id'],
                        movie_title=movie['title'],
                        vote_average=movie['vote_average'],
                        release_date=datetime.strptime(
                            movie['release_date'], '%Y-%m-%d'),
                        overview=movie['overview'])

                    new_movie.save()

                    user_movie = FavouriteMovies(
                        user_id=g.current_user.id,
                        movie_id=new_movie.id,
                        ranking_number=None
                    )
                    user_movie.save()
                    print(user_movie.save())

                    return {"message": "New movie added to both movies and favourites list!"}, 200


    @token_required
    def delete(self):
        movie_id = request.args.get('id', type=int)
        
        favourite_movies = FavouriteMovies.query.filter_by(
                    user_id=g.current_user.id).all()

        for movie in favourite_movies:
            print(movie.movie_details.movie_id)
            
            if movie.movie_details.movie_id == movie_id:
                print(movie.movie_details.movie_id)

                movie_name = movie.movie_details.movie_title

                movie.delete()

                response = jsonify({
                        'message': 'Movie deleted!',
                        'Movie Title that has been deleted': movie_name
                        })

                response.status_code = 200

            else:
                response = jsonify({
                        'message': 'Movie could not be deleted!'
                        })

                response.status_code = 400
        
        return response
