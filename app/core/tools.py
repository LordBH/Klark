from flask_mail import Message
from app import mail
from config import ConfigClass


def get_configurations(r):

    get = r.form.get

    data = {
        'nickname': get('nick'),
        'quantity': get('q'),
        'size': get('size'),
        'rules': {
            'horizontal': get('ch-h'),
            'vertical': get('ch-v'),
            'diagonal': get('ch-d'),
        },
        'color': {
          'first': [get('red-f'), get('green-f'), get('blue-f')],
          'second': [get('red-s'), get('green-s'), get('blue-s')],
          'noughts': [get('red-n'), get('green-n'), get('blue-n')],
          'crosses': [get('red-c'), get('green-c'), get('blue-c')],
        },
        'symbol': [get('cell-1'), get('cell-2')]
    }

    return data


def send_message(t, m):
    msg = Message(t, recipients=[ConfigClass.AUTHOR_EMAIL])
    msg.html = m

    mail.send(msg)
