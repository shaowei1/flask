from flask import Blueprint

private = Blueprint('private', __name__)


@private.route('/')
def index():
    return 'private_index'


@private.route('/list')
def private_list():
    return 'private_list'
