# import flask built-in object
from flask import session, render_template, current_app

from . import news_blue


@news_blue.route("/")
def index():
    # realize state retention
    session['shaowei'] = 'how lucky'
    return render_template('news/index.html')


# project logo icon loading, browser default request
# if not? clear browser cache and restart browser
# http://127.0.0.1:5000/favicon.ico
@news_blue.route('/favicon.ico')
def favicon():
    # by use context object, send static to browser
    return current_app.send_static_file('news/favicon.ico')
