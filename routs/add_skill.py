import flask, time
from flask import request, jsonify
from __main__ import app

from App import App


def replace_skills(skill, skills):
    answer = ''
    skills_lst = []
    for el in skills:
        skills_lst.append(el)
    skills_lst[int(skill)] = 1
    for el in skills_lst:
        answer += str(el)
    return answer

    
def check_cookies():
    if request.cookies.get('user_id') and request.cookies.get('code'):
        print('request: cookies and codes is got!')
        return True
    return False


@app.route('/user/add_skill', methods=['POST'])
def add_skill():
    user_id = request.cookies.get('user_id')
    skill = request.form['skill']

    if not check_cookies():
        return jsonify( {'success': False} )

    if len(skill) > 1 or int(skill) > 5:  
        return jsonify( {'error': 'skill can be a number from 1 to 5 '} )

    old_skills = App.get_skills(user_id)[0]
    skills = replace_skills(skill, old_skills)

    res = App.add_skill(user_id, skills)
    if res: return jsonify( {'success': True} )
    else: return jsonify( {'error': 'skill not update'} )
