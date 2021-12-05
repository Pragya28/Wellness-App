"""
    Defines the model of the database and tables used
"""

from datetime import date
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash

from .calculations import calculate_bmi, calculate_bmr, word_count_score
from . import db

class User(db.Model, UserMixin):
    """
        Defines the structure of User table
    """

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
        """
            Constructor for User
        """

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

    def update_profile(self, fullname, gender, age, height, weight, lifestyle):
        """
            Updates the User details
        """

        self.fullname = fullname
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.lifestyle = lifestyle
        self.bmi = calculate_bmi(height, weight)
        self.bmr = calculate_bmr(height, weight, age, gender)


class CalorieData(db.Model):
    """
        Defines the calorie data for activities performed by the user
    """

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date)
    exercise = db.Column(db.String(20))
    duration = db.Column(db.Integer)
    calories = db.Column(db.Integer)

    def __init__(self, exercise, duration, calories):
        """
            Constructor for calorie data
        """

        self.user_id = current_user.id
        self.date = date.today()
        self.exercise = exercise
        self.duration = duration
        self.calories = calories

class FoodData(db.Model):
    """
        Defines data related to food consumed by user
    """

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date)
    fooditem = db.Column(db.String(20))
    calories = db.Column(db.Integer)

    def __init__(self, fooditem, calories):
        """
            Constructor for food data
        """

        self.user_id = current_user.id
        self.date = date.today()
        self.fooditem = fooditem
        self.calories = calories


class Data(db.Model):
    """
        Defines all the details required to calculate user wellness
    """

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
        """
            Constructor for data
        """

        self.user_id = user_id
        self.date = date.today()
        self.wellness = current_user.wellness

    def add_calorie(self, calorie):
        """Add calorie information to data"""

        self.calorie = calorie

    def add_sleep(self, sleep):
        """Add sleep information to data"""

        self.sleep = sleep

    def add_water(self, water):
        """Add water information to data"""

        self.water = water

    def add_nutrition(self, nutrition):
        """Add nutrition information to data"""

        self.nutrition = nutrition

    def add_activity(self, activity, activity_rating):
        """Add activity information to data"""

        self.activity = activity
        self.activity_rating = activity_rating

    def add_learning(self, learning, learning_rating):
        """Add learning information to data"""

        self.learning = learning
        self.learning_rating = learning_rating

    def calculate_wellness(self):
        """Calculates wellness using all the data available"""

        days = (date.today()-current_user.join_date).days
        well = current_user.wellness * (days)

        if current_user.bmi >= 18.5 and current_user.bmi < 25:
            bmi_score = 10
        else:
            if current_user.bmi < 18.5:
                limit = 18.5
            else:
                limit = 25
            bmi_score = abs(current_user.bmi - limit)/limit * 10

        lifestyles = {
            "sedantary" : 1.2,
            "slightly-active" : 1.375,
            "moderately-active" : 1.55,
            "active" : 1.725,
            "very-active" : 1.9
            }

        if current_user:
            net_cal = current_user.bmr*lifestyles[current_user.lifestyle]
        else:
            net_cal = 0

        print(net_cal, self.calorie, self.nutrition)
        cal_score = abs(net_cal+self.calorie-self.nutrition)/current_user.bmr * 40

        sleep_score = abs(self.sleep-420)/420 * 10
        if current_user.gender == 'male':
            water_score = abs(self.water-3.7)/3.7 * 10
        else:
            water_score = abs(self.water-2.7)/2.7 * 10

        activity_score = self.activity_rating*2 + word_count_score(self.activity)
        learning_score = self.learning_rating*2 + word_count_score(self.learning)

        well += bmi_score + cal_score + sleep_score + water_score + activity_score + learning_score
        well /= (days+1)
        well = round(well, 2)
        self.wellness = well
        current_user.wellness = well
        