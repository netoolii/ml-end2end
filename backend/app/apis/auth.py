from flask import Blueprint, request, session
from flask_restx import Api, Resource
from handlers.auth import AuthHandler
from helpers.commom import set_session


auth_bp = Blueprint("auth", __name__)
auth_api = Api(auth_bp,
               version="V1",
               title="Auth")


@auth_api.route("/auth/login")
class AuthLogin(Resource):

    def post(self):
        username = request.json['username']
        password = request.json['password']

        user = AuthHandler.auth_login(username=username, password=password)
        if user is not None:
            set_session(session=session, current_user=user.to_json())
            # session['current_user'] = user.to_json()
            # session['current_conversation'] = {}
            # session['current_conversation_context'] = []
            return {"message": "login success", "user": user.to_json()}, 200
        return {"message": "invalid credentials"}, 401


@auth_api.route("/auth/logout")
class AuthLogout(Resource):

    def post(self):
        session.clear()
        [session.pop(key) for key in list(session.keys())]
        return {"message": "logout success"}, 200
