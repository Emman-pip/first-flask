from flask import Blueprint, render_template
import app

bp = Blueprint('pages', __name__)

@bp.route('/')
def home():
    return render_template('pages/home.html')

@bp.route('/missions')
def mission():
    data = app.missions.query.all()
    return render_template('pages/missions.html', missions=data)
