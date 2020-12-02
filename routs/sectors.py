from __main__ import app, get_db
from database.SectorsDB import SectorsDataBase
#from SectorsDB import SectorsDataBase

@app.route('/sectors', methods=['GET'])
def get_sectors():
    db = SectorsDataBase( get_db() )
    data = []
    for s in db.getSectors():
        sector = {'sector': ( s['id'], s['users'], s['food'])}
        data.append(sector)
    js = json.dumps(data, sort_keys=True, indent=4)
    return js

