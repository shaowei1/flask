#!/usr/bin/python3

from flask import Flask, url_for
app = Flask(__name__)
@app.route('/static/<cssname>')
def style(cssname):
    return 'css'

@app.route('/')
def index():
    return 'index page'
 
@app.route('/login')
def login():
    return 'login page'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Jhon Doe'))
    print(url_for('static', filename='style.css'))
     
'''     
python3 **.py
/
/login
/login?next=/
/user/John%20Doe
/static/style.css
'''
