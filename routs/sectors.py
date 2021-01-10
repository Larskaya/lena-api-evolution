from __main__ import app, connect_db
from database.SectorsDB import SectorsDataBase

@app.route('/sectors', methods=['GET'])
def get_sectors():
    db = SectorsDataBase( connect_db() )
    data = []
    for s in db.getSectors():
        sector = {'sector': ( s['id'], s['users'], s['food'])}
        data.append(sector)
    js = json.dumps(data, sort_keys=True, indent=4)
    return js
