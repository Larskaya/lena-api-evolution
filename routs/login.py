from __main__ import app
import flask
from flask import request, jsonify, make_response
from App import App
from werkzeug.security import check_password_hash


@app.route('/auth/login', methods=['POST'])
def login():
    data = App.login(request.form['login'])
    user_id = data[0]
    user_hpsw = data[1]

    if check_password_hash( user_hpsw, request.form['psw'] ):
        code = data[2]
        if code:
            log = ''
            if request.cookies.get('code') and request.cookies.get('user_id'):
                log = str(request.cookies.get('code')) + str(request.cookies.get('user_id'))

            res = make_response('authorization: {log}')
            res.set_cookie('code', str(code))
            res.set_cookie('user_id', str(user_id))
            return res
        
        return jsonify( {"success": False} )
    return render_template('docs.html')


@app.route('/auth/logout', methods=['POST'])
def logout():
    res = make_response("Cookie Removed")
    res.set_cookie('code', '', max_age=0)
    res.set_cookie('user_id', '', max_age=0)
    return res


@app.route('/auth/logout_full', methods=['POST'])
def logout_full():
    user_id = request.cookies.get('user_id')
    if user_id: 
        delete = App.deleteUser(int(user_id))
        if delete:
            res = make_response("Cookie Removed")
            res.set_cookie('code', '', max_age=0)
            res.set_cookie('user_id', '', max_age=0)
            return res
        return jsonify( {'error': 'error deleting from db'} )
    return jsonify( {'error': 'user has already been deleted'} )