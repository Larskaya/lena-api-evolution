
@app.route('/sector/add', methods=['POST'])
def add_sector():
    db = SectorsDataBase( get_db() )
    f = request.form
    print('FORM -', f)
    res = db.addSector( f['position_top'], f['position_left'], f['users'], f['food'] )
    if res: return jsonify( {"success": True} )
    else: return jsonify( {"success": False} )