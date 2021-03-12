import psycopg2

# import sys
# sys.path.append('../')

# from App import App

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

# def increase_amount():
#     try:
#         cursor.execute(f"UPDATE creatures SET amount = amount + 1, food = food - 1 WHERE food > 0 AND type = 'травоядный'")
#         db.commit()
#     except psycopg2.Error as e:
#         print( 'error adding '+ str(e) )
#         return False
#     return True 

def dicrease_food(sector_id):
    print('sector id', sector_id)
    try:
        cursor.execute("UPDATE sectors SET food = food - 1 WHERE id=(%s)", (str(sector_id)))
        db.commit()
    except psycopg2.Error as e:
        print('Error update', str(e))
        return False
    return True

def insrease_amount( sector_id, user_id ):
    try:
        cursor.execute("UPDATE creatures SET amount = amount + 1 WHERE user_id=(%s) AND sector_id=(%s)", (user_id, sector_id))
        db.commit()
    except psycopg2.Error as e:
        print('Error update', str(e))
        return False
    return True


def get_sector_data(i):
    res = None
    cursor.execute(f"SELECT amount, user_id FROM creatures WHERE sector_id={i} AND type='травоядный'")
    res = cursor.fetchone()
    if res: return res


def increase_herb():
    for i in range(1, 10):
        res = get_sector_data(i)
        print('herb here -', res)
        if res and res[0] > 0: 
            if insrease_amount( i, res[1] ):
                dicrease_food(i)
        else:
            print('-- isnt res or res[0] <= 0')
        print(res)
