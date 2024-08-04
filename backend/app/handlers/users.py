from models.conversation import Conversation
from models.posts import Posts
from database import db


class UserHandler:

    def get_prompt_list(user):
        user_list_prompt = db.session.query(Conversation.id, Posts.prompt, Conversation.status).\
                                    join(Posts, Conversation.id == Posts.conversation_id).\
                                    filter(Conversation.user_id == user.get('id')).\
                                    filter(Conversation.status != 'deleted').\
                                    distinct().\
                                    group_by(Conversation.id).\
                                    all()
        if user_list_prompt:
            readable_user_list_prompt = list()
            auxiliar_dict = dict()
            keys = ["id", "prompt", "status"]
            for id_line in range(len(user_list_prompt)):
                for idx in range(len(keys)):
                    auxiliar_dict[keys[idx]] = user_list_prompt[id_line][idx]
                readable_user_list_prompt.append(auxiliar_dict)
                auxiliar_dict = dict()
            return readable_user_list_prompt
        return None
