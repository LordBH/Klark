from os import path


BASE_DIR = path.join(path.dirname(__file__))
DB_NAME = "klark.db"


class ConfigClass:
    # App Settings
    SECRET_KEY = 'SECRET_KEY'

    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # create DB on absolute path
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + BASE_DIR + '/' + DB_NAME
    CSRF_ENABLED = True

    # Flask-User settings
    STATIC_FOLDER = 'static'


class ProductionConfig(ConfigClass):
    DEBUG = False


class DevelopmentConfig(ConfigClass):
    DEVELOPMENT = True
    DEBUG = True
