from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.sql import func

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('views.start'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        pwd1 = request.form.get('password1')
        pwd2 = request.form.get('password2')
        age = int(request.form.get('age'))
        gender = request.form.get('genderOptions')
        height = int(request.form.get('height'))
        weight = int(request.form.get('weight'))
        userbyusername = User.query.filter_by(username=username).first()
        userbyemail = User.query.filter_by(email=email).first()

        status = False
        if userbyusername:
            message = "Username already exists"
        elif userbyemail:
            message = "This email already has an account"
        elif pwd1 != pwd2:
            message = "Passwords don't match"
        elif len(fullname.split()) < 2:
            message = "Please enter your full name"
        elif age < 0:
            message = "Please enter valid age"
        elif height < 0:
            message = "Please enter valid height"
        elif weight < 0:
            message = "Please enter valid weight"
        elif gender is None:
            message = "Select your gender"
        else:
            user = User(
                username=username, 
                email=email, 
                fullname=fullname, 
                gender=gender,
                age=age, 
                height=height, 
                weight=weight, 
                password=generate_password_hash(pwd1, method='sha256'),
                join_date = func.now()
                )
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            status = True
            message = "Account created!"
        
        if status:
            flash(message, category="success")
            return redirect(url_for('views.home'))
        else:
            flash(message, category="error")
        
    return render_template('signup.html')
