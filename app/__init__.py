from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASEURI') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class missions(db.Model):
    missionID = db.Column(db.Integer, primary_key=True)
    spacecraft = db.Column(db.String(100), nullable=False)
    launchDate = db.Column(db.DateTime, nullable=False)
    operator = db.Column(db.String(100), nullable=False)
    outcome = db.Column(db.Boolean, nullable=False)
    