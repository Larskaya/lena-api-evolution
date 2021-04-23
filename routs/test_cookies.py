import flask
from flask import request, jsonify, make_response

from __main__ import app

@app.route('/cookies')
def cookie():
    if not request.cookies.get('code'):
        res = make_response("cookie in processing")
        res.set_cookie('code', str(12134124), max_age=60*60*24)
    else:
        res = make_response(request.cookies.get('code'))
    return res



@app.route('/delete-cookie/')
def delete_cookie():
    res = make_response("Cookie Removed")
    res.set_cookie('code', str(12134124), max_age=0)
    return res




# @app.route('/cookies')
# def cookie():
#     code = ''
#     if request.cookies.get('code'):
#         res = make_response('cookie')
#         code = set_cookie('code', str(12134124), max_age=5*60)
    
#     res = make_response(f"<h1>response code:</h1> {code}")
#     res.set_cookie('code', str(5553535), max_age=5*60)
#     return ''