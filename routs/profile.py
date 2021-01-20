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
def get_profile_data():
    user_id = request.form['user_id']
    color = request.form['color']
    type_ = request.form['type']
    if profile_type(type_) and profile_color(color):
        res = App.add_profile(user_id, type_, color)
        return jsonify( {'success': True} )
    else:  return jsonify( {'error': 'profile not added'} )


@app.route('/profile/<user_id>', methods=['GET'])
def get_profile(user_id):
    pass