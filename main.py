import flask
from flask import Flask, request, jsonify, render_template, url_for, redirect
import pymysql, json
import sqlite3
import os # files system

from werkzeug.security import generate_password_hash, check_password_hash

from EvolDataBase import EvolDataBase
#from flask_login import LoginManager
from UserLogin import UserLogin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GsGFfDduiAGF1344tyoDGaFagfG1'
app.config.from_object(__name__)


DATABASE = '/tmp/evolution.db'
DEBUG = True
SECRET_KEY = 'afe\shrtrjkl234frh#geash@hdrfzh1233'

app.config.update( dict(DATABASE=os.path.join(app.root_path, 'evolution.db')) )


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    # view db with dict not tuple
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    """ вспомогательная функция для создания таблиц бд без запуска сервера"""
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript( f.read() )
    db.commit()
    db.close()


def get_db():
    """ соединение с бд, если оно еще не установлено"""
    if not hasattr(flask.g, 'link_db'):
        flask.g.link_db = connect_db()
    return flask.g.link_db


dbase = None
@app.before_request
def before_request():
    """ Установление соединения с бд перед выполнением запроса  """
    global dbase 
    db = get_db()
    dbase = EvolDataBase(db)


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        hash = generate_password_hash( request.form['psw'] )
        res = dbase.addUser( request.form['name'], hash, request.form['email'] ) 
        if res:
            #return "<p> user added </p>"
            return redirect( url_for('login') )
        else:
            return "<p> add error </p>"
    return render_template('registration.html')



@app.route('/')
def index():
    return render_template('index.html')

from flask import jsonify
@app.route('/get_json')
def return_json():
    data = {'success': True}
    id_user = 1
    auth_user = dbase.addAuthUser(id_user)
    if auth_user:
        return jsonify(data) 




@app.route('/login1', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = dbase.getUser( request.form['email'] )
        if user:
            user_login = UserLogin().create(user)

        #print('USER:', user)
        #print('Email:', request.form['email'])
            print( 'JSON:', return_json(request.form['email']) )
            return "<p> ok </p>"
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def xxx():
    if request.method == 'POST':
        user_id = dbase.getUserId( request.form['email'] )
        print('USER ID:', user_id[0])
        if user_id:
            dbase.addAuthUser( int(user_id[0]) )
            return True
        return False
    return render_template('index.html')


@app.teardown_appcontext
def close_db(error):
    """ закрываем соединение с бд, если оно установлено """
    if hasattr(flask.g, 'link_db'):
        flask.g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)


