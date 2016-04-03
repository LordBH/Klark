from config import DevelopmentConfig
from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail


# application
app = Flask(__name__)

# app configurations
app.config.from_object(DevelopmentConfig)

# DataBase
db = SQLAlchemy(app)

# Mail
mail = Mail(app)

# Web sockets
socket_io = SocketIO(app)

