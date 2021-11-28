import pytest
from flask import Flask
from flask_login import current_user
from website import create_app
from .test_functions import login


def test_config(app):
    assert create_app("test_config.json").testing
    assert 'dummy' in (app.config['SQLALCHEMY_DATABASE_URI']) 
    assert "test" == app.config['TEST_USERNAME'] 
    

def test_start(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Wellness App" in resp.get_data()
    assert b"Login" in resp.get_data()
    assert b"Sign Up" in resp.get_data()
    assert b"Profile" not in resp.get_data()
    assert b"Logout" not in resp.get_data()
    assert b"BMI Calculator" not in resp.get_data()
    assert b"Calorie Counter" not in resp.get_data()
    assert b"Sleeping Hours" not in resp.get_data()
    assert b"Water Intake" not in resp.get_data()
    assert b"Enriching Activity" not in resp.get_data()
    assert b"Learning" not in resp.get_data()


def test_home(client, app):
    resp = client.get("/home")
    assert resp.status_code != 200
    resp = login(client, app.config['TEST_USERNAME'], app.config['TEST_PASSWORD'])
    assert resp.status_code == 200

    assert b"Wellness App" in resp.get_data()
    assert b"Profile" in resp.get_data()
    assert b"Logout" in resp.get_data()
    assert b"BMI Calculator" in resp.get_data()
    assert b"Calorie Counter" in resp.get_data()
    assert b"Sleeping Hours" in resp.get_data()
    assert b"Water Intake" in resp.get_data()
    assert b"Enriching Activity" in resp.get_data()
    assert b"Learning" in resp.get_data()
    assert b"Login" not in resp.get_data()
    assert b"Sign Up" not in resp.get_data()

    assert app.config['TEST_USERNAME'].encode() in resp.get_data()
        

def test_profile(client, app):
    resp = client.get("/profile")
    assert resp.status_code != 200
    resp = login(client, app.config['TEST_USERNAME'], app.config['TEST_PASSWORD'])
    assert resp.status_code == 200


def test_bmi(client, app):
    resp = client.get("/bmi")
    assert resp.status_code != 200
    resp = login(client, app.config['TEST_USERNAME'], app.config['TEST_PASSWORD'])
    assert resp.status_code == 200


def test_calorie(client, app):
    resp = client.get("/calorie")
    assert resp.status_code != 200
    resp = login(client, app.config['TEST_USERNAME'], app.config['TEST_PASSWORD'])
    assert resp.status_code == 200


def test_sleep(client, app):
    resp = client.get("/sleep")
    assert resp.status_code != 200
    resp = login(client, app.config['TEST_USERNAME'], app.config['TEST_PASSWORD'])
    assert resp.status_code == 200


def test_water(client, app):
    resp = client.get("/water")
    assert resp.status_code != 200
    resp = login(client, app.config['TEST_USERNAME'], app.config['TEST_PASSWORD'])
    assert resp.status_code == 200


def test_activity(client, app):
    resp = client.get("/activity")
    assert resp.status_code != 200
    resp = login(client, app.config['TEST_USERNAME'], app.config['TEST_PASSWORD'])
    assert resp.status_code == 200


def test_learning(client, app):
    resp = client.get("/learning")
    assert resp.status_code != 200
    resp = login(client, app.config['TEST_USERNAME'], app.config['TEST_PASSWORD'])
    assert resp.status_code == 200
