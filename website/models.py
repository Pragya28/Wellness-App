from . import db
from flask_login import UserMixin
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from .calculations import calculate_bmi, calculate_bmr, word_count_score
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
    lifestyle = db.Column(db.String(20))
    bmi = db.Column(db.Float)
    bmr = db.Column(db.Float)
    wellness = db.Column(db.Float, default=0.0)

    def __init__(self, username, email, password, fullname, gender, age, height, weight, lifestyle):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.fullname = fullname
        self.gender = gender 
        self.age = age
        self.height = height
        self.weight = weight
        self.lifestyle = lifestyle
        self.join_date = date.today()
        self.bmi = calculate_bmi(height, weight)
        self.bmr = calculate_bmr(height, weight, age, gender)


class CalorieData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date)
    exercise = db.Column(db.String(20))
    duration = db.Column(db.Integer)
    calories = db.Column(db.Integer)

    def __init__(self, exercise, duration, calories):
        self.user_id = current_user.id
        self.date = date.today()
        self.exercise = exercise
        self.duration = duration
        self.calories = calories

class FoodData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date)
    fooditem = db.Column(db.String(20))
    calories = db.Column(db.Integer)

    def __init__(self, fooditem, calories):
        self.user_id = current_user.id
        self.date = date.today()
        self.fooditem = fooditem
        self.calories = calories
        
    

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date)
    calorie = db.Column(db.Integer, default=0)
    sleep = db.Column(db.Integer, default=0)
    water = db.Column(db.Float, default=0.0)
    nutrition = db.Column(db.Integer, default=0)
    activity = db.Column(db.String(1000))
    activity_rating = db.Column(db.Integer,  default=0)
    learning = db.Column(db.String(1000))
    learning_rating = db.Column(db.Integer,  default=0)
    wellness = db.Column(db.Float, default=0.0)

    def __init__(self, user_id):
        self.user_id = user_id
        self.date = date.today()
        self.wellness = current_user.wellness

    def add_calorie(self, calorie):
        self.calorie = calorie

    def add_sleep(self, sleep):
        self.sleep = sleep

    def add_water(self, water):
        self.water = water

    def add_nutrition(self, nutrition):
        self.nutrition = nutrition

    def add_activity(self, activity, activity_rating):
        self.activity = activity
        self.activity_rating = activity_rating

    def add_learning(self, learning, learning_rating):
        self.learning = learning
        self.learning_rating = learning_rating

    def calculate_wellness(self):
        days = (date.today()-current_user.join_date).days
        w = current_user.wellness * (days)

        if current_user.bmi >= 18.5 and current_user.bmi < 25:
            bmi_score = 10
        else:
            if current_user.bmi < 18.5:
                LIMIT = 18.5
            else:
                LIMIT = 25
            bmi_score = abs(current_user.bmi - LIMIT)/LIMIT * 10

        LIFESTYLES = {
            "sedantary" : 1.2, 
            "slightly-active" : 1.375, 
            "moderately-active" : 1.55, 
            "active" : 1.725, 
            "very-active" : 1.9
            }

        net_cal = current_user.bmr*LIFESTYLES[current_user.lifestyle]
        act_cal = net_cal-current_user.bmr

        # print(net_cal, act_cal)
        
        cal_score = abs(net_cal+self.calorie-self.nutrition)/current_user.bmr * 40
        # print(cal_score)

        # calorie_score = abs(net_cal-self.calorie)/net_cal * 20
        # nutrition_score = abs(net_cal-self.nutrition*1000)/net_cal * 20

        sleep_score = abs(self.sleep-420)/420 * 10
        if current_user.gender == 'male':
            water_score = abs(self.water-3.7)/3.7 * 10
        else:
            water_score = abs(self.water-2.7)/2.7 * 10

        activity_score = self.activity_rating*2 + word_count_score(self.activity)
        learning_score = self.learning_rating*2 + word_count_score(self.learning)

        # print(bmi_score, calorie_score, nutrition_score, sleep_score, water_score, activity_score, learning_score)

        w += bmi_score + cal_score + sleep_score + water_score + activity_score + learning_score
        w /= (days+1)
        w = round(w, 2)
        self.wellness = w
        current_user.wellness = w