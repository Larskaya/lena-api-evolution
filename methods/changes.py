import time, psycopg2
#import flask
from herbivorous import herbivorous_skill
from predators import predators_skill
from fight import fighting


sector_types = {'water': 0, 'forest': 1}
skill_types = {'move': 0, 'herb': 1, 'pred': 2}

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


def get_skills_indexes(skills):
    count = skills.count('1')
    counter = 0
    indexes = []
    while counter < len(skills):
        #print('where while -', counter, 'skills -', skills, len(skills))
        if '1' == skills[counter]:
            print('IF')
            indexes.append(counter)
        counter += 1
    return indexes


def get_sector_type(sector_id):
    cursor.execute(f"SELECT type FROM sectors WHERE id={sector_id}")
    sector_type = cursor.fetchone()[0]
    return sector_type


def get_skills(user_id):
    cursor.execute(f"SELECT skills FROM skills WHERE user_id={user_id}")
    res = cursor.fetchone()
    if res: return res
    return False

def get_creatures():
    cursor.execute(f"SELECT * FROM creatures")
    res = cursor.fetchall()
    if res: return res
    return False


def start_transaction():
    cursor.execute('BEGIN')

def finish_transaction():
    cursor.execute('COMMIT')
    db.commit
  

def main():
    table_data = get_creatures()
    if table_data:
        for record in table_data:
            start_transaction()
            # record: {'sector id': 400, 'user id': 1, 'amount': 55}
            skills = get_skills(record[1]) 
            print('user', record[1], 'with skills', skills)
            indexes = get_skills_indexes(skills[0])

            sector_type = get_sector_type(record[0])

            influence = {'food': 0, 'amount': 0}

            # move
            print('indexes:', indexes)
            if skill_types['move'] in indexes:
                # herbivorous
                if skill_types['herb'] in indexes:
                    # water
                    if sector_type == sector_types['water']:
                        influence['food'] = 2
                    # forest
                    elif sector_type == sector_types['forest']:
                        influence['amount'] = 1
                    herbivorous_skill( db, cursor, record, influence )

                # predators
                if skill_types['pred'] in indexes:
                    # water
                    if sector_type == sector_types['water']:
                        influence['food'] = 1
                    # forest
                    elif sector_type == sector_types['forest']:
                        influence['amount'] = 2
                    predators_skill( db, cursor, record, influence )

            # without move
            else:
                # herbivorous
                if skill_types['herb'] in indexes:
                    herbivorous_skill( db, cursor, record, influence )
                # predators
                elif skill_types['pred'] in indexes:
                    predators_skill( db, cursor, record, influence )
                
            finish_transaction()
                
        
while True:
    main()
    fighting(cursor, db)

    time.sleep(10)