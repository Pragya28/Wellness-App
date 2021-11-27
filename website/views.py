from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def start():
    if current_user.is_authenticated:
        return redirect(url_for("views.home"))
    if request.method == "POST":
        if request.form.get("login") == "login":
            return redirect(url_for('auth.login'))
        if request.form.get("signup") == "signup":
            return redirect(url_for('auth.signup'))
    return render_template("index.html", user=current_user)
    
@views.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)

@views.route('/bmi')
@login_required
def bmi():
    bmi = current_user.bmi
    if bmi < 18.5:
        message = "You are underweight"
        category = "error"
    elif bmi < 24.9:
        message = "Your weight is normal"
        category = "success"
    elif bmi < 29.9:
        message = "You are overweight"
        category = "error"
    else:
        message = "You are obese"
        category = "error"
    flash(message, category=category)
    return render_template("bmi.html", user=current_user)

@views.route('/calorie')
@login_required
def calorie():
    return render_template("calorie.html", user=current_user)

@views.route('/sleep')
@login_required
def sleep():
    return render_template("sleep.html", user=current_user)

@views.route('/water')
@login_required
def water():
    return render_template("water.html", user=current_user)

@views.route('/activity')
@login_required
def activity():
    return render_template("activity.html", user=current_user)

@views.route('/learning')
@login_required
def learning():
    return render_template("learning.html", user=current_user)
    