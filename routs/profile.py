import flask, time
from flask import request, jsonify
from __main__ import app

from App import App

def profile_type(type_):
    if type_ == 'хищник':
        return 'predator'
    else:
        return 'herbivorous'
    return jsonify( {'error': "haven't type"} )

def profile_color(color):
    if color == 'синий':
        return 'blue'
    elif color == 'зеленый':
        return 'green'
    else:
        return 'red'
    return jsonify( {'error': "haven't color"} )

@app.route('/profile', methods=['POST'])
def add_profile():
    code = request.form['code']
    user_id = request.form['user_id']
    color = request.form['color']
    type_ = request.form['type']
    if profile_type(type_) and profile_color(color):
        if type_ == 'хищник':
            res = App.add_profile(user_id, 1, color, code)
        elif type_ == 'травоядный':
            res = App.add_profile(user_id, 0, color, code)
        if res: return jsonify( {'success': True} )
        else: return jsonify( {'error': 'profile not added(a profile with this id already exists)'} )
    else: return jsonify( {'error': 'type or color is not suitable'} )
