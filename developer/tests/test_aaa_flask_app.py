import pytest

@pytest.mark.filterwarnings("ignore:`np.typeDict`:DeprecationWarning")
def test_aaa_flask_app(flask_app):
    """Make sure flask app has been initialized"""
    dummy = flask_app
    assert True
