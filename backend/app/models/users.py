from models.base_model import BaseModel
from database import db


class Users(db.Model, BaseModel):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(36))
    created_at = db.Column(db.DateTime())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"Users(username='{self.username}, id='{self.id}')"
