from flask import Flask
from flask_smorest import Api
from config import config
#from flask_cors import CORS


api = Api()

def create_app(config_name):
    app = Flask(__name__)
    #CORS(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    api.init_app(app)

    # Set up api blueprint
    from .main import blp as api_blueprint
    api.register_blueprint(api_blueprint)

    return app
