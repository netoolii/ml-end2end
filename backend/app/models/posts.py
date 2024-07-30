from models.base_model import BaseModel
from database import db


class Posts(db.Model, BaseModel):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    prompt = db.Column(db.Text(), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    conversation_id = db.Column(db.Integer(),
                                db.ForeignKey('conversation.id'),
                                nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f"""Post(id={self.id}, prompt='{self.prompt[:20]}...',
        conversation_id={self.conversation_id})"""
