
from collections import Counter
import psycopg2, random, time

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


def start_transaction(cursor):
    cursor.execute('BEGIN')

def finish_transaction(cursor, db):
    cursor.execute('COMMIT')
    db.commit

def get_sectors_in_crtrs_tbl(cursor):
    cursor.execute(f"SELECT sector_id FROM creatures")
    res = cursor.fetchall()
    if res: return res
    return False

def get_sectors_where_many_crtrs(sectors_id, counter):
    res = []
    for sector in set(sectors_id):
        if counter[sector] > 1:
            res.append(sector)
    return res

def get_sector_ids(sectors_with_crtrs):
    sector_ids = []
    for sector in sectors_with_crtrs:
        sector_ids.append(int(sector[0]))
    return sector_ids

def get_users(cursor, sector_id):
    cursor.execute(f"SELECT user_id FROM creatures WHERE sector_id = {sector_id}")
    res = cursor.fetchall()
    if res: return res
    return False


def is_predator_in_pare(cursor, crtr):
    cursor.execute(f"SELECT skills FROM skills WHERE user_id = {crtr}")
    res = cursor.fetchone()[0]
    if res: 
        if res[2] == '1': return True
    return False


def delete_creatures(db, cursor, user_id, sector_id):
    try:
        cursor.execute(f"DELETE FROM creatures WHERE user_id = {user_id} AND sector_id = {sector_id}")
        db.commit()
        if cursor.rowcount == 0:
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

def creatures_died(cursor, user_id, sector_id):
    amount = get_amount(cursor, user_id, sector_id)[0]
    if amount < 1: delete_creatures(cursor, user_id, sector_id)



def increase_amount(db, cursor, sector_id, user_id, fertile):
    try:
        cursor.execute(f"UPDATE creatures SET amount = amount + {fertile} WHERE sector_id = {sector_id} AND user_id = {user_id}")
        db.commit()
        if cursor.rowcount == 0: 
            return False
    except psycopg2.Error as e:
        print( 'error adding '+ str(e) )
        return False
    return True


def dicrease_amount(db, cursor, sector_id, user_id, eat):
    try:
        cursor.execute(f"UPDATE creatures SET amount = amount - {eat} WHERE sector_id = {sector_id} AND user_id = {user_id}")
        db.commit()
        if cursor.rowcount == 0: 
            return False
    except psycopg2.Error as e:
        print( 'error adding '+ str(e) )
        return False
    return True


def get_fertile(cursor, crtr):
    cursor.execute(f"SELECT fertile FROM skills WHERE user_id = {crtr}")
    res = cursor.fetchone()
    if res: return res[0]
    return False

def get_eat(cursor, crtr):
    cursor.execute(f"SELECT eat FROM skills WHERE user_id = {crtr}")
    res = cursor.fetchone()
    if res: return res[0]
    return False


def fighting(cursor, db):
    sectors_with_crtrs = get_sectors_in_crtrs_tbl(cursor) # сектора, где есть существа
    if sectors_with_crtrs: 
        sector_ids = get_sector_ids(sectors_with_crtrs)
        sectors_where_many_crtrs = get_sectors_where_many_crtrs(sector_ids, Counter(sector_ids))

        # создадим словарь сектор и его существа
        sctrs_with_crtrs = {}

        # получаем id юзеров в нужных секторах
        users_id = []
        for sector in sectors_where_many_crtrs:
            users_id.append(get_users(cursor, sector))
            # составляем пары существ для драки
            for el in users_id:
                pares = make_pares(el)

            for pare in pares:
                a = pare.split()[0]
                b = pare.split()[1]
                # есть ли в паре существ хищник (второй скилл)
                if is_predator_in_pare(cursor, a):
                    fertile = get_fertile(cursor, a)
                    eat = get_eat(cursor, a)
                    if increase_amount(db, cursor, sector, a, fertile):
                        if dicrease_amount(db, cursor, sector, b, eat):
                            creatures_died(cursor, b, sector)
                
                elif is_predator_in_pare(cursor, b): 
                    fertile = get_fertile(cursor, b)
                    eat = get_eat(cursor, b)
                    if increase_amount(db, cursor, sector, b, fertile):
                        if dicrease_amount(db, cursor, sector, a, eat):
                            creatures_died(cursor, b, sector)

    


 
