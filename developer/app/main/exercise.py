from types import SimpleNamespace
from flask.views import MethodView
from flask_smorest import abort
from . import blp
from ..schemas import ResultResponseSchema, AddRequestSchema, TimeRequestSchema
from ..schemas import TimeRequestSchema, WeatherRequestSchema
from flask import current_app as app

import datetime
import requests

import pprint
pp = pprint.PrettyPrinter(indent=4)

def calc_time(days):
    """Calculate current time plus number of days"""
    now = datetime.datetime.now()
    return now + datetime.timedelta(days=days)

# https://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid={API key}
def get_weather(uszip):
    """Retrieve weather payload from the remote API"""
    url = f"{app.config['OPENWEATHERMAP_URL']}?zip={uszip},us&appid={app.config['OPENWEATHERMAP_KEY']}"
    tries = 0
    while tries < int(app.config['OPENWEATHERMAP_RETRIES']):
        print('try')
        result = requests.get(url)
        tries += 1
        if result.status_code == requests.codes.ok:
            break
        elif tries >= int(app.config['OPENWEATHERMAP_RETRIES']):
            abort(500)
    return result.content
    #return result.json()

@blp.route('/hello')
class HelloView(MethodView):
    """Developer hello API methods"""
    @blp.response(200, ResultResponseSchema)
    def get(self):
        return SimpleNamespace(result='Hello')

@blp.route('/add')
class AddView(MethodView):
    """Developer add API methods"""
    @blp.arguments(AddRequestSchema, location="query")
    @blp.response(200, ResultResponseSchema)
    def get(self, request_data):
        result = request_data['num1'] + request_data['num2']
        return SimpleNamespace(result=result)

    @blp.arguments(AddRequestSchema)
    @blp.response(200, ResultResponseSchema)
    def post(self, request_data):
        result = request_data['num1'] + request_data['num2']
        return SimpleNamespace(result=result)

@blp.route('/time')
class TimeView(MethodView):
    """Developer add API methods"""
    @blp.arguments(TimeRequestSchema, location="query")
    @blp.response(200, ResultResponseSchema)
    def get(self, request_data):
        result = calc_time(request_data['days'])
        return SimpleNamespace(result=result)

    @blp.arguments(TimeRequestSchema)
    @blp.response(200, ResultResponseSchema)
    def post(self, request_data):
        result = calc_time(request_data['days'])
        return SimpleNamespace(result=result)


@blp.route('/weather')
class TimeView(MethodView):
    """Developer add API methods"""
    @blp.arguments(WeatherRequestSchema, location="query")
    @blp.response(200, ResultResponseSchema)
    def get(self, request_data):
        result = get_weather(request_data['uszip'])
        return SimpleNamespace(result=result)

    @blp.arguments(WeatherRequestSchema)
    @blp.response(200, ResultResponseSchema)
    def post(self, request_data):
        result = get_weather(request_data['uszip'])
        return SimpleNamespace(result=result)