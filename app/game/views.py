from app import socket_io, db
from app.game.tools import check_game, set_player, create_context_game
from app.models import GameRooms
from flask import Blueprint, render_template, abort
from flask_socketio import join_room, emit


game_blueprint = Blueprint('game', __name__, template_folder='templates',
                           static_folder='static', static_url_path='/%s' % __name__)

extra = game_blueprint
KLARK_ROOM = 'KLARK'
GAME_CREATED = 'game-created'


@extra.route(r'/<game>', methods=['GET', 'POST'])
def play(game):
    check_game(game)
    q = GameRooms.query.filter_by(game_id=game).first()
    if q is None:
        abort(404)
    context = create_context_game(q)
    return render_template('game/play.html', context=context)


@socket_io.on('join-rooms', namespace='/core')
def first_connect(data):

    join_room(KLARK_ROOM)


@socket_io.on('create-game', namespace='/core')
def create_game(info):

    q = GameRooms(info, create=True)
    db.session.add(q)
    db.session.commit()
    info['game'] = q.game_id

    join_room(info['game'])

    emit(GAME_CREATED, info, room=KLARK_ROOM)


@socket_io.on('prepare-game', namespace='/core')
def loading_second_player(data):
    game_id = data.get('game')
    ex = {
        'msg': 'no game find',
        'game': game_id
    }
    q = GameRooms.query.filter_by(game_id=game_id).first()

    if game_id and q:
        join_room(game_id)
        set_player(q)
        ex['msg'] = 'Game Find'

        return emit('load-game', ex, room=game_id)  # info game
    emit('load-game', ex)  # info game
