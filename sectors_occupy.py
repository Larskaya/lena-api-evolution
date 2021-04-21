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
    position = App.getSectorPosition(int(sector_id))
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

    sectors = App.getAllSectorsPositions()
    sectors_list = []
    for sector in sectors:
        sectors_list.append( {'top': int(sector[0]), 'left': int(sector[1]), 'id': sector[2]} )

    answer = []
    for neighbor in neighbors:
        if neighbor['top'] != 0 and neighbor['left'] != 0:
            if neighbor in sectors_list:
                answer.append(neighbor)
    return answer


def has_user_enough_amount_in_neighbors(sector_id, user_id):
    sectors = App.getSectors()
    adjacents = get_possible_neighbors(sector_id)
    for adj in adjacents:
        amount = App.getUserAmountInNeighbors(adj['id'], user_id)
        if amount and int(amount[0]) >= THRESHOLD_AMOUNT:
            return True
    return False


def is_user_in_any_sector(user_id):
    sectors_data = App.getCreatures()
    users_in_sectors = []
    if sectors_data:
        for sector in sectors_data:
            users_in_sectors.append(sector[1]) 
        
        for user in users_in_sectors:
            if user == user_id[0]:
                return True
    return False


def sector_id_check(sector_id):
    sectors_data = App.getSectors()
    if sectors_data:
        for sector in sectors_data:
            id_ = sector[0]
            if id_ == int(sector_id):
                print('sector id = =',id_)
                return True
    return False




def check_cookies():
    if request.cookies.get('user_id') and request.cookies.get('code'):
        print('request: cookies and codes is got!')
        return True
    return False



# -------------------------------------------------------------------------------------------------------------
@app.route('/sectors/occupy', methods=['POST']) # to do PUT
def check_of_received_data():
    user_id = request.form['user_id'] 
    sector_id = request.form['sector_id']

    #code = request.form['code'] 

    if not check_cookies():
        return jsonify( {'error': 'in cookies'} )


    # if not App.auth(user_id, code):
    #     return jsonify( {"success": False, "error": "unauthorized"} )

    if sector_id_check(sector_id): 
        if not is_user_in_any_sector(user_id): 
            App.addUserCreaturesAmount( sector_id, user_id, 1)
            return jsonify( {"success": True} )
        else:
            return jsonify( {"success": False, "error": "user is in some sector(not neighbor)"} )

        if has_user_enough_amount_in_neighbors(sector_id, user_id):
            App.addUserCreaturesAmount( sector_id, user_id, 1)
            return jsonify( {"success": True} )
        else:
            return jsonify( {"success": False, "error": "not enough amount in neighbors"} )

    else:
        return jsonify( {"success": False, "error": "sector is not defined"} )

    return jsonify( {"success": False, "error": "cannot add user to sector"} )

