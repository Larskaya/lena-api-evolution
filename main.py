import flask
from flask import Flask, request, jsonify, render_template, url_for, redirect
import pymysql, json, sqlite3, os, ast


from werkzeug.security import generate_password_hash, check_password_hash

from EvolDataBase import EvolDataBase
from UserLogin import UserLogin
from SectorsDB import SectorsDataBase


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



@app.route('/sectors', methods=['GET'])
def get_sectors():
    db = SectorsDataBase( get_db() )
    data = []
    for s in db.getAllData():
        sector = {'sector': ( s['id'], s['users'], s['food'])}
        data.append(sector)
    js = json.dumps(data, sort_keys=True, indent=4)
    return js





@app.route('/sectors/occupy', methods=['POST'])
def add_user_to_sector():
    # сделать проверку кода при добавлении в сектор
    user_code = 'aFSEHRtfhaetfae1445T'
    db = SectorsDataBase( get_db() )
    permission = db.userVerificationWhenAddingToSector(request.form['user_id'])
    print('PERMISSION -', permission)
    if permission: 
        users_in_sector = db.getUsersToSector( request.form['sector_id'] )
        users = ''
        for user in users_in_sector:
            if user[0] != 0:
                users += str(user[0]) + ', '
        users += str(request.form['user_id'])
        res = db.addUserToSector( request.form['sector_id'], users ) 
        if res: return jsonify( {"success": True} )
    return  jsonify( {"success": False} )












"""

@app.route('/user_vertification/<int:user_id>')
def userVerification(user_id):
    db = SectorsDataBase( get_db() )
    users = db.userVerificationWhenAddingToSector()
    users_str = []
    for user in users:
        if str(user[0]) != '0':
            users_str.append(str(user[0]))
    if str(user_id) not in users_str[0].split(','):
        return 'True'
    return 'False'


"""








@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        hash = generate_password_hash( request.form['psw'] )
        res = dbase.addUser( request.form['name'], hash, request.form['login'], request.form['email'] ) 
        if res:
            #return "<p> user added </p>"
            return redirect( url_for('login') )
        else:
            return jsonify( {"success": False} )
    return render_template('registration.html')



@app.route('/main-page')
def index():
    return render_template('index.html')



#@app.route('/messages', methods=['POST'])
def add_messages():
    user_id = 1
    code = '9684372501' 
    if dbase.userVerificationWhenSendingMessage(user_id, code):
        if dbase.addMessageInDB( user_id, request.form['message-text'] ):
            return render_template('communicate.html', message=request.form['message-text'])
        else:
            return '<h2> some kind error (added failed) </h2>'
    return '<h2> some kind error (verification failed) </h2>'


#@app.route('/messages', methods=['GET'])
def return_messages():
    data = []
    for m in dbase.getMessages():
        mes = {'sender': m['user_id'], 'time': m['time']}
        data.append(mes)
        js = json.dumps(data, sort_keys=True, indent=4)
    return js


@app.route('/')
def documentation():
    return render_template( 'docs.html' )



@app.route('/messages', methods=['POST', 'GET'])
def messages():
    user_id = 1
    code = '9684372501'
    if request.method == 'POST':
        if dbase.userVerificationWhenSendingMessage(user_id, code):
            if dbase.addMessageInDB( user_id, request.form['message-text'] ):
                return render_template('communicate.html', message=request.form['message-text'])
            else:
                return '<h2> some kind error (added failed) </h2>'
        return '<h2> some kind error (verification failed) </h2>'
    elif request.method == 'GET':
        return render_template('communicate.html')
    return ''



@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_id = dbase.getUserId( request.form['login'] )
        hash = generate_password_hash( request.form['psw'] )
        if user_id and check_password_hash( hash, request.form['psw']):
            dbase.addAuthUser( int(user_id[0]) )
            return jsonify( {"success": True} )
        return render_template('index.html')
    return render_template('login.html')



@app.route('/users', methods=['POST', 'GET', 'PUT'])
def get_auth_users():
    if request.method == 'PUT':
        data = request.data
        dict_data = data.decode("UTF-8")
        mydata = ast.literal_eval(dict_data)
        print('data:', mydata['test'])
        return ''



    elif request.method == 'GET':
        data = []
        for u in dbase.getUsers():
            user = {'login': u['login']}
            data.append(user)
        js = json.dumps(data, sort_keys=True, indent=4)
        return js
    else:
        data = {'success': False}
        return jsonify(data)



@app.teardown_appcontext
def close_db(error):
    """ закрываем соединение с бд, если оно установлено """
    if hasattr(flask.g, 'link_db'):
        flask.g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)


