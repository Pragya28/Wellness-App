from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def start():
    if request.method == "POST":
        if request.form.get("login") == "login":
            return redirect(url_for('auth.login'))
        if request.form.get("signup") == "signup":
            return redirect(url_for('auth.signup'))
    return render_template("index.html")

@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/profile')
def profile():
    return render_template("profile.html")

@views.route('/bmi')
def bmi():
    return render_template("bmi.html")

@views.route('/calorie')
def calorie():
    return render_template("calorie.html")

@views.route('/sleep')
def sleep():
    return render_template("sleep.html")

@views.route('/water')
def water():
    return render_template("water.html")

@views.route('/activity')
def activity():
    return render_template("activity.html")

@views.route('/learning')
def learning():
    return render_template("learning.html")
    