from flask_todo.database import db, Base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Todo(Base):
    __tablename__ = 'todos'

    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(10000))
    status = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class TodoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Todo
        include_relationships = True
        load_instance = True

todo_schema = TodoSchema()