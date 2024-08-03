from models.posts import Posts
from database import db
from clients.tinyllama import TinyLlama
from flask import current_app


class PostsHandler:

    def create(conversation, prompt="", context=[]):

        body = TinyLlama(context=context).request(prompt)
        posts = Posts(prompt=prompt,
                      conversation_id=conversation.get('id', None),
                      body=body)
        try:
            db.session.add(posts)
            db.session.commit()
            posts = Posts.query.get(posts.id)
            return posts
        except Exception as e:
            current_app.logger.critical(str(e), exc_info=True)
            return None

    def get_by_conversation(conversation):
        posts = Posts.query.filter(Posts.conversation_id == conversation.
                                   get('id', None)).all()
        if posts:
            return posts
        return None
