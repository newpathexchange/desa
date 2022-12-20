import os

class Config:
    # Open Weather Map settings
    OPENWEATHERMAP_URL = 'https://api.openweathermap.org/data/2.5/weather'
    OPENWEATHERMAP_KEY = 'REDACTED'
    OPENWEATHERMAP_RETRIES = '3'
    
    # OpenAPI settings
    API_TITLE = 'DESA Example API'
    API_VERSION = '1.1'
    OPENAPI_URL_PREFIX = "/doc"
    OPENAPI_JSON_PATH = "api-spec.json"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_URL = "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    OPENAPI_VERSION = '3.0.2'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass

class EnvironmentConfig(Config):
    ## MongoDB settings
    OPENWEATHERMAP_URL = os.environ.get('OPENWEATHERMAP_URL')
    OPENWEATHERMAP_KEY = os.environ.get('OPENWEATHERMAP_KEY')
    OPENWEATHERMAP_RETRIES = os.environ.get('OPENWEATHERMAP_RETRIES')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'kubernetes': EnvironmentConfig,

    'default': DevelopmentConfig
}
