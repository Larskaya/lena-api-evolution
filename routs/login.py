from __main__ import app
#from database.EvolutionDB import EvolDataBase
import flask
from flask import request, jsonify
from werkzeug.security import check_password_hash

from App import App

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #print('login', request.form['login'])
        data = App.login(request.form['login'])
        print('all data for login', data)
        user_id = data[0]
        user_hpsw = data[1]

        #print('PSWhASH:', user_hpsw, request.form['psw'])
        if check_password_hash( user_hpsw, request.form['psw']):
            code = data[2]
            if code:
                return jsonify( {"success": True, "code": code, "id": user_id} )
        return jsonify( {"success": False} )
    return render_template('docs.html')