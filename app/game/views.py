from app import socket_io, db
from app.game.tools import check_game, set_player, create_context_game, create_template
from app.models import GameRooms
from flask import Blueprint, render_template, abort, session
from flask_socketio import join_room, emit


game_blueprint = Blueprint('game', __name__, template_folder='templates',
                           static_folder='static', static_url_path='/%s' % __name__)

extra = game_blueprint
KLARK_ROOM = 'klark-room'
GAME_CREATED = 'game-created'
GAME_ROOMS = {}


@extra.route(r'/<game>', methods=['GET', 'POST'])
def play(game):
    check_game(game)
    q = GameRooms.query.filter_by(game_id=game).first()
    if q is None:
        abort(404)
    context = create_context_game(q)
    return render_template('game/play.html', context=context)


@socket_io.on('joining', namespace='/core')
def first_connect(data):
    for x in data['rooms']:
        join_room(str(x))


@socket_io.on('create-game', namespace='/core')
def create_game(data):
    q = GameRooms(data, create=True)

    data['template'] = create_template(q)
    data['game'] = q.game_id

    db.session.add(q)
    db.session.commit()

    emit(GAME_CREATED, data, room=KLARK_ROOM)

    emit('my-game-created', data)


@socket_io.on('prepare-game', namespace='/core')
def loading_second_player(data):
    game_id = data.get('game')
    player2 = data.get('nickname')
    ex = {
        'msg': 'no game find',
        'game': game_id
    }
    q = GameRooms.query.filter_by(game_id=game_id).first()
    if game_id and q:
        set_player(q, player2)
        ex['msg'] = 'Game Find'

    emit('load-game', ex)  # info game
    emit('load-game', ex, room=game_id)


@socket_io.on('game-on', namespace='/core')
def loading_players(data):
    game_id = data.get('rooms')
    if game_id is not None:
        join_room(game_id)
        GAME_ROOMS.setdefault(game_id, set())
        GAME_ROOMS[game_id].add(session.get('nickname'))
        return emit('players', len(GAME_ROOMS[game_id]), room=KLARK_ROOM)


@socket_io.on('enter-message', namespace='/core')
def send_message(ex):
    data = {
        'msg': ex.get('msg'),
        'nickname': session.setdefault('nickname', 'Guest'),
    }
    return emit('show-message', data, room=ex.get('room'))


@socket_io.on('symbol-set', namespace='/core')
def send_message(ex):
    data = {
        'id': ex.get('id'),
        'symbol': ex.get('symbol'),
    }
    return emit('show-symbol', data, room=ex.get('room'))
