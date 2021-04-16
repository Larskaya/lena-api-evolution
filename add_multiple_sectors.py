import psycopg2

def connect_db():
    conn = False
    try:
        conn = psycopg2.connect(
            database="evolution", 
            user="postgres", 
            
            host="localhost", 
            port="5432"
        )
    except Exception as e:
        print('connection error', str(e))
    return conn

db = connect_db()
cur = db.cursor()

def add_sectors(x, y, f):
    try:
        type_ = 1
        cur.execute('INSERT INTO sectors (position_left, position_top, food, type) VALUES (%s, %s, %s, %s)', (x, y, f, type_))
        db.commit()
    except psycopg2.Error as e:
        print('error adding', str(e))
    return True
