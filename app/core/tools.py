from app import mail, db
from config import ConfigClass
from flask_mail import Message
from app.models import UserConfigurations


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
        'colors': {
          'f': [get('red-f'), get('green-f'), get('blue-f')],
          's': [get('red-s'), get('green-s'), get('blue-s')],
          'n': [get('red-n'), get('green-n'), get('blue-n')],
          'c': [get('red-c'), get('green-c'), get('blue-c')],
        },
        'symbols': [get('cell-1'), get('cell-2')]
    }

    return data


def send_message(t, m):
    msg = Message(t, recipients=[ConfigClass.AUTHOR_EMAIL])
    msg.html = m

    mail.send(msg)


def save_settings(c, ip):
    q = UserConfigurations.query.filter_by(ip=ip).first()

    if q is None:
        q = UserConfigurations(c, ip)
        db.session.add(q)
    else:
        UserConfigurations.change_settings(q, c)

    db.session.commit()
