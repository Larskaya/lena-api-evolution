from __main__ import app, get_db
from database.Sectors import SectorsDB
import json

@app.route('/sectors', methods=['GET'])
def get_sectors():
    db = SectorsDataBase( get_db() )

    data = []
    sectors_data = db.getSectors()
    creatures = []

    for sector in sectors_data:
        all_creatures = db.getSectorCreatures(sector[0])
        if all_creatures:
            for user_id in all_creatures:
                if user_id:
                    a = db.getCreatureDataByUserId(user_id[0])
                    user_data = {'user_id': user_id[0], 'amount': a[0], 'type': a[1]}
                    creatures.append(user_data)
        else:
            creatures = []
        b = {
            'id': sector[0], 
            'position_top': sector[1],  
            'position_left': sector[2], 
            'food': sector[3],
            'creatures': creatures
        }
        data.append(b)

   
    js = json.dumps(data, indent = 4)
    return js

