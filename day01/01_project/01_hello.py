from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello, world!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id , the id is a integer
    return 'Post %s' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

# Unique URLs/Redirection Behavior
# the following two rules differ in their use of a trailing slash
@app.route('/project/')
def project():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

'''
string: (default) access any text with a slash 削减/斜线
int:    accept positive integers
float:  accepts positive floating point values
path:   like string but also accepts slashs
uuid:   accepts UUID strings
'''

