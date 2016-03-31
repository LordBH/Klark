from app import socket_io
from flask import Blueprint, render_template, request
from app.core.tools import get_configurations


core_blueprint = Blueprint('core', __name__, template_folder='templates',
                           static_folder='static', static_url_path='/%s' % __name__)

extra = core_blueprint


@extra.route(r'/', methods=['GET', 'POST'])
def index():
    context = {}

    if request.method == 'GET':

        return render_template('core/base.html', context=context)

    if request.method == 'POST':

        data = get_configurations(request)

        print()
        print(data)
        print()

        return render_template('core/base.html', context=context)
