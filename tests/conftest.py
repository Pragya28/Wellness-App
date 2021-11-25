import pytest

from website import create_app

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///dummy.db'
    })
    return app

@pytest.fixture
def client(app):
    return app.test_client()