from flask import Flask, jsonify
from flask_cors import CORS
from api.mongo import mongo

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
    mongo.init_app(app)

    # enable cross origin resource sharing
    CORS(app)

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
