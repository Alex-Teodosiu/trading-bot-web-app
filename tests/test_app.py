import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Welcome to the Automated Trading Bot' in rv.data

def test_invalid_page(client):
    """Test a page that does not exist."""
    rv = client.get('/invalid_page')
    assert rv.status_code == 404
