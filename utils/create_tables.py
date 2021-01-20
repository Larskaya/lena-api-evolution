

def create_db():
    db = connect_db()
    with app.open_resource('utils/create_tables.sql', mode='r') as f:
        db.cursor().execute(f.read())
    db.commit()
    db.close()