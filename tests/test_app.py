import os
import pytest
from app import create_app
from app.models import db

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False
    })

    # Create tables in the temporary database
    with app.app_context():
        db.create_all()

    yield app

    # Clean up after test
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Wild Grill" in response.data

def test_menu_items_exist(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Menu" in response.data 