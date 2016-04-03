from flask import Blueprint, render_template, request, redirect, url_for, session
from app.core.tools import get_configurations, send_message, save_settings
from app.core.validations import ValidateConfig
from app import app


core_blueprint = Blueprint('core', __name__, template_folder='templates',
                           static_folder='static', static_url_path='/%s' % __name__)

extra = core_blueprint


@extra.route(r'/', methods=['GET'])
def index():
    context = {}

    message = session.get('message')
    if message is not None:
        context['msg'] = message
        del session['message']

    if request.method == 'GET':
        return render_template('core/base.html', context=context)


@extra.route(r'/recall', methods=['POST'])
def recall():
    session['message'] = 'So small e-mail, retry'
    get = request.form.get
    title = get('title')
    message = get('message')
    if len(title) > 3 and len(message) > 10:
        send_message(title, message)
        session['message'] = 'Thank you for helping'
    return redirect(url_for('core.index'))


@extra.route(r'/set_settings', methods=['POST'])
def settings():
    if request.method == 'POST':
        session['message'] = 'Bad Settings'

        data = get_configurations(request)
        validate = ValidateConfig()
        if validate(data):
            ip = request.remote_addr
            save_settings(data, ip)
            session['message'] = 'Settings saved for yours IP'

        return redirect(url_for('core.index'))


@app.errorhandler(404)
def not_found(error):
    print(error)
    return render_template('404.html')
