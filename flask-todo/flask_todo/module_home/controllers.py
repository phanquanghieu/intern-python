from flask import Blueprint, redirect, request, render_template
from flask_login import login_required, current_user

home_bp = Blueprint('home', __name__)


@home_bp.get('/')
@login_required
def home():
    print(current_user.email)
    return render_template('module_home/home.html', user=current_user)
