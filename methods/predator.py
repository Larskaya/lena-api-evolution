import time, psycopg2
import flask
from flask import jsonify

def connect_db():
    conn = psycopg2.connect(
        database="evolution", 
        user="postgres", 
        password="4815162342", 
        host="localhost", 
        port="5432"
    )
    return conn

class Predator:
    def __init__(self, owner_id, color):
        self.owner = owner_id
        self.color = color

        self.health = 100
        self.hunger = 0
    
    def eat_others(self, sector_id):
        db = connect_db()
        cur = db.cursor()
        # получаем user_id того пользователя, которого будет есть хищник
        cur.execute(f"SELECT user_id FROM creatures WHERE sector_id={secor_id} AND type='травоядный'}" )
        user_for_food = cur.fetchone()
        if user_for_food[0] > 0:
            # уменьшается кол-во этого юзера в секторе 
            pass
        return jsonify({'error': 'there is no food in this sector'})