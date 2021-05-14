from decrease_herbivorous import get_crtrs_in_sector, get_fertile
import psycopg2

from skills_matrix import Matrix

def start_transaction(cursor):
    cursor.execute('BEGIN')

def finish_transaction(db, cursor):
    cursor.execute('COMMIT')
    db.commit





def get_pred_amount(cursor, pred, sector_id):
    cursor.execute(f"SELECT amount FROM creatures WHERE user_id = {pred} AND sector_id = {sector_id}")
    res = cursor.fetchone()
    if res:
        print('herb amount', res) 
        return res[0]
    return False
 

def kill_pred(db, cursor, pred, sector_id):
    try:
        print('kill herb')
        cursor.execute(f"DELETE FROM creatures WHERE user_id = {pred} AND sector_id = {sector_id}")
        db.commit()
    except psycopg2.Error as e:
        print('Error delete', str(e))
        return False
    return True


def decrease(db, cursor, pred, sector_id):
    try:
        amount = get_pred_amount(cursor, pred, sector_id) 
        fertile = get_fertile(cursor, pred)
        if amount - (fertile + 1) > 0:
            print('update amount: amount -= 1')
            cursor.execute(f"UPDATE creatures SET amount = amount - 1 WHERE user_id = {pred} AND sector_id = {sector_id}")
            db.commit()
        else:
            if not kill_pred(db, cursor, pred, sector_id):
                print('pred was not died')
                return False
            else:
                print('predator was killed')
    except psycopg2.Error as e:
        print('Error update', str(e))
        return False
    return True

  

def decrease_predators(db, cursor, sector_id):
    crtrs_in_sector = get_crtrs_in_sector(cursor, sector_id)
    if crtrs_in_sector: 
        crtrs_in_sector = crtrs_in_sector[0]
        print('herbs in sectors -', crtrs_in_sector)
        # for crtr in crtrs_in_sector:
        #     start_transaction(cursor)

        if len(crtrs_in_sector) == 1: # если в секторе только 1 существо 
            decrease(cursor, crtrs_in_sector[0], sector_id)

        #     finish_transaction(db, cursor)