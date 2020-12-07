import flask
from flask import Flask, request, jsonify, render_template, url_for, redirect
import pymysql, json, psycopg2, os, ast

import time
from time import sleep

from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'GsGFfDduiAGF1344tyoDGaFagfG1'
app.config.from_object(__name__)

DATABASE = '/tmp/evolution.db'
DEBUG = True
SECRET_KEY = 'afe\shrtrjkl234frh#geashhdrfzh1233'

app.config.update( dict(DATABASE=os.path.join(app.root_path, 'evolution.db')) )

def connect_db():
    conn = psycopg2.connect(
        database="evolution", 
        user="postgres", 
        password="4815162342", 
        host="localhost", 
        port="5432"
    )
    return conn

def get_db():
    """ соединение с бд, если оно еще не установлено"""
    if not hasattr(flask.g, 'link_db'):
        flask.g.link_db = connect_db()
    return flask.g.link_db

# dbase = None
# @app.before_request
# def before_request():
#     """ Установление соединения с бд перед выполнением запроса  """
#     global dbase 
#     db = get_db()
#     dbase = EvolDataBase(db)

@app.route('/main-page')
def index():
    return render_template('index.html')


@app.route('/')
def documentation():
    return render_template( 'docs.html' )

# @app.route('/users', methods=['POST', 'GET', 'PUT'])
# def get_auth_users():
#     if request.method == 'PUT':
#         data = request.data
#         dict_data = data.decode("UTF-8")
#         mydata = ast.literal_eval(dict_data)
#         print('data:', mydata['test'])
#         return ''
#     elif request.method == 'GET':
#         data = []
#         for u in dbase.getUsers():
#             user = {'login': u['login']}
#             data.append(user)
#         js = json.dumps(data, sort_keys=True, indent=4)
#         return js
#     else:
#         data = {'success': False}
#         return jsonify(data)

from routs import login, registration, sectors, sectors_add, messages
import food_change, sectors

if __name__ == '__main__':
    app.run(debug=True)


