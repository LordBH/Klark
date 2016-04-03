from flask import Blueprint, render_template
from app.game.tools import check_game
# from flask_socketio import join_room
# from app.models import GameRooms, UserConfigurations


game_blueprint = Blueprint('game', __name__, template_folder='templates',
                           static_folder='static', static_url_path='/%s' % __name__)

extra = game_blueprint


@extra.route(r'/<game>', methods=['GET', 'POST'])
def play(game):

    exist = check_game(game)

    if exist:
        pass

    return render_template('game/play.html')
