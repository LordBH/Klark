from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

# application
app = Flask(__name__)

# app configurations
app.config.from_object(DevelopmentConfig)

# DataBase
db = SQLAlchemy(app)

# Register blueprints
