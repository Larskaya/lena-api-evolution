import psycopg2

def decrease_food( db, cursor, sector_id, infl_f ):
    try:
        f = 1 + infl_f
        cursor.execute("UPDATE sectors SET food = food - (%s) WHERE id=(%s)", (f, sector_id, ))
        db.commit()
    except psycopg2.Error as e:
        print('Error update', str(e))
        return False
    return True


def increase_amount( db, cursor, sector_id, user_id, infl_a ):
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

