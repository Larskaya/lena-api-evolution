from __main__ import app
import flask
from flask import request, jsonify, make_response, render_template
from App import App
from werkzeug.security import check_password_hash

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = App.login(request.form['login'])
        user_id = data[0]
        user_hpsw = data[1]

        if check_password_hash( user_hpsw, request.form['psw'] ):
            code = data[2]
            if code:

                log = ''
                if request.cookies.get('code'):
                    log = request.cookies.get('code')

                res = make_response('authorization: {log}')
                res.set_cookie('code', str(code))
                return res
            
        return jsonify( {"success": False} )
    return render_template('docs.html')




# @app.route('/delete-cookie/')
# def delete_cookie():
#     res = make_response("Cookie Removed")
#     res.set_cookie('code', str(12134124), max_age=0)
#     return res

