from flask import Blueprint, render_template

core_blueprint = Blueprint('core', __name__, template_folder='templates',
                           static_folder='static', static_url_path='/%s' % __name__)

extra = core_blueprint


@extra.route(r'/', methods=['GET'])
def index():
    return render_template('core/base.html')
