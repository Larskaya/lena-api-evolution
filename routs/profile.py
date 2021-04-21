import flask, time
from flask import request, jsonify
from __main__ import app

from App import App

def profile_color(color):
    if color == 'синий':
        return 'blue'
    elif color == 'зеленый':
        return 'green'
    else:
        return 'red'
    return jsonify( {'error': "haven't color"} )


def replace_skills(skill):
    answer = ''
    skills = '00000'
    skills_lst = []
    for el in skills:
        skills_lst.append(el)
    skills_lst[int(skill)] = 1
    for el in skills_lst:
        answer += str(el)
    return answer




def check_cookies(code, user_id):
    if request.cookies.get('user_id') and request.cookies.get('code'):
        print('request: cookies and codes is got!')
        return True
    return False

@app.route('/profile', methods=['POST'])
def add_profile():
    code = request.form['code']
    user_id = request.form['user_id']
    color = request.form['color']
    skill = request.form['skill']
    
    if len(skill) > 1 or int(skill) > 5:
        return jsonify( {'error': 'skill can be a number from 1 to 5 '} )

    if not check_cookies(code, user_id):
        return jsonify( {'error': 'in cookies'} )

    skills = replace_skills(skill)
    
    res = App.add_profile(user_id, skills, color, code)
    if res: return jsonify( {'success': True} )
    else: return jsonify( {'error': 'profile not added(a profile with this id already exists)'} )
