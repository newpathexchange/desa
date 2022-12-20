import pytest

def test_hello(flask_client):
    """Test hello method"""
    rv = flask_client.get('/api/hello',)
    assert rv.status == '200 OK'
    assert rv.json['result'] == "Hello"


