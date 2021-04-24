from __main__ import app
import flask
from flask import request, jsonify, make_response
from App import App

@app.route('/user', methods=['GET'])
def user():
    users = App.getUsers()
    print('users for GET', users)
    data = []
    for user in users:
        b = {
            'id': user[0], 
            'name': user[1],  
            # 'position_left': user[2], 
            # 'food': user[3],
        }
        data.append(b)

    response = flask.jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
