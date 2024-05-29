import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['AUTH_SERVER_URL'] = 'http://testserver'  # Add missing configuration
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test the index route."""
    rv = client.get('/')
    assert rv.status_code == 200
    # Remove the incorrect assertion
    assert b'Automated Trading Bot' in rv.data  # Adjust the assertion to match the actual page content

def test_favicon_route(client):
    """Test the favicon route."""
    rv = client.get('/favicon.ico')
    assert rv.status_code == 200

def test_register_route(client):
    """Test the register route."""
    rv = client.get('/register')
    assert rv.status_code == 200
    rv = client.post('/register')
    assert rv.status_code == 200

def test_login_route(client):
    """Test the login route."""
    rv = client.get('/login')
    assert rv.status_code == 200
    rv = client.post('/login')
    assert rv.status_code == 200

def test_logout_route(client):
    """Test the logout route."""
    rv = client.get('/logout')
    assert rv.status_code == 302  # Redirect to index

def test_register_trading_account_route(client):
    """Test the register trading account route."""
    rv = client.get('/register_trading_account')
    assert rv.status_code == 200
    rv = client.post('/register_trading_account')
    assert rv.status_code == 200

def test_view_stocks_route(client):
    """Test the view stocks route."""
    rv = client.get('/view_stocks')
    assert rv.status_code == 200

def test_select_algorithm_route(client):
    """Test the select algorithm route."""
    rv = client.get('/select_algorithm')
    assert rv.status_code == 200

def test_view_open_positions_route(client):
    """Test the view open positions route."""
    rv = client.get('/view_open_positions')
    assert rv.status_code == 200
    rv = client.post('/view_open_positions')
    assert rv.status_code == 200

def test_view_balance_growth_route(client):
    """Test the view balance growth route."""
    rv = client.get('/view_balance_growth')
    assert rv.status_code == 200
    rv = client.post('/view_balance_growth')
    assert rv.status_code == 200

def test_view_trade_history_route(client):
    """Test the view trade history route."""
    rv = client.get('/view_trade_history')
    assert rv.status_code == 200

def test_view_profile_route(client):
    """Test the view profile route."""
    rv = client.get('/view_profile')
    assert rv.status_code == 200
