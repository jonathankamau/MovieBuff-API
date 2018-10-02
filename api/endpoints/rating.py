from flask import g, jsonify, request
from flask_restplus import Resource
from api.utils import FavouriteMovies, token_required


class UserMovieRatings(Resource):

    @token_required
    def get(self):
        rating_list = []
        users_ratings = FavouriteMovies.query.filter_by(
                        user_id=g.current_user.id).all()
  
        for rating in users_ratings:

            rating_list.append({
                'movie_title': rating.movie_details.movie_title,
                'movie_id': rating.movie_details.movie_id,
                'movie_rating': rating.ranking_number

            })

        return rating_list

    @token_required
    def post(self):
        movie = request.get_json()
        users_ratings = FavouriteMovies.query.filter_by(
                        user_id=g.current_user.id).all()

        for rating in users_ratings:


            if (rating.movie_details.movie_id == movie['id'] and 
                rating.ranking_number == 0):
                
                rating.ranking_number = movie['rating']

                print(rating.movie_details.movie_id)

                rating.save()
                print(rating.save())

                response = jsonify({
                        'message': 'rating updated successfully!'
                        })

                response.status_code = 201
            else:
                response = jsonify({
                        'message': 'rating could not be updated!'
                        })

                response.status_code = 400
        
        return response

    @token_required
    def put(self):
        movie = request.get_json()

        movie_details = FavouriteMovies.query.filter_by(
            user_id=g.current_user.user_id,
            movie_id=movie['movie_id']).first_or_404()

        movie_details.rating = movie['rating']

        movie_details.save()

        return {"response": "Movie rating updated successfully!"}, 201
