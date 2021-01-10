from __main__ import connect_db#, app
import flask
from flask import g
from database.EvolutionDB import EvolDataBase
from database.SectorsDB import SectorsDataBase

class App():

    def auth(user_id, code):
        g.evolution_db = EvolDataBase( connect_db() )
        if g.evolution_db.isAuthValid(user_id, code):
            return True
        return False

    def registration(name, hash, login, email):
        g.evolution_db = EvolDataBase( connect_db() )
        if g.evolution_db.addUser( name, hash, login, email ):
            return True
        return False

    def login(login):
        g.evolution_db = EvolDataBase( connect_db() )
        user_id = g.evolution_db.getUserId( login )[0]
        #user_id = user_id[0]
        #print('user id', user_id)
        user_hpsw = g.evolution_db.getUserPsw( user_id )[0]
        #print('hpsw', user_hpsw)
        code = g.evolution_db.addAuthUser( user_id )

        print(user_id, user_hpsw, code)

        if user_id and user_hpsw and code:
            return user_id, user_hpsw, code
        return False


    def add_sector(position_top, position_left, food):
        g.sector_db = SectorsDataBase( connect_db() )
        if g.sector_db.addSector(position_top, position_left, int(food)):
            return True
        return False

    def getSectors():
        g.sector_db = SectorsDataBase( connect_db() )
        sectors = g.sector_db.getSectors()
        if sectors: return sectors
        else: return False

    def getUserAmountInNeighbors(id_sector, id_user):
        g.sector_db = SectorsDataBase( connect_db() )
        ngbrs = g.sector_db.getUserAmountInNeighbors(id_sector, id_user)
        if ngbrs: return ngbrs
        else: return False

    def getNeigborId(left, top):
        g.sector_db = SectorsDataBase( connect_db() )
        id_sector = g.sector_db.getNeigborId(left, top)
        if id_sector: return id_sector
        else: return False

    def getSectorPosition(id_sector):
        g.sector_db = SectorsDataBase( connect_db() )
        position = g.sector_db.getSectorPosition(id_sector)
        if position: return position 
        else: return False

    # def addUserToSector(id_sector, id_user, amount):
    #     g.sector_db = SectorsDataBase( get_db() )
    #     if g.sector_db.addUserToSector(id_sector, id_user, amount): return True
    #     else: return False

    def getAllSectorsPositions():
        g.sector_db = SectorsDataBase( connect_db() )
        position = g.sector_db.getAllSectorsPositions()
        if position: return position
        else: return False

    def addUserCreaturesAmount(id_sector, id_user, amount):
        g.sector_db = SectorsDataBase( connect_db() )
        if g.sector_db.addUserCreaturesAmount(id_sector, id_user, amount): return True
        else: return False



    #@app.teardown_appcontext
    def getUserCreaturesAmount(self, id_user, id_sector):
        with app.app_context():
            #db = getattr(g, '_database', None)
            g.sector_db = SectorsDataBase( connect_db() )
            #g.sector_db = SectorsDataBase(db)
        #amount = 0
        amount = g.sector_db.getUserCreaturesAmount(id_user, id_sector)
        if amount: return amount
        else: return False

    #@app.teardown_appcontext
    # def updateUserCreaturesAmount(self):
    #     with app.app_context():
    #         g.sector_db = SectorsDataBase( connect_db() )
    #         res = g.sector_db.updateUserCreaturesAmount()
    #     if res: return res
    #     else: return False

    def getSectorFood(id_sector):
        g.sector_db = SectorsDataBase( connect_db() )
        food = g.sector_db.getSectorFood(id_sector)
        if food: return food
        else: return False






    # def getSectorUsers(id_sector):
    #     g.sector_db = SectorsDataBase( get_db() )
    #     users = g.sector_db.getSectorUsers(id_sector)
    #     if users: return users
    #     else: return False






    def updateSectorFood(id_sector, food):
        g.sector_db = SectorsDataBase( connect_db() )
        if g.sector_db.updateSectorFood(id_sector, food): return True
        else: return False



    def getCreatures():
        g.sector_db = SectorsDataBase( connect_db() )
        res = g.sector_db.getCreatures()
        if res: return res
        else: return False