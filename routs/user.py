from __main__ import app
import flask
from flask import request, jsonify, make_response
from App import App
from werkzeug.security import generate_password_hash

@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        users = App.getUsers()
        data = []
        for user in users:
            b = {
                'id': user[0], 
                'name': user[1]
            }
            data.append(b)

        response = flask.jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    elif request.method == 'POST':
        hash_ = generate_password_hash( request.form['psw'] )
        res = False
        try:
            res = App.registration(request.form['name'], hash_, request.form['login'], request.form['email'])
        except Exception as e:
            print('Exception', str(e))

        if res:
            return jsonify( {"success": True} )
        else:
            return jsonify( {"success": False, "error": 'res - false'} )
    return jsonify( {'success': False} )


