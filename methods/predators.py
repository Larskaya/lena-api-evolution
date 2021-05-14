from decrease_predators import decrease_predators
import psycopg2
import random

def get_skills(cursor, user_id):
    cursor.execute(f"SELECT skills FROM skills WHERE user_id={user_id}")
    skills = cursor.fetchone()[0]
    if skills: return skills
    return None


def get_skills_indexes(skills):
    count = skills.count('1')
    counter = 0
    indexes = []
    while counter < len(skills):
        if '1' == skills[counter]:
            indexes.append(counter)
        counter += 1
    if indexes: return indexes
    else: return None


def get_creatures_in_sector( cursor, sector_id ):
    cursor.execute(f"SELECT user_id FROM creatures WHERE sector_id = {sector_id}")
    users = cursor.fetchall()
    if users: return users
    return False


def get_herb(cursor, creature):
    skills = get_skills(cursor, creature)
    indexes = get_skills_indexes(skills)
    if 0 in indexes or 1 in indexes: return True
    elif 0 in indexes and 1 in indexes: return True
    return False


def deleteCreatures(cursor, user_id, sector_id):
    try:
        cursor.execute(f"DELETE FROM creatures WHERE user_id={user_id} AND sector_id={sector_id}")
    except psycopg2.Error as e:
        print('Error', str(e))
        return False
    return True


def is_there_enough_amount( cursor, num, herb_id, sector_id ):
    cursor.execute(f"SELECT amount FROM creatures WHERE user_id={herb_id} AND sector_id={sector_id}")
    amount = cursor.fetchone()
    if amount: 
        if amount[0] - num > 0: return True
        elif amount[0] - num == 0: return deleteCreatures(cursor, herb_id, sector_id)
    return False


def decrease_herb(db, cursor, herb_id, sector_id, infl_a):
    try:
        a = 1 + infl_a
        if is_there_enough_amount( cursor, a, herb_id, sector_id ):
            cursor.execute("UPDATE creatures SET amount = amount - (%s) WHERE user_id = (%s) AND sector_id = (%s)", (a, herb_id, sector_id, ))
            db.commit()
        else:
            decrease_predators(db, cursor, sector_id)
            return False

    except psycopg2.Error as e:
        print('error', str(e))
        return False
    return True

def increase_pred(db, cursor, pred_id, sector_id, infl_a):
    try:
        a = 1 + infl_a
        cursor.execute("UPDATE creatures SET amount = amount + (%s) WHERE user_id = (%s) AND sector_id = (%s)", (a, pred_id, sector_id))
        db.commit()
    except psycopg2.Error as e:
        print('error', str(e))
        return False
    return True




def predators_skill( db, cursor, record, influence ):
    creatures = get_creatures_in_sector( cursor, record[0] )
    herbs = []
    herb = ''
    for creature in creatures:
        if get_herb(cursor, creature[0]):
            herbs.append(creature[0])
    if herbs: herb = random.choice(herbs) 
    infl_a = influence['amount']
    if herb:
        if decrease_herb(db, cursor, int(herb), record[0], infl_a): increase_pred(db, cursor, record[1], record[0], infl_a)


