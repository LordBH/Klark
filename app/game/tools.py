from app.models import db
from flask import abort, session, request


def check_game(game):
    if len(game) != 8:
        abort(404)
    try:
        int(game)
    except ValueError:
        abort(404)


def set_player(q):
    nickname = session.get('nickname')
    ip = request.remote_addr

    q.player2 = nickname
    q.ip2 = ip

    db.session.add(q)
    db.session.commit()


def create_context_game(query):
    nickname = session.get('nickname')
    context = {
        'link': request.host + query.game_id,
        'moves': 0,
        'quantity': query.q_count,
        'permissions': 0,
    }
    if nickname == query.player1:
        context['you'] = query.player1,
        context['opponent'] = query.player2
    else:
        context['you'] = query.player2,
        context['opponent'] = query.player1

    return context
