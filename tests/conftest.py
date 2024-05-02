import pytest
from app import create_app
from flask_mysqldb import MySQL

@pytest.fixture()
def app():
    app = create_app(testing=True)
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
