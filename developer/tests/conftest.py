import pytest
from app import create_app

@pytest.fixture(scope='module')
def flask_app():
    """Initialized Flask app"""
    return create_app('testing')

@pytest.fixture(scope='module')
def flask_client():
    """Build a Flask test client"""
    app = create_app('testing')
    return app.test_client()
