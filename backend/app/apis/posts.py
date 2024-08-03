from flask import Blueprint, request, session
from flask_restx import Api, Resource
from handlers.posts import PostsHandler
from helpers.commom import get_assistant_chat, get_user_chat

posts_bp = Blueprint("posts", __name__)
posts_api = Api(posts_bp,
                version="V1",
                title="Posts")


@posts_bp.before_request
def check_user():
    user = session.get('current_user', None)
    if user is None:
        return {"message": "invalid credentials"}, 401


@posts_api.route("/posts")
class Posts(Resource):

    def post(self):
        prompt = request.json['prompt']
        context = session.get("current_conversation_context", [])
        conversation = session.get('current_conversation', {})
        posts = PostsHandler.create(conversation,
                                    prompt=prompt,
                                    context=context)
        if posts is not None:
            _posts = posts.to_json()
            session['current_conversation_context'].append(
                get_user_chat(_posts.get("prompt", "")))
            session['current_conversation_context'].append(
                get_assistant_chat(_posts.get("body", "")))
            return {"message": "successfully registered",
                    'data': _posts}, 201
        return {'message': 'unable to create', 'data': {}}, 500

    def get(self):
        conversation = session.get('current_conversation', {})
        session['current_conversation_context'] = []
        posts = PostsHandler.get_by_conversation(conversation)
        if posts is not None:
            _posts = [_post.to_json() for _post in posts]
            for post in _posts:
                session['current_conversation_context'].append(
                    get_user_chat(post.get("prompt", "")))
                session['current_conversation_context'].append(
                    get_assistant_chat(post.get("body", "")))
            print(session['current_conversation_context'])
            return {"message": "success", "data": _posts}, 200
        return {'message': 'no posts', 'data': {}}, 400
