import time, psycopg2
import flask 
from flask import jsonify

def connect_db():
    conn = psycopg2.connect(
        database="evolution", 
        
        host="localhost", 
        port="5432"
    )
    return conn    


db = connect_db()
cursor = db.cursor()
#print('db:', db, ', cursor:', cursor)


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
    sectors_with_herbs = getSectorsWithHerbivorous()
    sectors_with_preds = getSectorsWithPredators()
    general = set(sectors_with_herbs[0]) & set(sectors_with_preds[0])
    return general



def dicrease_herbivorous_amount(sector_id):
    try:
        cursor.execute("UPDATE creatures SET amount = amount - 1 WHERE amount > 0 AND sector_id=(%s) AND type='травоядный'", (str(sector_id)))
        db.commit()
        if cursor.rowcount == 0: 
            return 'herd (-)', False 
    except psycopg2.Error as e:
        print( 'error adding '+ str(e) )
        return False 
    return 'herd (-)', True 


def increase_predator_amount(sector_id):
    try:
        cursor.execute("UPDATE creatures SET amount = amount + 1 WHERE sector_id=(%s) AND type='хищник'", (str(sector_id)))
        db.commit()
        if cursor.rowcount == 0: 
            return 'predator (+)', False 
    except psycopg2.Error as e:
        print( 'error adding '+ str(e) )
        return False
    return 'predator (+)', True 


def creatures_amount_changes():
    general_sectors = get_general_sectors()
    print('sectors:', general_sectors)
    for el in general_sectors:
        if dicrease_herbivorous_amount(el):
            increase_predator_amount(el)


creatures_amount_changes()
