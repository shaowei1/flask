from flask import request, Flask
app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or credentials were invalid
    return render_template('login.html', error=error)

'''
to access parameters submitted in the URL (?key=value) you can use the args attribute:
searchword = request.args.get('key', '')
'''
