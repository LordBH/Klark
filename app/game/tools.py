from app.models import UserConfigurations, db
from app.core.tools import get_colors
from flask import abort, request, session
from random import choice


GAME_CONTEXT_CHECKER = {}


def create_template(q):
    game = q.game_id
    opponent = q.player1
    board_size = q.q_size
    quantity = q.q_count
    rules = ''
    for y in q.rules.split('|')[:-1]:
        rules += y.upper() + ' '
    butt = """<td class="start-play" onclick="startPlay(event)">Play</td>"""

    template = ''
    template += butt

    for x in [game, opponent, board_size, quantity, rules]:
        template += "<td>" + str(x) + "</td>"

    # template += butt

    return template


def check_game(game):
    if len(game) != 8:
        abort(404)
    try:
        int(game)
    except ValueError:
        abort(404)


def set_player(q, pl):
    ip = request.remote_addr

    q.player2 = pl
    q.ip2 = ip

    db.session.add(q)
    db.session.commit()


def create_context_game(query):
    context = {
        'link': 'http://' + request.host + '/' + query.game_id,
        'moves': 0,
        'quantity': query.q_count,
        'size': query.q_size,
        'player1': query.player1,
        'player2': query.player2,
        'rules': {}
    }
    GAME_CONTEXT_CHECKER.setdefault(query.game_id, {'count': 0, 'flag': choice([True, False])})
    game_id = GAME_CONTEXT_CHECKER[query.game_id]
    if game_id['count'] == 0:
        context['flag'] = game_id['flag']
    elif game_id['count'] == 1:
        context['flag'] = not game_id['flag']
    game_id['count'] += 1

    for x in query.rules.split('|')[:-1]:
        val = False
        if x:
            val = True
        context['rules'][x.upper()] = val
    if session.get('nickname') != 'Guest':
        get_user_settings(context)

    return context


def get_user_settings(cont):
    q = UserConfigurations.query.filter_by(ip=request.remote_addr).first()
    if q is not None:
        col = get_colors(q.__dict__)['colors']
        for y in col:
            cont[y] = '#'
            for x in ['r', 'g', 'b']:
                s = hex(int(col[y][x]))[2:]
                if len(s) != 2:
                    s = '0' + s
                cont[y] += s
        cont['symbols'] = q.symbols
