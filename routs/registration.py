import flask
from flask import request, jsonify
from __main__ import app
from werkzeug.security import generate_password_hash

#from database.EvolutionDB import EvolDataBase

from App import App

@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        hash = generate_password_hash( request.form['psw'] )

        # dbase = EvolDataBase( get_db() )
        # res = dbase.addUser( request.form['name'], hash, request.form['login'], request.form['email'] ) 

        # print('email:', request.form['email'])
        # print('name:', request.form['name'])
        # print('hash:', hash)
        # print('login:', request.form['login'])

        res = App.registration(request.form['name'], hash, request.form['login'], request.form['email'])
        if res:
            return jsonify( {"success": True} )
        else:
            return jsonify( {"success": False, "error": 'something error'} )
    return jsonify( {'success': False} )


