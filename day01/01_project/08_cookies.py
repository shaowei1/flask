from flask import request, Flask
app = Flask(__name__)

# Reading cookies
@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies get(key) instead of cookies[key] to not get a 
    # KeyError if the cookies is missing

# Storing cookies
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp

