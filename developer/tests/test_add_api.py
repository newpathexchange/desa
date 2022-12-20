import pytest

def test_add_get(flask_client):
    """Test add get"""
    rv = flask_client.get('/api/add?num1=14&num2=17')
    assert rv.status == '200 OK'
    assert rv.json['result'] == "31.0"
    rv = flask_client.get('/api/add?num1=47.38&num2=8.14')
    assert rv.status == '200 OK'
    assert rv.json['result'] == "55.52"
    rv = flask_client.get('/api/add?num1=-8.5&num2=14')
    assert rv.status == '200 OK'
    assert rv.json['result'] == "5.5"
    rv = flask_client.get('/api/add?num1=bogus&num2=8.14')
    assert rv.status == '422 UNPROCESSABLE ENTITY'


def test_add_post(flask_client):
    """Test add post"""
    rv = flask_client.post('/api/add', json={
        'num1': 14,
        'num2': 17
    })
    assert rv.status == '200 OK'
    assert rv.json['result'] == "31.0"
    rv = flask_client.post('/api/add', json={
        'num1': "47.38",
        'num2': "8.14"
    })
    assert rv.status == '200 OK'
    assert rv.json['result'] == "55.52"
    rv = flask_client.post('/api/add', json={
        'num1': "-8.5",
        'num2': "14"
    })
    assert rv.status == '200 OK'
    assert rv.json['result'] == "5.5"
    rv = flask_client.post('/api/add', json={
        'num1': "bogus",
        'num2': "14"
    })
    assert rv.status == '422 UNPROCESSABLE ENTITY'

