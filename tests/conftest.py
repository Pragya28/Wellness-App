import pytest
import json
from website import create_app

@pytest.fixture
def app():
    app = create_app("../tests/test_config.json")
    return app

@pytest.fixture
def client(app):
    return app.test_client()