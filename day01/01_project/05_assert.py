from flask import request, Flask
app = Flask(__name__)

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until
    # end of the with block such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'
# with app.test_request_context():
#    assert request.method == "POST"
