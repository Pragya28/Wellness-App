import pytest
from .auth_functions import signup, login, logout

def test_signup(client, app):
    resp = client.get("/sign-up")
    assert resp.status_code == 200
    assert b"Wellness App" in resp.get_data()
    assert b"Profile" not in resp.get_data()
    assert b"Logout" not in resp.get_data()
    assert b"BMI Calculator" not in resp.get_data()
    assert b"Calorie Counter" not in resp.get_data()
    assert b"Sleeping Hours" not in resp.get_data()
    assert b"Water Intake" not in resp.get_data()
    assert b"Enriching Activity" not in resp.get_data()
    assert b"Learning" not in resp.get_data()
    assert b"Login" in resp.get_data()
    assert b"Sign Up" in resp.get_data()
    assert b'Full Name' in resp.get_data()
    assert b'Email Address' in resp.get_data()
    assert b'Username' in resp.get_data()
    assert b'Password' in resp.get_data()
    assert b'Confirm Password' in resp.get_data()
    assert b'Age' in resp.get_data()
    assert b'Gender' in resp.get_data()
    assert b'Height' in resp.get_data()
    assert b'Weight' in resp.get_data()

    name = app.config["TEST_FULLNAME"]
    username = app.config["TEST_USERNAME"]
    password = app.config["TEST_PASSWORD"]
    email = app.config["TEST_EMAIL"]
    age = app.config["TEST_AGE"]
    gender = app.config["TEST_GENDER"]
    height = app.config["TEST_HEIGHT"]
    weight = app.config["TEST_WEIGHT"]
    

    rv = signup(client, username, name, email, password, f'{password}x', age, gender, height, weight, )
    assert b"Unmatched passwords" in rv.data

    rv = signup(client, username, "Test", email, password, password, age, gender, height, weight)
    assert b"Please enter your full name" in rv.data

    rv = signup(client, username, name, email, password, password, "-1", gender, height, weight)
    assert b"Please enter valid age" in rv.data

    rv = signup(client, username, name, email, password, password, age, gender, "-1", weight)
    assert b"Please enter valid height" in rv.data
    
    rv = signup(client, username, name, email, password, password, age, gender, height, "-1")
    assert b"Please enter valid weight" in rv.data
    
    rv = signup(client, username, name, email, password, password, age, None, height, weight)
    assert b"Select your gender" in rv.data

    rv = signup(client, username, name, email, password, password, age, gender, height, weight)
    assert b"Account created" in rv.data
    logout(client)

    rv = signup(client, username, name, email, password, password, age, gender, height, weight)
    assert b"Username already exists" in rv.data

    rv = signup(client, f'{username}x', name, email, password, password, age, gender, height, weight)
    assert b"This email already has an account" in rv.data

def test_login_logout(client, app):
    resp = client.get("/login")
    assert resp.status_code == 200
    assert b"Wellness App" in resp.get_data()
    assert b"Profile" not in resp.get_data()
    assert b"Logout" not in resp.get_data()
    assert b"BMI Calculator" not in resp.get_data()
    assert b"Calorie Counter" not in resp.get_data()
    assert b"Sleeping Hours" not in resp.get_data()
    assert b"Water Intake" not in resp.get_data()
    assert b"Enriching Activity" not in resp.get_data()
    assert b"Learning" not in resp.get_data()
    assert b"Login" in resp.get_data()
    assert b"Sign Up" in resp.get_data()
    assert b'Username' in resp.get_data()
    assert b'Password' in resp.get_data()

    username = app.config["TEST_USERNAME"]
    password = app.config["TEST_PASSWORD"]

    rv = login(client, f'{username}x', password)
    assert b'Username does not exist' in rv.data

    rv = login(client, username, f'{password}x')
    assert b"Incorrect password" in rv.data

    rv = login(client, username, password)
    assert b"Logged in successfully" in rv.data
    logout(client)
    
    