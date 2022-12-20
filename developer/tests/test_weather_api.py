import pytest
import json

def test_weather_get(flask_client):
    """Test hello method"""
    rv = flask_client.get('/api/weather?uszip=21207')
    try:
      rv_json = json.loads(rv.json['result'])
      json_error = False
    except:
        json_error = True
    assert rv.status == '200 OK'
    assert not json_error
    assert rv_json['name'] == 'Gwynn Oak'

def test_weather_post(flask_client):
    """Test hello method"""
    rv = flask_client.post('/api/weather', json={ 'uszip': '21207' })
    try:
      rv_json = json.loads(rv.json['result'])
      json_error = False
    except:
        json_error = True
    assert rv.status == '200 OK'
    assert not json_error
    assert rv_json['name'] == 'Gwynn Oak'
