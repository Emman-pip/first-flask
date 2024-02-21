from flask import Blueprint, render_template
from sqlalchemy import select, text
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
    
    # data3 = app.db.session.scalars(select(func.extract('year', app.missions.launchDate), func.count(app.missions.missionID)).group_by(func.extract('year',app.missions.launchDate))).all()
    
    # data3 = app.db.session.scalars(select(app.missions.launchDate, func.count(app.missions.missionID), func.extract('year',app.missions.launchDate)).group_by(app.missions.launchDate)).all()
    # data3 = app.db.session.query(app.missions).from_statement(text("SELECT YEAR(launchDate) as years, COUNT(*) as num FROM missions GROUP BY YEAR(launchDate);")).all()
    data3 = app.db.session.query(func.extract('year', app.missions.launchDate).label('years'), func.count().label('num')).group_by(func.extract('year', app.missions.launchDate)).all()
    years = [x.years for x in data3]
    frequency = [x.num for x in data3]
    # years = [x[0] for x in data3]
    # data2 = app.db.session.execute(app.db.select(app.missions.operator, app.db.func.count(app.missions.operator).label("Times_sent_to_moon")).order_by(app.missions.operator)).scalars()
    # data2 = app.db.session.execute(app.db.select(app.missions)).scalar()
    # print(data3)
    # data3 = []
    # data = app.missions.query.group_by(app.missions.operator).order_by(func.count(app.missions.operator)).all()
    return render_template('pages/missions.html', missions=data, countries=labels, data=numbers, years=years, frequency=frequency)

@bp.route('/aboutus')
def aboutUs():
    return render_template('pages/aboutUs.html')
