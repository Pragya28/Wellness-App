from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class CalorieCalculator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('userprofile.id'))
    exercise = db.Column(db.String(50))
    duration = db.Column(db.Integer)
    calories = db.Column(db.Float)

class UserProfile(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    fullname = db.Column(db.String(150))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    join_date = db.Column(db.DateTime(timezone=True), default=func.now)

