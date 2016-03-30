from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig
from app.blueprints import BLUEPRINTS

# application
app = Flask(__name__)

# app configurations
app.config.from_object(DevelopmentConfig)

# DataBase
db = SQLAlchemy(app)

# Register blueprints
for b in BLUEPRINTS:
    app.register_blueprint(b)
