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


@app.route('/add_skill', methods=['POST'])
def add_skill():
    user_id = request.form['user_id']
    skill = request.form['skill']

    old_skills = App.get_skills(user_id)[0]
    skills = replace_skills(skill, old_skills)

    res = App.add_skill(user_id, skills)
    if res: return jsonify( {'success': True} )
    else: return jsonify( {'error': 'skill not update'} )
