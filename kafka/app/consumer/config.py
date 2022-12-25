import os

class Config:
    # Kafka settings
    KAFKA_BOOTSTRAP_SERVERS = 'desa1:9092,desa2:9092,desa3:9092'
    KAFKA_SECURITY_PROTOCOL = 'SASL_PLAINTEXT'
    KAFKA_SASL_MECHANISM = 'SCRAM-SHA-256'
    KAFKA_SASL_USERNAME = 'app-consumer'
    KAFKA_SASL_PASSWORD = 'app123encryptme'
    AVRO_SCHEMA_REGISTRY_URL = 'http://srd1:8081'
    AVRO_SCHEMA_NAMESPACE = 'com.desa'

    # Application-specific settings
    FAKE_DATA_TOPIC = 'fake_data'
    FAKE_DATA_CONSUMER_GROUP = 'fake-data-consumer'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass

class EnvironmentConfig(Config):
    # Kafka AvroProducer settings
    KAFKA_BOOTSTRAP_SERVERS = os.environ.get('KAFKA_BOOTSTRAP_SERVERS')
    KAFKA_SECURITY_PROTOCOL = os.environ.get('KAFKA_SECURITY_PROTOCOL')
    KAFKA_SASL_MECHANISM = os.environ.get('KAFKA_SASL_MECHANISM')
    KAFKA_SASL_USERNAME = os.environ.get('KAFKA_SASL_USERNAME')
    KAFKA_SASL_PASSWORD = os.environ.get('KAFKA_SASL_PASSWORD')
    AVRO_SCHEMA_REGISTRY_URL = os.environ.get('AVRO_SCHEMA_REGISTRY_URL')

    # Application-specific settings
    FAKE_DATA_TOPIC = os.environ.get('FAKE_DATA_TOPIC')
    FAKE_DATA_CONSUMER_GROUP = os.environ.get('FAKE_DATA_CONSUMER_GROUP')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'kubernetes': EnvironmentConfig,

    'default': DevelopmentConfig
}
