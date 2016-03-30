from flask import Blueprint

game_blueprint = Blueprint('game', __name__, template_folder='templates',
                           static_folder='static', static_url_path='/%s' % __name__)

extra = game_blueprint
