import flask
from flask import request, jsonify
from __main__ import app

from App import App

@app.route('/sector/add', methods=['POST'])
def add_sector():
    f = request.form
    res = App.add_sector( f['position_top'], f['position_left'], f['food'] )
    if res: return jsonify( {"success": True} )
    else: return jsonify( {"success": False} )


