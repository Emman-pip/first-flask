from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime, Boolean 
import os
from dotenv import load_dotenv

from app import pages

load_dotenv()

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABSEURIONLINE') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(pages.bp)

db.init_app(app)

class missions(db.Model):
    missionID = Column(Integer, primary_key=True)
    spacecraft = Column(String(100), nullable=False)
    launchDate = Column(DateTime, nullable=False)
    operator = Column(String(100), nullable=False)
    outcome = Column(Boolean, nullable=False)
    