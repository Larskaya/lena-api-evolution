import flask
from flask import Flask, render_template, send_from_directory
import psycopg2, os 

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'GsGFfDduiAGF1344tyoDGaFagfG1'
app.config.from_object(__name__)

DATABASE = '/tmp/evolution.db'
DEBUG = True
SECRET_KEY = 'afe\shrtrjkl234frh#geashhdrfzh1233'

app.config.update( dict(DATABASE=os.path.join(app.root_path, 'evolution.db')) )

def connect_db():
    conn = False
    try:
        conn = psycopg2.connect(
            database="evolution", 
            user="postgres", 
            
            host="localhost", 
            port="5432"
        )
    except Exception as e:
        print('connection error', str(e))
    return conn


def get_db():
    print('get db', flask.g)
    """ соединение с бд, если оно еще не установлено"""
    if not hasattr(flask.g, 'link_db'):
        flask.g.link_db = connect_db()
    return flask.g.link_db


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('templates/react/static/', path)


@app.route('/')
def documentation():
    return render_template( 'react/index.html' )


from routs import login, sectors, add_sector, messages, profile, add_skill, user
import sectors_occupy


if __name__ == '__main__':
    app.run(host='0.0.0.0')


