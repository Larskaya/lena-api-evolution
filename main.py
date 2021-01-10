import flask
from flask import Flask, render_template
import psycopg2, os 
from threading import Thread

#from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GsGFfDduiAGF1344tyoDGaFagfG1'
app.config.from_object(__name__)
#socketio = SocketIO(app)

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

# def get_db():
#     """ соединение с бд, если оно еще не установлено"""
#     if not hasattr(flask.g, 'link_db'):
#         flask.g.link_db = connect_db()
#     return flask.g.link_db

@app.route('/')
def documentation():
    return render_template( 'docs.html' )

from routs import login, registration, sectors, add_sector, messages
import sectors#, decrease_food



#from increase_amount import increase_amount
# thread1 = Thread(target=increase_amount)

# def main():
#     if __name__ == '__main__':
#         app.run(port=3355)

# thread2 = Thread(target=main)

if __name__ == '__main__':
    app.run(port=3355)

# thread1.start()
# print('111')
# thread2.start()
# print('222')



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