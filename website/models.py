from . import db
from flask_login import UserMixin
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from .calculations import calculate_bmi
from flask_login import current_user

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
    wellness = db.Column(db.Float, default=0.0)

    def __init__(self, username, email, password, fullname, gender, age, height, weight):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.fullname = fullname
        self.gender = gender 
        self.age = age
        self.height = height
        self.weight = weight
        self.join_date = date.today()
        self.bmi = calculate_bmi(height, weight)


class CalorieData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date)
    exercise = db.Column(db.String(20))
    duration = db.Column(db.Integer)
    calorie = db.Column(db.Integer)

    def __init__(self, exercise, duration, calorie):
        self.user_id = current_user.id
        self.date = date.today()
        self.exercise = exercise
        self.duration = duration
        self.calorie = calorie


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
