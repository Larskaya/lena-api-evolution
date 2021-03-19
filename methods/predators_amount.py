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

db = connect_db()
cursor = db.cursor()

def getSectorsWithHerbivorous():
    cursor.execute(f"SELECT sector_id FROM creatures WHERE type='травоядный'")
    res = cursor.fetchall()
    if res: return res
    return False

def getSectorsWithPredators():
    cursor.execute(f"SELECT sector_id FROM creatures WHERE type='хищник'")
    res = cursor.fetchall()
    if res: return res
    return False

def get_general_sectors():
    herbs, preds = [], []
    sectors_with_herbs = getSectorsWithHerbivorous()
    for el in sectors_with_herbs:
        herbs.append(el[0])

    sectors_with_preds = getSectorsWithPredators()
    for el in sectors_with_preds:
        preds.append(el[0])

    general = set(herbs) & set(preds)
    return general

def dicrease_herbivorous_amount(sector_id):
    try:
        cursor.execute("UPDATE creatures SET amount = amount - 1 WHERE amount > 0 AND sector_id=(%s) AND type='травоядный'", (str(sector_id)))
        db.commit()
    except psycopg2.Error as e:
        print('Error update', str(e))
        return False
    return True

def increase_predator_amount(sector_id):
    try:
        cursor.execute("UPDATE creatures SET amount = amount + 1 WHERE sector_id=(%s) AND type='хищник'", (str(sector_id)))
        db.commit()
    except psycopg2.Error as e:
        print('Error update', str(e))
        return False
    return True

def creatures_amount_changes():
    general_sectors = get_general_sectors()
    for el in general_sectors:
        if dicrease_herbivorous_amount(el):
            increase_predator_amount(el)


