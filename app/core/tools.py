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
        },
        'symbol': get('symbol'),
    }

    return data
