from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_sesac():
    return 'I want to sleep!'

@bp.route('/')
def index():
    return 'Sesac index'