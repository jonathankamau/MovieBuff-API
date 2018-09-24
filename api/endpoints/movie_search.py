import os
import requests
from flask import g, jsonify, request
from flask_restplus import Resource
from api.utils import token_required, set_result_in_cache, User



class MovieSearch(Resource):

    @token_required
    def get(self):
        movie_name = request.args.get('movie_name', type=str)

        if not movie_name:
            return {'error': 'Movie name has not been given!'}
        else:
            movie_details = requests.get('https://api.themoviedb.org/3/search/movie?api_key='+os.getenv('MOVIES_API_KEY')+'&query='+movie_name)
            
            set_result_in_cache(movie_details.json())
        
        return movie_details.json()['results']
