from flask import g, jsonify, request
from functools import wraps

from api.utils.models import UserDetails

user_details = UserDetails()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        authorization_token = request.headers.get('Authorization')

        if not authorization_token:
            message = "Bad request. Header does not contain " \
                      "authorization token"

            return {"response": message}, 400
        g.current_user = user_details.verify_auth_token(authorization_token)
        if g.current_user in ['Invalid Token!', 'Expired Token!']:
            message = ("You are not authorized to access this page",
                       g.current_user)

            return {"response": message}, 400
        return f(*args, **kwargs)
    return decorated
