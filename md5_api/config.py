DB_CONFIG = ('postgres', '1234', 'postgres:5432', 'md5_api')
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://%s:%s@%s/%s" % DB_CONFIG
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://%s:%s@%s/%s" % DB_CONFIG

SQLALCHEMY_DATABASE_URI_TEST = 'sqlite:////tmp/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

CELERY_BROKER_URL = 'amqp://user:password@rabbit:5672/'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_IMPORTS = ('md5_api.tasks',)

# Email
EMAIL_ENABLED = False
EMAIL_HOST = 'test.ru'
EMAIL_FROM_ADDR = 'info@test.ru'
