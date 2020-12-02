from __main__ import app, get_db
from database.SectorsDB import SectorsDataBase
from database.EvolDataBase import EvolDataBase


import flask
from flask import request, jsonify

from food_change import increase_the_food

THRESHOLD_AMOUNT = 50



dbase = None
@app.before_request
def before_request():
    global dbase 
    db = get_db()
    dbase = SectorsDataBase(db)



def get_neighbor_id(left, top):
    n_id = dbase.getNeigborId(left, top)
    if n_id:
        return n_id[0]
    return None



def get_possible_neighbors(sector_id):
    print('sector with his type -', sector_id, type(sector_id))
    position = dbase.getSectorPosition(int(sector_id))
    print('position', position)
    position = position[0]
    top = position[0]
    left = position[1]
    left1 = int(left) - 1
    left2 = int(left) + 1
    top1 = int(top)
    top2 = int(top)

    left3 = int(left)
    left4 = int(left) 
    top3 = int(top) - 1
    top4 = int(top) + 1

    neighbors = []
    neighbors.append( {'top': top1, 'left': left1, 'id': get_neighbor_id(top1, left1) } )
    neighbors.append( {'top': top2, 'left': left2, 'id': get_neighbor_id(top2, left2) } )
    neighbors.append( {'top': top3, 'left': left3, 'id': get_neighbor_id(top3, left3) } )
    neighbors.append( {'top': top4, 'left': left4, 'id': get_neighbor_id(top4, left4) } )

    sectors = dbase.getAllSectorsPositions()
    sectors_list = []
    for sector in sectors:
        sectors_list.append( {'top': int(sector[0]), 'left': int(sector[1]), 'id': sector[2]} )

    answer = []
    for neighbor in neighbors:
        if neighbor['top'] != 0 and neighbor['left'] != 0:
            if neighbor in sectors_list:
                answer.append(neighbor)
    print('possible neighbors -', answer)
    return answer



def has_user_enough_amount_in_neighbors(sector_id, user_id):
    sectors = dbase.getSectors()
    adjacents = get_possible_neighbors(sector_id)
    # for adj in adjacents:
    #     amount = dbase.getUserAmountsInNeighbors(adj['id'], user_id)
    #     print('AMOUNT USER', amount, '+', adj['id'])
    #     if amount:
    #         if int(amount[0]) >= THRESHOLD_AMOUNT:
    #             dbase.addUserToSector(sector_id, user_id)
    #             dbase.addUserCreaturesAmount(sector_id, user_id, 1) 
    #             return True
    return False



def is_user_in_any_sector(user_id):
    # поиск пользователя по секторам
    sectors_data = dbase.getSectorsData()
    users_in_sectors = []
    for sector in sectors_data:
        users_in_sectors.append(sector[3]) 
    
    print('users -', users_in_sectors)
    users = ''
    for user in users_in_sectors:
        print(user, type(user), user_id, type(user_id))
        if user == int(user_id):
            return True
    return False

def sector_id_check(sector_id):
    # проверка введенного id сектора во всех секторах
    sectors_data = dbase.getSectorsData()
    for sector in sectors_data:
        id_ = sector[0]
        if id_ == int(sector_id):
            return True
    return False


def add_user_to_sector(user_id, sector_id, code):
    print(1, sector_id_check(sector_id))
    if sector_id_check(sector_id):
        print(2, is_user_in_any_sector(user_id))
        if is_user_in_any_sector(user_id):

            print(3, has_user_enough_amount_in_neighbors(sector_id, user_id))
            if has_user_enough_amount_in_neighbors(sector_id, user_id):
                dbase.addUserToSector( sector_id, user_id )
                print(True, 'where amount >= 50')
                return True
        else:
            dbase.addUserToSector( sector_id, user_id )
        # dbase.addUserCreaturesAmount( sector_id, user_id, 1 )
        print(True, 'where amount = 0')
        return True
    return jsonify( {"success": False, "error": "choose another sector"} )


@app.route('/sectors/occupy', methods=['POST']) # to do PUT
def addMAIN():
    user_id = request.form['user_id']
    sector_id = request.form['sector_id']
    code = request.form['code']
    db = EvolDataBase( get_db() )

    if not db.isAuthValid(user_id, code):
        return jsonify( {"success": False, "error": "not authorized"} )
    if add_user_to_sector(user_id, sector_id, code):
        increase_the_food(sector_id)
        return jsonify( {"success": True} )
    return jsonify( {"success": False, "error": "cannot add user to sector"} )







