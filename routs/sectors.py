from __main__ import app, get_db
from database.Creatures import CreaturesDB
from database.Sectors import SectorsDB
import json

@app.route('/sectors', methods=['GET'])
def get_sectors():
    db1 = CreaturesDB( get_db() )
    db2 = SectorsDB( get_db() )

    data = []
    sectors_data = db2.getSectors()
    creatures = []

    for sector in sectors_data:
        all_creatures = db1.getSectorCreatures(sector[0])
        if all_creatures:
            for user_id in all_creatures:
                if user_id:
                    a = db1.getCreatureDataByUserId(user_id[0])
                    user_data = {'user_id': user_id[0], 'amount': a[0], 'type': a[1]}
                    creatures.append(user_data)
        else:
            creatures = []
        b = {
            'id': sector[0], 
            'position_top': sector[1],  
            'position_left': sector[2], 
            'food': sector[3],
            'type': sector[4],
            'creatures': creatures
        }
        data.append(b)

    
    js = json.dumps(data, indent = 4)
    return js

