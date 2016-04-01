from flask import Blueprint, render_template


game_blueprint = Blueprint('game', __name__, template_folder='templates',
                           static_folder='static', static_url_path='/%s' % __name__)

extra = game_blueprint


@extra.route(r'/<game>', methods=['GET', 'POST'])
def play(game):
    print()
    print(game)
    print()
    return render_template('game/play.html')
