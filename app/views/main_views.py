from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_sesac():
    return 'Hello, sesac!!'

@bp.route('/')
def index():
    return 'Sesac index'