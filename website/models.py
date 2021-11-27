from . import db
from flask_login import UserMixin
from datetime import date

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    fullname = db.Column(db.String(150))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    join_date = db.Column(db.Date)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    bmi = db.Column(db.Float)
    wellness = db.Column(db.Float)

# class CalorieCalculator(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('userprofile.id'))
#     exercise = db.Column(db.String(50))
#     duration = db.Column(db.Integer)
#     calories = db.Column(db.Float)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date)
    calorie = db.Column(db.Float)
    sleep = db.Column(db.Float)
    water = db.Column(db.Float)
    activity = db.Column(db.String(1000))
    activity_rating = db.Column(db.Integer)
    learning = db.Column(db.String(1000))
    learning_rating = db.Column(db.Integer)
