import flask, time
from flask import request, jsonify
from __main__ import app
from routs.skills_matrix import Matrix


from App import App

def profile_color(color):
    if color == 'синий':
        return 'blue'
    elif color == 'зеленый':
        return 'green'
    else:
        return 'red'
    #return jsonify( {'error': "haven't color"} )


def replace_skills(skill):
    answer = ''
    skills = '000000000000'
    skills_lst = []
    for el in skills:
        skills_lst.append(el)
    skills_lst[int(skill)] = 1
    for el in skills_lst:
        answer += str(el)
    print('answer where replace skill', answer)
    return answer

def check_cookies():
    if request.cookies.get('user_id') and request.cookies.get('code'):
        print('request: cookies and codes is got!')
        return True
    return False

def start_transaction(cursor):
    cursor.execute('BEGIN')

def finish_transaction(cursor, db):
    cursor.execute('COMMIT')
    db.commit

from main import connect_db

@app.route('/user/profile', methods=['POST'])
def add_profile():

    db = connect_db()
    #cursor = db.cursor()

    user_id = request.cookies.get('user_id')
    color = request.form['color']
    skill = request.form['skill']
    
    if len(skill) > 2 or int(skill) > 12:
        return jsonify( {'error': 'skill can be a number from 1 to 12 '} )

    if not check_cookies():
        return jsonify( {'error': 'in cookies'} )

    
    skills = replace_skills(skill)

    skill = request.form['skill']
    abilities = Matrix.get_skill_matrix(skill)
    res = App.add_profile(user_id, skills, color, abilities)
    if res: 
        return jsonify( {'success': True} )
    else: return jsonify( {'error': 'profile not added(a profile with this id already exists)'} )
