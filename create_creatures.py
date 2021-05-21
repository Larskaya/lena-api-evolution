
from werkzeug.security import generate_password_hash
from routs.skills_matrix import Matrix
import random, psycopg2


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


def create_user_data():
    letters = 'qazxswedcvfrtgbnhyujmkiolp'
    for_psw = 'qazxswedcvfrtgbnhyujmkiolp0123456789'

    name = ''.join(random.choices(letters, k=7))
    login = '{}LOGIN'.format(name)
    email = '{}@ya.ru'.format(name)
    psw = ''.join(random.choices(for_psw, k=8))
    hpsw = generate_password_hash( psw )
    return name, login, hpsw, email



def addFirstSkill(cursor, db, user_id, skills, ab):
    try:
        cursor.execute("INSERT INTO skills (user_id, skills, fight, friend, hide, eat, fertile) VALUES (%s, %s, %s, %s, %s, %s, %s)", (user_id, skills, ab['fight'], ab['friend'], ab['hide'], ab['eat'], ab['fertile']))
        db.commit()
    except psycopg2.Error as e:
        print( 'error adding '+ str(e) )
        return False
    return True 


def checkAddingUser(login):
    cursor.execute(f"SELECT COUNT(*) FROM users WHERE login='{login}' ")
    res = cursor.fetchone()
    if res[0] > 0:
        return False
    return True


def add_user(cursor, db, name, hpsw, login, email):
    try:
        if checkAddingUser(login):
            cursor.execute( "INSERT INTO users (name, login, email, hpsw) VALUES(%s, %s, %s, %s)", (name, login, email, hpsw))
            db.commit()
        else:
            return False
    except psycopg2.Error as e:
        print( 'error adding '+ str(e) )
        return False
    return True


def get_userId(login):
    try:
        cursor.execute(f"SELECT id FROM users WHERE login='{login}'")
        res = cursor.fetchone()
        if res: return res
    except:
        print('error reading from db')
    return []


def updateAuthUser(cursor, db, code, user_id):
    try:
        cursor.execute(f"UPDATE auth_users SET code='{code}' WHERE id='{user_id}'")
        db.commit()
        if cursor.rowcount == 0: return False
    except psycopg2.Error as e:
        print( 'error adding '+ str(e) )
        return False
    return True



def add_auth_user(cursor, db , user_id):
    code = ''
    try:
        lst = random.sample(range(0, 10), 10)  
        
        for n in lst:
            code+=str(n)
        is_auth_updated = updateAuthUser(cursor, db, code, user_id)
        if not is_auth_updated:   
            cursor.execute( "INSERT INTO auth_users VALUES(%s, %s)", (user_id, code,) )
            db.commit()
    except psycopg2.Error as e:
        print( 'error adding '+ str(e) )
        return False
    return code

def add_profile(cursor, user_id, color):
    try:
        cursor.execute('INSERT INTO profiles (user_id, color) VALUES (%s, %s)', (user_id, color))
        db.commit()
    except psycopg2.Error as e:
        print('error adding', str(e))
    return True


def checkUserInSector(cursor, user_id, sector_id):
    cursor.execute(f"SELECT COUNT(*) FROM creatures WHERE user_id='{user_id}' AND sector_id={sector_id}")
    res = cursor.fetchone()
    if res[0] == 0: 
        print(True)
        return True
    return False



def addUserCreaturesAmount(cursor, id_sector, id_user, amount):
    try:
        if checkUserInSector(cursor, id_user, id_sector):
            #print('add creatures')
            cursor.execute( f"INSERT INTO creatures VALUES(%s, %s, %s)", (id_sector, id_user, amount, ) )
            db.commit()
    except psycopg2.Error as e:
        print( 'error adding '+ str(e) )
        return False
    return True



def add_creature(cursor, db):
    
    user_data = create_user_data()
    name, login, hpsw, email = user_data[0], user_data[1], user_data[2], user_data[3]
    add_us = add_user(cursor, db, name, hpsw, login, email)
    user_id = get_userId(login)[0]
    if add_us:
        add_auth = add_auth_user(cursor, db , user_id)

        if add_auth:
            skills = '010100100000'
            skill = skills.index('1')
            abilities = Matrix.get_skill_matrix(str(skill))
            color = random.choice(['красный', 'синий', 'зеленый'])
            add_pr = add_profile(cursor, user_id, color)
            if add_pr:
                if addFirstSkill(cursor, db, user_id, skills, abilities):
                    if addUserCreaturesAmount(cursor, random.randint(228, 300), user_id, random.randint(1, 50)):
                        return 1
                    return 2
                return 3
            return 4
        return 5
    return 6




counter = 20
while counter > 0:
    print(add_creature(cursor, db))
    print('creature added to sector!')
    counter -= 1