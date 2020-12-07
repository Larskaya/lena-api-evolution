import flask
from flask import request, jsonify
from __main__ import app, get_db
from database.EvolDataBase import EvolDataBase
from werkzeug.security import generate_password_hash

@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        dbase = EvolDataBase( get_db() )
        hash = generate_password_hash( request.form['psw'] )
        res = dbase.addUser( request.form['name'], hash, request.form['login'], request.form['email'] ) 
        print('result where final', res)
        if res:
            #return "<p> user added </p>"
            return jsonify( {"success": True} )
        else:
            return jsonify( {"success": False, "error": 'such login already exists'} )
    return render_template('registration.html')


# {
#   "code": "6059378214", 
#   "id": 5, 
#   "success": true
# }


