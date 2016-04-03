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
    q_count = db.Column(db.String(5), nullable=False)
    q_size = db.Column(db.String(5), nullable=False)
    rules = db.Column(db.String(10), nullable=False)
    colors = db.Column(db.String(20), nullable=False)
    symbols = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, data, ip):
        self.ip = ip
        self.nickname = data['nickname']
        self.q_count = data['q_count']
        self.q_size = data['q_size']
        self.rules = data['rules']
        self.colors = data['colors']
        self.symbols = data['symbols']

        self.set_data()

    def set_data(self):
        u = UserConfigurations
        self.rules = u.set_rules(self)
        self.colors = u.set_colors(self)
        self.symbols = u.set_symbols(self).upper()

    @staticmethod
    def set_rules(self):
        sel = ''

        for x, y in self.items():
            if y == 'on':
                sel += x[0] + "|"

        return sel

    @staticmethod
    def set_colors(self):
        colors = ''

        for x, y in self.items():
            colors += x + ':' + y[0] + "|" + y[1] + "|" + y[2] + '+'

        return colors

    @staticmethod
    def set_symbols(self):
        return self[0] + '|' + self[1]

    @staticmethod
    def change_settings(q, data):
        # for x in q.__dict__:
        #     if x[0] not in ['_', 'd', 'i']:
        #         q.__dict__[x] = data[x]
        u = UserConfigurations
        q.nickname = data['nickname']
        q.q_count = data['q_count']
        q.q_size = data['q_size']
        q.rules = u.set_rules(data['rules'])
        q.colors = u.set_colors(data['colors'])
        q.symbols = u.set_symbols(data['symbols']).upper()
        return q

db.create_all()
