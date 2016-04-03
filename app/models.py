from app import db
from datetime import datetime


class GameRooms(db.Model):
    __tablename__ = 'game_rooms'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    game_id = db.Column(db.String(30), nullable=False)
    player1 = db.Column(db.String(40), nullable=False)
    player2 = db.Column(db.String(40), nullable=False)
    win = db.Column(db.String(40), nullable=False)
    ip1 = db.Column(db.String(15), nullable=False)
    ip2 = db.Column(db.String(15), nullable=False)
    moves = db.Column(db.Text)
    active = db.Column(db.DateTime, default=datetime.now())

    def __init__(self):
        pass


class UserConfigurations(db.Model):
    __tablename__ = 'user_config'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    ip = db.Column(db.String(15), nullable=False, unique=True)
    nickname = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    rules = db.Column(db.String(10), nullable=False)
    colors = db.Column(db.String(20), nullable=False)
    symbols = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, data, ip):
        self.ip = ip
        self.nickname = data['nickname']
        self.quantity = data['quantity']
        self.size = data['size']
        self.rules = data['rules']
        self.colors = data['colors']
        self.symbols = data['symbols']

        self.set_data(self)

    @staticmethod
    def set_data(self):
        u = UserConfigurations
        self.rules = u.set_selections(self)
        self.colors = u.set_colors(self)
        self.symbols = u.set_symbols(self)

    @staticmethod
    def set_selections(self):
        sel = ''

        for x in self.rules:
            sel += x + "|"

        return sel

    @staticmethod
    def set_colors(self):
        colors = ''

        col = self.colors

        for x, y in col.items():
            colors += x + ':' + y[0] + "|" + y[1] + "|" + y[2] + '+'

        return colors

    @staticmethod
    def set_symbols(self):
        return self.symbols[0] + '|' + self.symbols[1]

    @staticmethod
    def change_settings(q, data):
        q.nickname = data['nickname']
        q.quantity = data['quantity']
        q.size = data['size']
        q.rules = data['rules']
        q.colors = data['colors']
        q.symbols = data['symbols']

        UserConfigurations.set_data(q)

db.create_all()
