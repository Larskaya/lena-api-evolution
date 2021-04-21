
from __main__ import app, get_db
import flask, json
from flask import request, jsonify

from database.Messages import MessagesDB




def check_cookies():
    if request.cookies.get('user_id') and request.cookies.get('code'):
        print('request: cookies and codes is got!')
        return True
    return False



@app.route('/messages', methods=['POST', 'GET'])
def messages():
    dbase = MessagesDB( get_db() )
    if request.method == 'POST':
        user_id = request.form['user_id']
        message = request.form['message']
        #print('form data massage:', request.form)

        if not check_cookies():
            return jsonify( {'error': 'in cookies'} )


            # if not dbase.isAuthValid(user_id, code):
            #     return jsonify( {"success": False, "error": "not authorized"} )
            #if dbase.userVerificationWhenSendingMessage(user_id, code):

        if dbase.addMessageInDB( user_id, message ):
            return jsonify( {"success": True} )
        else:
            return jsonify( {"success": False, "error": "added failed"} )
        return jsonify( {"success": False, "error": "verification failed"} )

    elif request.method == 'GET':
        data = []
        for m in dbase.getMessages():
            print('mm:', m)
            mes = {'user_id': m[0], 'text': m[1], 'time': m[2] }
            data.append(mes)

        return jsonify(data)
    return jsonify( {"success": False} )