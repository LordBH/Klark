from os import path, urandom


BASE_DIR = path.join(path.dirname(__file__))
DB_NAME = "klark.db"


class ConfigClass:
    # App Settings
    SECRET_KEY = urandom(60)

    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # create DB on absolute path
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + BASE_DIR + '/' + DB_NAME
    CSRF_ENABLED = True

    # Flask-Mail settings
    MAIL_USERNAME = 'testingdjangomaxx@gmail.com'
    MAIL_PASSWORD = '][poi123'
    MAIL_DEFAULT_SENDER = 'testingdjangomaxx@gmail.com'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    AUTHOR_EMAIL = 'testingdjangomaxx@gmail.com'

    # Flask-User settings
    STATIC_FOLDER = 'static'


class ProductionConfig(ConfigClass):
    DEBUG = False


class DevelopmentConfig(ConfigClass):
    DEVELOPMENT = True
    DEBUG = True
