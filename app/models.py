from app import db
from datetime import datetime


class GameRooms(db.Model):
    __tablename__ = 'game_rooms'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    game_id = db.Column(db.String(80), nullable=False)
    moves = db.Column(db.Text)
    active = db.Column(db.DateTime, default=datetime.now())

    def __init__(self):
        pass


class UserConfigurations(db.Model):
    __tablename__ = 'user_config'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nickname = db.Column(db.String(80), nullable=False)
    quantity_to_win = db.Column(db.Integer(20), nullable=False)
    board_size = db.Column(db.Integer(20), nullable=False)
    selections = db.Column(db.String(10), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    form = db.Column(db.Text)
    last_active = db.Column(db.DateTime, default=datetime.now())

    def __init__(self):
        pass


db.create_all()
