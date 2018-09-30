from flask import Flask, jsonify
from flask_cors import CORS
from flask_restplus import Api
from api.endpoints import (CreateAccount, UserLogin, MovieSearch,
                           AddMovie, ViewFavouritesList, DeleteMovie,
                           UpdateUserDetails)
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
        default='Api')
    # enable cross origin resource sharing
    CORS(app)

    api.add_resource(CreateAccount, "/api/v1/auth/register",
                     endpoint="register")
    api.add_resource(UserLogin, "/api/v1/auth/login", endpoint="login")
    api.add_resource(MovieSearch, "/api/v1/movie/search", endpoint="search")
    api.add_resource(AddMovie, "/api/v1/movie/add", endpoint="add")
    api.add_resource(ViewFavouritesList,
                     "/api/v1/movie/favourites", endpoint="favourites")
    api.add_resource(DeleteMovie, "/api/v1/movie/delete", endpoint="delete")
    api.add_resource(UpdateUserDetails,
                     "/api/v1/user/update", endpoint="update")

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
