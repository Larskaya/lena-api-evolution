from decrease_predators import decrease_predators
import random, psycopg2

def delete_creatures(cursor, crtr, sector_id):
    try:
        cursor.execute(f"DELETE FROM creatures WHERE user_id={crtr} AND sector_id={sector_id}")
    except psycopg2.Error as e:
        print('Error', str(e))
        return False
    return True

def is_there_enough_amount( cursor, crtr, sector_id ):
    cursor.execute(f"SELECT amount FROM creatures WHERE user_id={crtr} AND sector_id={sector_id}")
    amount = cursor.fetchone()
    if amount: 
        num = 1
        if amount[0] - num > 0: return True
        elif amount[0] - num == 0: return delete_creatures(cursor, crtr, sector_id)
    return False

def decrease_crtr(db, cursor, crtr, sector_id):
    try:
        #a = 1 + infl_a
        if is_there_enough_amount( cursor, crtr, sector_id ):
            cursor.execute(f"UPDATE creatures SET amount = amount - 1 WHERE user_id = {crtr} AND sector_id = {sector_id}")#, ( crtr, sector_id, ))
            db.commit()
        else:
            decrease_predators(db, cursor, sector_id)
            return False

    except psycopg2.Error as e:
        print('error', str(e))
        return False
    return True

def increase_pred(db, cursor, pred_id, sector_id):
    try:
        #a = 1 + infl_a
        cursor.execute(f"UPDATE creatures SET amount = amount + 1 WHERE user_id = {pred_id} AND sector_id = {sector_id}")#, ( pred_id, sector_id))
        db.commit()
    except psycopg2.Error as e:
        print('error', str(e))
        return False
    return True

def get_creatures_in_sector( cursor, sector_id ):
    cursor.execute(f"SELECT * FROM creatures WHERE sector_id = {sector_id}")
    res = cursor.fetchall()
    if res: return res
    return False

def predators_skill( db, cursor, record, influence ):
    print('record:', record)
    creatures = get_creatures_in_sector( cursor, record[0] )
    crtr = random.choice(creatures)[1] # выбирается любое сущесвто из сектора (сам себя?)
    if decrease_crtr(db, cursor, crtr, record[0]): # вычитаем из него amount
        increase_pred(db, cursor, record[1], record[0]) # прибывляем к amount хищника