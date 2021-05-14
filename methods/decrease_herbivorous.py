import psycopg2

from skills_matrix import Matrix

def start_transaction(cursor):
    cursor.execute('BEGIN')

def finish_transaction(db, cursor):
    cursor.execute('COMMIT')
    db.commit

def get_fertile(cursor, crtr):
    cursor.execute(f"SELECT skills FROM skills WHERE user_id = {crtr}")
    skills = cursor.fetchone()
    fertile = 0
    if skills:
        skills = skills[0]
        for skill in skills:
            fertile += Matrix.get_skill_matrix(skill)['fertile']
    print('fertile:', fertile)
    return fertile

def get_herb_amount(cursor, herb, sector_id):
    cursor.execute(f"SELECT amount FROM creatures WHERE user_id = {herb} AND sector_id = {sector_id}")
    res = cursor.fetchone()
    if res:
        print('herb amount', res) 
        return res[0]
    return False
 
def kill_herb(db, cursor, herb, sector_id):
    try:
        print('kill herb')
        cursor.execute(f"DELETE FROM creatures WHERE user_id = {herb} AND sector_id = {sector_id}")
        db.commit()
    except psycopg2.Error as e:
        print('Error delete', str(e))
        return False
    return True

def decrease(db, cursor, herb, sector_id):
    try:
        amount = get_herb_amount(cursor, herb, sector_id)
        fertile = get_fertile(cursor, herb)
        if fertile and amount:
            if amount - (fertile + 1) > 0:
                print('update amount: amount -= (1 + fertile)')
                cursor.execute(f"UPDATE creatures SET amount = amount - 1 WHERE user_id = {herb} AND sector_id = {sector_id}")
                db.commit()
            else:
                if not kill_herb(db, cursor, herb, sector_id):
                    print('herd was not died')
                    return False
                else:
                    print('herbivorous was killed')
    except psycopg2.Error as e:
        print('Error update', str(e))
        return False
    return True

def get_crtrs_in_sector(cursor, sector_id):
    cursor.execute(f"SELECT * FROM creatures WHERE sector_id = {sector_id}")
    res = cursor.fetchall()
    if res: return res
    return False

def this_crtr_is_herb(cursor, crtr):
    cursor.execute(f"SELECT skills FROM skills WHERE user_id = {crtr}")
    skills = cursor.fetchone()
    if skills:
        if skills[0][1] == '1':
            return True
    return False

def decrease_herbivorous(db, cursor, sector_id):
    herbs = []
    crtrs_in_sector = get_crtrs_in_sector(cursor, sector_id) 
    
    if crtrs_in_sector: 
        crtrs_in_sector = crtrs_in_sector[0]
        print('herbs in sectors -', crtrs_in_sector)
        for crtr in crtrs_in_sector:
            start_transaction(cursor)

            if this_crtr_is_herb(cursor, crtr): herbs.append(crtr)
            # print('start transaction')
            if herbs:
                for herb in herbs:
                    decrease(db, cursor, herb, sector_id)
            finish_transaction(db, cursor)
            #print('finish transaction')
            print('herbs:', herbs)

