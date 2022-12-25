import os

class Config:
    # Kafka settings
    KAFKA_BOOTSTRAP_SERVERS = 'desa1:9092,desa2:9092,desa3:9092'
    KAFKA_SECURITY_PROTOCOL = 'SASL_PLAINTEXT'
    KAFKA_SASL_MECHANISM = 'SCRAM-SHA-256'
    KAFKA_SASL_USERNAME = 'app-producer'
    KAFKA_SASL_PASSWORD = 'app123encryptme'
    AVRO_SCHEMA_REGISTRY_URL = 'http://srd1:8081'
    AVRO_SCHEMA_NAMESPACE = 'com.desa'
    KAFKA_PRODUCER_ACKS = 'all'
    KAFKA_PRODUCER_COMPRESSION = 'none'
    #KAFKA_PRODUCER_COMPRESSION = 'snappy'

    # Application-specific settings
    FAKE_DATA_TOPIC = 'fake_data'
    #SLEEP_SECONDS = '1'
    SLEEP_SECONDS = '.12'

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
    KAFKA_PRODUCER_ACKS = os.environ.get('KAFKA_PRODUCER_ACKS')
    KAFKA_PRODUCER_COMPRESSION = os.environ.get('KAFKA_PRODUCER_COMPRESSION')

    # Application-specific settings
    FAKE_DATA_TOPIC = os.environ.get('FAKE_DATA_TOPIC')
    SLEEP_SECONDS = os.environ.get('SLEEP_SECONDS')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'kubernetes': EnvironmentConfig,

    'default': DevelopmentConfig
}
