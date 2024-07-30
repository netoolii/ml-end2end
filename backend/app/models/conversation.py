from database import db
from models.base_model import BaseModel


class Conversation(db.Model, BaseModel):
    __tablename__ = 'conversation'
    id = db.Column(db.Integer(), primary_key=True)
    status = db.Column(db.Enum('online', 'deleted'))
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'),
                        nullable=False)
    created_at = db.Column(db.DateTime())

    def __init__(self, status, user_id):
        self.status = status
        self.user_id = user_id

    def __repr__(self):
        return f"""Conversation(id={self.id},
        status='{self.status}', user_id={self.user_id})"""
