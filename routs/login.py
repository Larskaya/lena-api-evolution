
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #print('form of login -', request.form['login'])
        user_id = dbase.getUserId( request.form['login'] )
        print('user id -', user_id)
        user_id = user_id[0]

        user_hpsw = dbase.getUserPsw( user_id )[0]
        print('PSWhASH:', user_hpsw, request.form['psw'])
        if check_password_hash( user_hpsw, request.form['psw']):
            code = dbase.addAuthUser( int(user_id) )
            if code:
                return jsonify( {"success": True, "code": code, "id": user_id} )
        return jsonify( {"success": False} )
    return render_template('docs.html')