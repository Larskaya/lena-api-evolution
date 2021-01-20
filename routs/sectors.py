from __main__ import app, get_db
from database.SectorsDB import SectorsDataBase
import json

@app.route('/sectors', methods=['GET'])
def get_sectors():
    db = SectorsDataBase( get_db() )

    data = []
    foods = db.getSectorsFood()
    print('food:', foods)
    id_and_users = db.getCreatures()
    print('id and users:', id_and_users)
   
    js = json.dumps(data, sort_keys=True, indent=4)
    return js

# sectors_food [id, food]
# creatures [sector_id, user_id, amount, type]  

