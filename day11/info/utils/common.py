from flask import session, current_app, g
from info.models import User


# define filter
def index_filter(index):
    if index == 0:
        return 'first'
    elif index == 1:
        return 'second'
    elif index == 2:
        return 'third'
    else:
        return ''


import functools


def login_required(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id')
        user = None
        try:
            user = User.query.filter_by(id=user_id).first()
        except Exception as e:
            current_app.logger.error(e)
        g.user = user
        return f(*args, **kwargs)

    # wrapper.__name__ = f.__name__
    return wrapper
