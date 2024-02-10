from flask import Blueprint, render_template, url_for

bp = Blueprint('page', __name__)

@bp.route('/')
def home():
    return render_template('pages/home.html')

@bp.route('/about')
def about():
    return render_template('pages/about.html')