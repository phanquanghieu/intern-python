import email
from functools import wraps
from flask import request, abort, current_app
import jwt

from flask_todo.module_user.models import User


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "error": "Unauthorized"
            }, 401
        try:
            payload = jwt.decode(
                token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            user = User.query.filter_by(id=payload['user_id']).first()
            if not user:
                return {
                    "message": "Authentication Token is missing!",
                    "error": "Unauthorized"
                }, 401
        except Exception as e:
            return {
                "error": str(e)
            }, 500
        return f(user, *args, **kwargs)

    return decorated
