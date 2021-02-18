import flask
from flask import request, jsonify
from __main__ import app
from werkzeug.security import generate_password_hash

from App import App

@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        hash_ = generate_password_hash( request.form['psw'] )
        res = False
        try:
            res = App.registration(request.form['name'], hash_, request.form['login'], request.form['email'])
            print('res:', res)
        except Exception as e:
            print('Exception', str(e))

        if res:
            return jsonify( {"success": True} )
        else:
            return jsonify( {"success": False, "error": 'something error'} )
    return jsonify( {'success': False} )


