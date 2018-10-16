#!/usr/bin/python3

# By default, a route only answer to GET requests,
from flask import request


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


'''
If GET is present, Flask automatically adds support for the HEAD method and handles HEAD requests
'''
