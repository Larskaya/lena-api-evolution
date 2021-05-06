
from collections import Counter
import psycopg2, random, time

def connect_db():
    conn = psycopg2.connect(
        database="evolution", 
        user="postgres", 
        
        host="localhost", 
        port="5432"
    )
    return conn    

db = connect_db()
cursor = db.cursor()


def get_fight(cursor, id_):
    cursor.execute(f"SELECT fight FROM skills WHERE user_id = {id_}")
    res = cursor.fetchone()
    if res: return res
    return False

def increase_amount(cursor, db, value, user_id, sector_id):
    print('user id and value +', user_id, value)
    try:
        cursor.execute(f"UPDATE creatures SET amount = amount + {value} WHERE user_id = {user_id} AND sector_id = {sector_id}")
        db.commit()
        if cursor.rowcount == 0:
            print('value has not been update')
            return False
    except psycopg2.Error as e:
        print( 'error adding '+ str(e) )
        return False
    return True

def get_amount(cursor, user_id, sector_id):
    cursor.execute(f"SELECT amount FROM creatures WHERE user_id = {user_id} AND sector_id = {sector_id}")
    res = cursor.fetchone()
    if res: return res
    return False

def delete_creatures(cursor, user_id, sector_id):
    try:
        cursor.execute(f"DELETE FROM creatures WHERE user_id = {user_id} AND sector_id = {sector_id}")
        db.commit()
        if cursor.rowcount == 0:
            #print('value has not been update')
            return False
    except psycopg2.Error as e:
        print( 'error adding '+ str(e) )
        return False
    return True


def creatures_died(cursor, user_id, sector_id):
    amount = get_amount(cursor, user_id, sector_id)[0]
    if amount < 1: delete_creatures(cursor, user_id, sector_id)


def dicrease_amount(cursor, db, value, user_id, sector_id):
    print('user id and value -', user_id, value)
    try:
        cursor.execute(f"UPDATE creatures SET amount = amount - {value} WHERE user_id = {user_id} AND sector_id = {sector_id}")
        db.commit()
        if cursor.rowcount == 0: 
            print('value has not been update')
            return False
    except psycopg2.Error as e:
        print( 'error adding '+ str(e) )
        return False
    return True


def get_winner(cursor, pare, sector_id):
    a = pare.split()[0]
    b = pare.split()[1]
    print('ids:', a, 'and', b)
    fight_a = get_fight(cursor, a)[0]
    fight_b = get_fight(cursor, b)[0]
    print('fight value -', fight_a, 'and', b)
    if fight_a > fight_b:
        value = fight_a - fight_b
        if increase_amount(cursor, db, value, a, sector_id): 
            if dicrease_amount(cursor, db, value, b, sector_id):
                creatures_died(cursor, b, sector_id)
    elif fight_b > fight_a:
        value = fight_b - fight_a
        if increase_amount(cursor, db, value, b, sector_id): 
            if dicrease_amount(cursor, db, value, a, sector_id):
                creatures_died(cursor, a, sector_id)
                



def make_pares(users_id):
    lst = []
    for el in users_id:
        lst.append(el[0]) 

    pares = []
    count = 0
    lnght = len(lst)
    while count < lnght:
        count2 = 0
        while count2 < lnght:
            if count != count2:
                pares.append('{0} {1}'.format(lst[count], lst[count2]))
            count2 += 1
        count += 1
    return pares

def get_sectors_id_in_creatures():
    cursor.execute(f"SELECT sector_id FROM creatures")
    res = cursor.fetchall()
    if res: return res
    return False

def start_transaction(cursor):
    cursor.execute('BEGIN')

def finish_transaction(cursor, db):
    cursor.execute('COMMIT')
    db.commit

def get_need_sectors(sectors_id, counter):
    res = []
    for sector in set(sectors_id):
        if counter[sector] > 1:
            res.append(sector)
    return res


def get_users(sector_id):
    cursor.execute(f"SELECT user_id FROM creatures WHERE sector_id = {sector_id}")
    res = cursor.fetchall()
    if res: return res
    return False



def main(cursor, pares, sectors_id):
        count = 0
        #for pare in pares:
        while count < len(pares):
            start_transaction(cursor)
            print('sectors - ', sectors_id)
            print('count, pares, sector_id -', count, pares[count], sectors_id[count])
            get_winner(cursor, pares[count], sectors_id[count])
            time.sleep(5)
            finish_transaction(cursor, db)
            count += 1


def fighting(cursor, db):
    pares = []
    sectors_id = []
    data = get_sectors_id_in_creatures()
    if data:
        print('data', data)
        for sector in data:
            sectors_id.append(int(sector[0]))

        counter = Counter(sectors_id)
        users_id = []
        need_sectors = get_need_sectors(sectors_id, counter)
        for sector in need_sectors:
            users_id.append(get_users(sector))
        for el in users_id:
            pares = make_pares(el)
        print('pares:', pares)

        try:
            main(cursor, pares, sectors_id)
        except:
            return False
