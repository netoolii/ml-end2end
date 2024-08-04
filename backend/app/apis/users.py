from flask import Blueprint, session
from flask_restx import Api, Resource
from handlers.users import UserHandler

user_bp = Blueprint("user", __name__)
user_api = Api(user_bp,
               version="V1",
               title="User")


@user_bp.before_request
def check_user():
    user = session.get('current_user', None)
    if user is None:
        return {"message": "invalid credentials"}, 401


@user_api.route("/user/list")
class User(Resource):

    def get(self):
        user = session.get('current_user', None)
        user_list = UserHandler.get_prompt_list(user=user)
        if user_list is not None:
            return {"message": "success", "user_list": user_list}, 200
        return {"message": "No posts"}, 200
