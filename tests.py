import pytest
from flask import Flask
from main import app


@pytest.fixture
def client():
    print(app.test_client())
    return app.test_client()


def test_start(client):
    resp = client.get("/")
    assert resp.status_code == 200
