from app import mail, db
from app.models import UserConfigurations
from config import ConfigClass
from flask_mail import Message
from flask import session
from random import random


DEFAULT_VALUE = {
    'nickname': int(random()*10**10),
    'q_count': 3,
    'q_size': 3,
    'rules': 'd|v|h|',
    'colors': 'c:90|90|90+s:255|255|255+f:0|0|0+n:90|90|90+',
    'symbols': 'O|X'
}


def get_configurations(r):

    get = r.form.get

    data = {
        'nickname': get('nick'),
        'q_count': get('q'),
        'q_size': get('size'),
        'rules': {
            'horizontal': get('ch-h'),
            'vertical': get('ch-v'),
            'diagonal': get('ch-d'),
        },
        'colors': {
          'f': [get('red-f'), get('green-f'), get('blue-f')],
          's': [get('red-s'), get('green-s'), get('blue-s')],
          'n': [get('red-n'), get('green-n'), get('blue-n')],
          'c': [get('red-c'), get('green-c'), get('blue-c')],
        },
        'symbols': [get('cell-1'), get('cell-2')]
    }
    return data


def get_context(c):
    # Symbols
    c['symbols'] = get_symbols(c)

    # Rules
    get_rules(c)

    # Colors
    get_colors(c)

    return c


def get_symbols(c):
    symbols = c['symbols'].split('|')
    return [symbols[0], symbols[1]]


def get_rules(c):
    rules = c['rules'].split('|')[:-1]
    c['rules'] = {}
    for x in rules:
        c['rules'][x] = True
    return c


def get_colors(c):
    color_class = c['colors'].split('+')[:-1]
    c['colors'] = {}
    for x in color_class:
        color_id = x.split(':')
        color_name = color_id[0]
        color_rgb = color_id[1].split('|')
        b = c['colors'][color_name] = {}
        for clr, v in zip(['r', 'g', 'b'], color_rgb):
            b[clr] = v
    return c


def get_user_settings(c, ip):
    q = UserConfigurations.query.filter_by(ip=ip).first()
    for x, y in DEFAULT_VALUE.items():
        if q is None:
            c[x] = y
        else:
            c[x] = q.__dict__[x]
    session.setdefault('nickname', DEFAULT_VALUE['nickname'])
    return get_context(c)


def send_message(t, m):
    msg = Message(t, recipients=[ConfigClass.AUTHOR_EMAIL])
    msg.html = m

    mail.send(msg)


def save_settings(c, ip):
    q = UserConfigurations.query.filter_by(ip=ip).first()

    if q is None:
        q = UserConfigurations(c, ip)
    else:
        q = UserConfigurations.change_settings(q, c)

    db.session.add(q)
    db.session.commit()
