@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        hash = generate_password_hash( request.form['psw'] )
        res = dbase.addUser( request.form['name'], hash, request.form['login'], request.form['email'] ) 
        if res:
            #return "<p> user added </p>"
            return jsonify( {"success": True} )
        else:
            return jsonify( {"success": False} )
    return render_template('registration.html')



