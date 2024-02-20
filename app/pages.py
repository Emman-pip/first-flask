from flask import Blueprint, render_template
from sqlalchemy import select
from sqlalchemy.sql import func
import app

bp = Blueprint('pages', __name__)

@bp.route('/')
def home():
    return render_template('pages/home.html')

@bp.route('/missions')
def mission():
    data = app.missions.query.all()
    # TODO: LEARN HOW TO QUERY LIKE THIS
    data2 = app.db.session.query(app.missions.operator, func.count(app.missions.missionID)).group_by(app.missions.operator).all()
    labels = [i[0] for i in data2]
    numbers = [i[1] for i in data2]
    # data2 = app.db.session.execute(app.db.select(app.missions.operator, app.db.func.count(app.missions.operator).label("Times_sent_to_moon")).order_by(app.missions.operator)).scalars()
    # data2 = app.db.session.execute(app.db.select(app.missions)).scalar()
    # data = app.missions.query.group_by(app.missions.operator).order_by(func.count(app.missions.operator)).all()
    return render_template('pages/missions.html', missions=data, countries=labels, data=numbers)
