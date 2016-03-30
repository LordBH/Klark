import os


class ConfigClass:
    # App Settings
    BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))
    SECRET_KEY = 'SECRET_KEY'

    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_DATABASE_URI = "postgresql:///cupcake"
    CSRF_ENABLED = True

    # Flask-User settings
    STATIC_FOLDER = 'static'


class ProductionConfig(ConfigClass):
    DEBUG = False


class DevelopmentConfig(ConfigClass):
    DEVELOPMENT = True
    DEBUG = True
