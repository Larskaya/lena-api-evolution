@app.route('/messages', methods=['POST', 'GET'])
def messages():
    if request.method == 'POST':
        code = request.form['code']
        user_id = request.form['user_id']
        message = request.form['message']
        if not dbase.isAuthValid(user_id, code):
            return jsonify( {"success": False, "error": "not authorized"} )
        if dbase.userVerificationWhenSendingMessage(user_id, code):
            if dbase.addMessageInDB( user_id, message ):
                return jsonify( {"success": True} )
            else:
                return jsonify( {"success": False, "error": "some kind error (added failed)"} )
        return jsonify( {"success": False, "error": "some kind error (verification failed)"} )

    elif request.method == 'GET':
        data = []
        for m in dbase.getMessages():
            mes = {'user_id': m['user_id'], 'message': m['message'], 'time': m['time'] }
            data.append(mes)

        js = json.dumps({'data':data}, sort_keys=True, indent=4)
        return js
    return jsonify( {"success": False} )