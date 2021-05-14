import psycopg2

from decrease_herbivorous import decrease_herbivorous

def start_transaction(cursor):
    cursor.execute('BEGIN')

def finish_transaction(db, cursor):
    cursor.execute('COMMIT')
    db.commit

def is_there_enough_food( cursor, num, sector_id ):
    print('SECTOR ID:', sector_id, type(sector_id))
    cursor.execute(f"SELECT food FROM sectors WHERE id = {sector_id}")
    food = cursor.fetchone()
    print("FOOD:", food)
    if food: 
        if food[0] - num >= 0: return True
    return False

def decrease_food( db, cursor, sector_id, infl_f ):
    print('decrease food')
    try:
        f = 1 + infl_f
        if is_there_enough_food( cursor, f, sector_id ):
            print('herb food update')
            cursor.execute("UPDATE sectors SET food = food - (%s) WHERE id=(%s)", (f, sector_id, ))
            db.commit()
        else:
            decrease_herbivorous(db, cursor, sector_id)
            return False
    except psycopg2.Error as e:
        print('Error update', str(e))
        return False
    return True

def increase_amount( db, cursor, sector_id, user_id, infl_a ):
    print('increase amount')
    try:
        a = 1 + infl_a
        cursor.execute("UPDATE creatures SET amount = amount + (%s) WHERE user_id=(%s) AND sector_id=(%s)", (a, user_id, sector_id, ))
        db.commit()
    except psycopg2.Error as e:
        print('Error update', str(e))
        return False
    return True

def herbivorous_skill( db, cursor, record, influence ):
    infl_f = influence['food']
    infl_a = influence['amount']
    if decrease_food( db, cursor, record[0], infl_f ):
        increase_amount( db, cursor, record[0], record[1], infl_a )

