from models.conversation import Conversation
from database import db
from flask import current_app


class ConversationHandler:

    def create(user):
        conversation = Conversation(status='online', user_id=user.get('id', None))
        try:
            db.session.add(conversation)
            db.session.commit()
            conversation = Conversation.query.get(conversation.id)
            return conversation
        except Exception as e:
            current_app.logger.critical(str(e), exc_info=True)
            return None

    def get_one(conversation_id):
        conversation = Conversation.query.get(conversation_id)
        if conversation:
            return conversation
        return None

    def get_list():
        conversation = Conversation.query.distinct().all()
        if conversation:
            return conversation
        return None

    def delete_one(conversation_id, user):
        try:
            user_id = user.get('id', None)
            conversation = db.session.query(Conversation).get(conversation_id)
            if (conversation and user_id is not None) and conversation.user_id == user_id:
                conversation.status = 'deleted'
                db.session.commit()
                return conversation
            current_app.logger.critical("trying to delete a conversation from different user", exc_info=True)
        except Exception as e:
            current_app.logger.critical(str(e), exc_info=True)
        return None
