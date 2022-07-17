from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

db_session = db.session

class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())


def init_db(app):
    db.init_app(app)

    from flask_todo.module_user.models import User
    from flask_todo.module_todo.models import Todo
    db.create_all(app=app)
    
    print("Created database")
