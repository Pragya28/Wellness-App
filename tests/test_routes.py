import pytest
from flask import Flask
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_start(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Wellness App" in resp.get_data()
    assert b"Login" in resp.get_data()
    assert b"Sign Up" in resp.get_data()
    # assert b"Profile" not in resp.get_data()
    # assert b"Logout" not in resp.get_data()
    # assert b"BMI Calculator" not in resp.get_data()
    # assert b"Calorie Counter" not in resp.get_data()
    # assert b"Sleeping Hours" not in resp.get_data()
    # assert b"Water Intake" not in resp.get_data()
    # assert b"Enriching Activity" not in resp.get_data()
    # assert b"Learning" not in resp.get_data()


def test_home(client):
    resp = client.get("/home")
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
    # assert b"Login" not in resp.get_data()
    # assert b"Sign Up" not in resp.get_data()


def test_profile(client):
    resp = client.get("/profile")
    assert resp.status_code == 200


def test_login(client):
    resp = client.get("/login")
    assert resp.status_code == 200
    assert b'Username' in resp.get_data()
    assert b'Password' in resp.get_data()


def test_logout(client):
    resp = client.get("/logout")
    assert resp.status_code == 302 # found but redirected as there is no specific page for logout and it redirects to home page


def test_signup(client):
    resp = client.get("/sign-up")
    assert resp.status_code == 200
    assert b'Full Name' in resp.get_data()
    assert b'Email Address' in resp.get_data()
    assert b'Username' in resp.get_data()
    assert b'Password' in resp.get_data()
    assert b'Confirm Password' in resp.get_data()
    assert b'Gender' in resp.get_data()


def test_bmi(client):
    resp = client.get("/bmi")
    assert resp.status_code == 200


def test_calorie(client):
    resp = client.get("/calorie")
    assert resp.status_code == 200


def test_sleep(client):
    resp = client.get("/sleep")
    assert resp.status_code == 200


def test_water(client):
    resp = client.get("/water")
    assert resp.status_code == 200


def test_activity(client):
    resp = client.get("/activity")
    assert resp.status_code == 200


def test_learning(client):
    resp = client.get("/learning")
    assert resp.status_code == 200

