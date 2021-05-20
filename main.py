import flask
from flask import Flask, render_template
import psycopg2, os 

app = Flask(__name__)
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

@app.route('/main-page')
def documentation():
    #return render_template( 'sftp://v296823.hosted-by-vdsina.ru/home/lena/api/index.html' )
    return render_template( 'docs.html' )

from routs import login, sectors, add_sector, messages, profile, add_skill, user
import sectors_occupy



# import sys
# s = sys.path[0]
# print('sys', s)

# s += r"\\evolution_game"
# print(s)

# import pandas.Pandas
# print(Pandas.pr())

if __name__ == '__main__':
    app.run(debug=True)



# import sys
# sys.path[0] += r"\\folder"
# import index

# /home/lena/api/