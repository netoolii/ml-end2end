from flask import Blueprint, session
from flask_restx import Api, Resource
from handlers.conversation import ConversationHandler


conversation_bp = Blueprint("conversation", __name__)
conversation_api = Api(conversation_bp, version="V1", title="Conversation")


@conversation_bp.before_request
def check_user():
    user = session.get('current_user', None)
    if user is None:
        return {"message": "invalid credentials"}, 401


@conversation_api.route("/conversation/")
@conversation_api.route("/conversation/<id_conversation>")
class Conversation(Resource):
    def post(self):
        print("inside post conversation")
        conversation = ConversationHandler.create(session.get('current_user'))
        if conversation is not None:
            session['current_conversation'] = conversation.to_json()
            session['current_conversation_context'] = []
            return {"message": "successfully registered", 'data': conversation.to_json()}, 201
        return {'message': 'unable to create', 'data': {}}, 500

    def get(self, id_conversation):
        conversation = ConversationHandler.get_one(id_conversation)
        if conversation is not None:
            session['current_conversation'] = conversation.to_json()
            session['current_conversation_context'] = []
            return {"message": "successfully got", 'data': conversation.to_json()}, 200
        return {'message': 'unable to access', 'data': {}}, 500

    def patch(self, id_conversation):
        conversation = ConversationHandler.delete_one(id_conversation, session.get('current_user'))
        if conversation is not None:
            session['current_conversation'] = {}
            session['current_conversation_context'] = []
            return {"message": "successfully deleted"}, 200
        return {'message': 'unable to access', 'data': {}}, 500


@conversation_api.route("/conversation/list")
class ConversationList(Resource):

    def get(self):
        conversation = ConversationHandler.get_list()
        if conversation is not None:
            _conversation = [_conversation.to_json() for _conversation in conversation]
            return {"message": "successfully got", "data": _conversation}, 200
        return {'message': 'unable to access', 'data': {}}, 500
