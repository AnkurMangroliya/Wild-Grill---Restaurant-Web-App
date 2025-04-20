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
    # Test navbar brand
    assert b"WildGrill" in response.data
    # Test page title
    assert b"<title>WildGrill - Premium Restaurant</title>" in response.data
    # Test contact information
    assert b"123 Restaurant Street" in response.data
    assert b"(555) 123-4567" in response.data
    assert b"info@wildgrill.com" in response.data

def test_menu_items_exist(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Menu" in response.data

def test_static_files_loaded(client):
    response = client.get("/")
    assert response.status_code == 200
    # Test CSS files
    assert b'href="/static/css/style.css"' in response.data
    assert b'bootstrap.min.css' in response.data
    assert b'font-awesome' in response.data
    # Test JS files
    assert b'bootstrap.bundle.min.js' in response.data
    assert b'src="/static/js/main.js"' in response.data 