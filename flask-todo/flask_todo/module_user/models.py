from flask_todo.database import db, Base
from flask_login import UserMixin

class User(Base, UserMixin):
    __tablename__ = 'users'

    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255))
    avatar = db.Column(db.String(255))
    todos = db.relationship('Todo')
