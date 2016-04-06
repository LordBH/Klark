from app import db
from app.core.validations import ValidateConfig
from datetime import datetime
from flask import request
from random import random

valid = ValidateConfig()


class GameRooms(db.Model):
    __tablename__ = 'game_rooms'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    game_id = db.Column(db.String(30), nullable=False)
    player1 = db.Column(db.String(40))
    player2 = db.Column(db.String(40))
    win = db.Column(db.String(40))
    ip1 = db.Column(db.String(15))
    ip2 = db.Column(db.String(15))
    q_count = db.Column(db.String(5))
    q_size = db.Column(db.String(5))
    rules = db.Column(db.String(10))
    moves = db.Column(db.Text, default='0')
    active = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, data, create=False, join=False):
        if create:
            q = data.get('q')
            size = data.get('size')
            rules = {
                'v': data.get('v'),
                'h': data.get('h'),
                'd': data.get('d')
            }

            self.game_id = self.create_game_id()
            self.player1 = valid.valid_nickname(data.get('nickname'))
            self.q_count = q if not valid.valid_size(q) else 3
            self.q_size = size if not valid.valid_size(size) else 3
            self.ip1 = request.remote_addr
            self.win = -1

            self.get_rules(rules)

    def get_rules(self, rul):
        extra = ''
        for x, y in rul.items():
            if y:
                extra += x + '|'

        self.rules = extra

    @staticmethod
    def create_game_id(n=8):
        value = int(random() * 10 ** n)
        l = len(str(value))
        for x in range(n - l):
            value *= 10

        return value


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
        u = UserConfigurations

        self.ip = ip
        self.nickname = data['nickname']
        self.q_count = data['q_count']
        self.q_size = data['q_size']
        self.rules = u.set_rules(data['rules'])
        self.colors = u.set_colors(data['colors'])
        self.symbols = u.set_symbols(data['symbols'])

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
        u = UserConfigurations
        q.nickname = data['nickname']
        q.q_count = data['q_count']
        q.q_size = data['q_size']
        q.rules = u.set_rules(data['rules'])
        q.colors = u.set_colors(data['colors'])
        q.symbols = u.set_symbols(data['symbols']).upper()

        return q

db.create_all()
