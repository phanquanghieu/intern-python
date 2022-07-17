from flask import Flask
from os import getenv
from dotenv import load_dotenv
from ntpath import join
from posixpath import dirname
from flask_cors import CORS
from flask_todo.module_auth import init_login_manager
from flask_todo.database import init_db


def create_app():
    app = Flask(__name__)
    CORS(app)
    
    load_dotenv(join(dirname(__file__), '.env'))
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv(
        'SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')

    init_db(app)
    init_login_manager(app)

    from flask_todo.module_auth.controllers import auth_bp
    from flask_todo.module_home.controllers import home_bp
    from flask_todo.module_todo.controllers import todo_bp
    app.register_blueprint(auth_bp, url_prefix='/')
    app.register_blueprint(home_bp, url_prefix='/')
    app.register_blueprint(todo_bp, url_prefix='/api/v1')

    return app
