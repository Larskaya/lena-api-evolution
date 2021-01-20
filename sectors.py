from __main__ import app
from App import App
import flask, time
from flask import request, jsonify

THRESHOLD_AMOUNT = 50

def get_neighbor_id(left, top):
    n_id = App.getNeigborId(left, top)
    if n_id:
        return n_id[0]
    return None

def get_possible_neighbors(sector_id):
    print('FUNCTION get possible neighbors')
    #print('sector with his type -', sector_id, type(sector_id))
    position = App.getSectorPosition(int(sector_id))
    print('--- position', position)
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
    print('--- get neighbors', neighbors)

    sectors = App.getAllSectorsPositions()
    sectors_list = []
    for sector in sectors:
        sectors_list.append( {'top': int(sector[0]), 'left': int(sector[1]), 'id': sector[2]} )

    answer = []
    for neighbor in neighbors:
        if neighbor['top'] != 0 and neighbor['left'] != 0:
            if neighbor in sectors_list:
                answer.append(neighbor)
    print('--- possible neighbors -', answer)
    return answer


def has_user_enough_amount_in_neighbors(sector_id, user_id):
    print('FUNCTION has user enough...')
    sectors = App.getSectors()
    adjacents = get_possible_neighbors(sector_id)
    print('--- adjacents', adjacents)
    for adj in adjacents:
        amount = App.getUserAmountInNeighbors(adj['id'], user_id)
        print('--- --- amount in neighbors', amount)
        #проверка количества сущетсв пользователя
        if amount and int(amount[0]) >= THRESHOLD_AMOUNT:
            return True
    return False


def is_user_in_any_sector(user_id):
    print('FUNCTION is user in any sector')
    # поиск пользователя по секторам
    sectors_data = App.getCreatures()
    users_in_sectors = []
    print('sectors data', sectors_data)
    if sectors_data:
        for sector in sectors_data:
            print('--- sector', sector)
            users_in_sectors.append(sector[1]) 
        
        print('--- users', users_in_sectors)
        users = ''
        for user in users_in_sectors:
            print('--- --- user data', user, type(user), user_id, type(user_id))
            if user == int(user_id):
                return True
    return False


def sector_id_check(sector_id):
    print('FUNCTION sector id check')
    # проверка введенного id сектора во всех секторах
    sectors_data = App.getSectors()
    print('--- sectors data -', sectors_data)
    if sectors_data:
        for sector in sectors_data:
            id_ = sector[2]
            print('--- --- sector data', id_, type(id_), sector_id, type(sector_id))
            if id_ == int(sector_id):
                return True
    return False

# -------------------------------------------------------------------------------------------------------------
@app.route('/sectors/occupy', methods=['POST']) # to do PUT
def check_of_received_data():
    # получаем данные
    user_id = request.form['user_id']
    sector_id = request.form['sector_id']
    code = request.form['code']
    profile_type = request.form['profile_type']
    # авторизованность
    if not App.auth(user_id, code):
        return jsonify( {"success": False, "error": "unauthorized"} )

    # наличие сектора
    if sector_id_check(sector_id): 
        # пользователя еще нет в секторах    
        if not is_user_in_any_sector(user_id): 
            print('NEW USER')
            App.addUserCreaturesAmount( sector_id, user_id, 1, profile_type )
            return jsonify( {"success": True} )
        else:
            return jsonify( {"success": False, "error": "user is in some sector(not neighbor)"} )

        # найти соседей. добавить, если >50
        if has_user_enough_amount_in_neighbors(sector_id, user_id):
            App.addUserCreaturesAmount( sector_id, user_id, 1, profile_type )
            return jsonify( {"success": True} )
        else:
            return jsonify( {"success": False, "error": "not enough amount in neighbors"} )

    else:
        return jsonify( {"success": False, "error": "sector is not defined"} )

    return jsonify( {"success": False, "error": "cannot add user to sector"} )

