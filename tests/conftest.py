import pytest
from app import create_app
from flask_mysqldb import MySQL

# produces a testing app instance
@pytest.fixture()
def app():
    app = create_app(testing=True)
    app.config.update({
        "TESTING": True,
    })
    yield app

# produces a test client for testing
@pytest.fixture()
def client(app):
    return app.test_client()
