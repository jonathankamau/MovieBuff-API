from flask import Flask, jsonify
from flask_cors import CORS
from flask_restplus import Api
from api.endpoints import (Users, Movies, Categories, UserMovieRatings,
                           Search)
from api.utils.models import db


try:
    from .config import env_configuration
except ImportError:
    from config import env_configuration


def create_app(environment):
    """Factory Method that creates an instance of the app with the given config.
    Args:
        environment (str): Specify the configuration to initilize app with.
    Returns:
        app (Flask): it returns an instance of Flask.
    """
    app = Flask(__name__)
    app.config.from_object(env_configuration[environment])
    db.init_app(app)

    api = Api(
        app=app,
        default='Api',
        default_label="Available Endpoints",
        title='MovieBuff API',
        version='2.0.0',
        description="""MovieBuff Api Endpoint Documentation 📚"""
        )
    # enable cross origin resource sharing
    CORS(app)

    api.add_resource(Users, "/api/v2/auth/<string:operation>",
                     endpoint="user")
    api.add_resource(Movies, "/api/v2/movie", endpoint="movie")

    api.add_resource(Categories, "/api/v2/movie/category",
                     "/api/v2/movie/category/<string:category_id>",
                     endpoint="category")
    api.add_resource(UserMovieRatings, "/api/v2/movie/ratings",
                     endpoint="ratings")
    api.add_resource(Search,
                     "/api/v2/movie/search", endpoint="search")

    # handle default 404 exceptions
    @app.errorhandler(404)
    def resource_not_found(error):
        response = jsonify(dict(
            error='Not found',
            message='The requested URL was not found on the server.'))
        response.status_code = 404
        return response

    # handle default 500 exceptions
    @app.errorhandler(500)
    def internal_server_error(error):
        response = jsonify(dict(
            error='Internal server error',
            message="The server encountered an internal error."))
        response.status_code = 500
        return response

    return app
