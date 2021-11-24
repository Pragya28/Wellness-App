import pytest
from flask import Flask
from app import app


@pytest.fixture
def client():
    print(app.test_client())
    return app.test_client()


def test_start(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_start(client):
    resp = client.get("/home")
    assert resp.status_code == 200


def test_start(client):
    resp = client.get("/profile")
    assert resp.status_code == 200


def test_start(client):
    resp = client.get("/login")
    assert resp.status_code == 200


def test_start(client):
    resp = client.get("/logout")
    assert resp.status_code == 200


def test_start(client):
    resp = client.get("/sign-up")
    assert resp.status_code == 200


def test_start(client):
    resp = client.get("/bmi")
    assert resp.status_code == 200


def test_start(client):
    resp = client.get("/calorie")
    assert resp.status_code == 200


def test_start(client):
    resp = client.get("/sleep")
    assert resp.status_code == 200


def test_start(client):
    resp = client.get("/water")
    assert resp.status_code == 200


def test_start(client):
    resp = client.get("/activity")
    assert resp.status_code == 200


def test_start(client):
    resp = client.get("/learning")
    assert resp.status_code == 200
