from flask import Blueprint, current_app, redirect, request, render_template, flash, url_for
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_todo.module_user.models import User
from flask_todo.database import db_session
import jwt

auth_bp = Blueprint('auth', __name__, url_prefix='/')


@auth_bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            token = jwt.encode(
                {"user_id": user.id},
                current_app.config["SECRET_KEY"],
                algorithm="HS256"
            )
            return render_template('module_home/home.html', user=current_user, token=token)

    return render_template('module_auth/login.html', user=current_user)


@auth_bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        passwordConfirm = request.form.get('passwordConfirm')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists!', category='error')
        else:
            _user = User(
                email=email, password=generate_password_hash(password))
            db_session.add(_user)
            db_session.commit()
            flash('Account created!', category='success')
            return redirect('/login')

    return render_template('module_auth/register.html', user=current_user)


@auth_bp.get('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
