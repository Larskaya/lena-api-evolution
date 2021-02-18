import time, psycopg2
import flask 
from flask import jsonify

def connect_db():
    conn = psycopg2.connect(
        database="evolution", 
        user="postgres", 
        password="user", 
        host="localhost", 
        port="5432"
    )
    return conn    

def 

print(processing())
