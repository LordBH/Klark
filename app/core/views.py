from flask import Blueprint, render_template, request, redirect, url_for, session
from app.core.tools import get_configurations


core_blueprint = Blueprint('core', __name__, template_folder='templates',
                           static_folder='static', static_url_path='/%s' % __name__)

extra = core_blueprint


@extra.route(r'/', methods=['GET', 'POST'])
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
    get = request.form.get
    title = get('title')
    message = get('message')
    print()
    print(title)
    print(message)
    print()
    session['message'] = 'Thank you for helping'
    return redirect(url_for('core.index'))


@extra.route(r'/settings', methods=['POST'])
def settings():
    if request.method == 'POST':
        data = get_configurations(request)
        print()
        print(data)
        print()
        session['message'] = 'Settings saved for yours IP'
        return redirect(url_for('core.index'))
