import pytest
import datetime

def test_time_get(flask_client):
    """Test add get"""
    before = datetime.datetime.now() + datetime.timedelta(days=4)
    rv = flask_client.get('/api/time?days=4')
    rv_date = datetime.datetime.strptime(rv.json['result'],'%Y-%m-%d %H:%M:%S.%f')
    after = datetime.datetime.now() + datetime.timedelta(days=4)
    assert rv.status == '200 OK'
    assert before < rv_date < after

    before = datetime.datetime.now() + datetime.timedelta(days=12.5)
    rv = flask_client.get('/api/time?days=12.5')
    rv_date = datetime.datetime.strptime(rv.json['result'],'%Y-%m-%d %H:%M:%S.%f')
    after = datetime.datetime.now() + datetime.timedelta(days=12.5)
    assert rv.status == '200 OK'
    assert before < rv_date < after

    before = datetime.datetime.now() + datetime.timedelta(days=-3.5)
    rv = flask_client.get('/api/time?days=-3.5')
    rv_date = datetime.datetime.strptime(rv.json['result'],'%Y-%m-%d %H:%M:%S.%f')
    after = datetime.datetime.now() + datetime.timedelta(days=-3.5)
    assert rv.status == '200 OK'
    assert before < rv_date < after


def test_add_post(flask_client):
    """Test add post"""
    before = datetime.datetime.now() + datetime.timedelta(days=4)
    rv = flask_client.post('/api/time', json={ 'days': 4 })
    rv_date = datetime.datetime.strptime(rv.json['result'],'%Y-%m-%d %H:%M:%S.%f')
    after = datetime.datetime.now() + datetime.timedelta(days=4)
    assert rv.status == '200 OK'
    assert before < rv_date < after
    
    before = datetime.datetime.now() + datetime.timedelta(days=12.5)
    rv = flask_client.post('/api/time', json={ 'days': 12.5 })
    rv_date = datetime.datetime.strptime(rv.json['result'],'%Y-%m-%d %H:%M:%S.%f')
    after = datetime.datetime.now() + datetime.timedelta(days=12.5)
    assert rv.status == '200 OK'
    assert before < rv_date < after

    before = datetime.datetime.now() + datetime.timedelta(days=-3.5)
    rv = flask_client.post('/api/time', json={ 'days': -3.5 })
    rv_date = datetime.datetime.strptime(rv.json['result'],'%Y-%m-%d %H:%M:%S.%f')
    after = datetime.datetime.now() + datetime.timedelta(days=-3.5)
    assert rv.status == '200 OK'
    assert before < rv_date < after


