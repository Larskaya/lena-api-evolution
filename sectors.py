from __main__ import app, get_db
from SectorsDB import SectorsDataBase
from EvolDataBase import EvolDataBase

import flask
from flask import request, jsonify


THRESHOLD_AMOUNT = 50



dbase = None
@app.before_request
def before_request():
    global dbase 
    db = get_db()
    dbase = SectorsDataBase(db)

def get_possible_neighbors_ids(sector_id, sectors):
    res = []
    #print('SECTOR ID:', sector_id)
    x1 = int(sector_id[0]) - 1
    x2 = int(sector_id[0]) + 1
    y1 = int(sector_id[1])
    y2 = int(sector_id[1])

    res.append('{0}/{1}'.format(x1, y1))
    res.append('{0}/{1}'.format(x2, y2))

    x1 = int(sector_id[0]) 
    x2 = int(sector_id[0]) 
    y1 = int(sector_id[1]) + 1
    y2 = int(sector_id[1]) - 1

    res.append('{0}/{1}'.format(x1, y1))
    res.append('{0}/{1}'.format(x2, y2))

    answer = []
    for adj in res:
        for sec in sectors:
            #print('sector:', sec['id'])
            if sec['id'] == adj:
                answer.append(adj)
    print('answer where adj -', answer)
    return answer

def has_user_enough_amount_in_neighbors(sector_id, user_id):
    sector_id = sector_id.split('/')
    sectors = dbase.getSectors()
    adjacents_ids = get_possible_neighbors_ids(sector_id, sectors)
    print('all sectors:', sectors)
    print('ADJ -', adjacents_ids)
    for sector in sectors:
        print('sector data', sector['id'], sector['amounts'])
        if sector['id'] in adjacents_ids and str(user_id) in sector['users']:
            amounts = sector['amounts'].split(',')
            for amount in amounts:
                amount_user = amount.split('/')[0]
                amount_amount = amount.split('/')[1]

                if amount_user == user_id and int(amount_amount) >= THRESHOLD_AMOUNT:
                    return True
    return False

def is_user_in_any_sector(user_id):
    users_in_sectors = dbase.getSectorsUsers()
    print('users in sector:', users_in_sectors)
    users = ''
    for user in users_in_sectors:
        print('USER',user[0], str(user_id))
        if str(user_id) in str(user[0]):
            return True
    return False

def sector_id_check(sector_id):
    ids = dbase.getSectorsID()
    ids_lst = []
    for id in ids:
        ids_lst.append(id[0])
    if sector_id in ids_lst:
        return True
    return False


def add_user_to_sector(user_id, sector_id, code):
    #print('isAuthValid', db.isAuthValid(user_id, code))
    if sector_id_check(sector_id):
        print(2, is_user_in_any_sector(user_id))
        if is_user_in_any_sector(user_id):
            if has_user_enough_amount_in_neighbors(sector_id, user_id):
                dbase.addUserToSector( sector_id, user_id )
                return True
        else:
            dbase.addUserToSector( sector_id, user_id )
            return True
    return False


@app.route('/sectors/occupy', methods=['POST']) # to do PUT
def addMAIN():
    user_id = request.form['user_id']
    sector_id = request.form['sector_id']
    code = request.form['code']
    db = EvolDataBase( get_db() )
    if not db.isAuthValid(user_id, code):
        return jsonify( {"success": False, "error": "not authorized"} )

    #print('first func -', add_user_to_sector(user_id, sector_id, code))
    #print('second func -', has_user_enough_amount_in_neighbors(sector_id, user_id))


    if add_user_to_sector(user_id, sector_id, code):
        return jsonify( {"success": True} )

    #elif has_user_enough_amount_in_neighbors(sector_id, user_id):
    #       return jsonify( {"success": True} )

    return jsonify( {"success": False, "error": "cannot add user to sector"} )
