from __main__ import get_db
import flask
from flask import g
from database.EvolutionDB import EvolDataBase
from database.SectorsDB import SectorsDataBase
from database.CreaturesDB import CreaturesDataBase

class App():
    def add_profile(id_, type_, color, code):
        g.evolution_db = EvolDataBase( get_db() )
        if g.evolution_db.addProfile(id_, type_, color, code):
            return True
        return False

    def auth(user_id, code):
        g.evolution_db = EvolDataBase( get_db() )
        if g.evolution_db.isAuthValid(user_id, code):
            return True
        return False

    def registration(name, hash, login, email):
        g.evolution_db = EvolDataBase( get_db() )
        if g.evolution_db.addUser( name, hash, login, email ):
            return True
        return False

    def login(login):
        g.evolution_db = EvolDataBase( get_db() )
        print('user id', g.evolution_db.getUserId( login ))
        user_id = g.evolution_db.getUserId( login )[0]
        print('user psw', g.evolution_db.getUserPsw( user_id ))
        user_hpsw = g.evolution_db.getUserPsw( user_id )[0]
        code = g.evolution_db.addAuthUser( user_id )
        if user_id and user_hpsw and code:
            return user_id, user_hpsw, code
        return False

    def add_sector(position_top, position_left, food):
        g.sector_db = SectorsDataBase( get_db() )
        if g.sector_db.addSector(position_top, position_left, int(food)):
            return True
        return False

    def getSectors():
        g.sector_db = SectorsDataBase( get_db() )
        sectors = g.sector_db.getSectors()
        if sectors: return sectors
        else: return False

    def getUserAmountInNeighbors(id_sector, id_user):
        g.sector_db = SectorsDataBase( get_db() )
        ngbrs = g.sector_db.getUserAmountInNeighbors(id_sector, id_user)
        if ngbrs: return ngbrs
        else: return False

    def getNeigborId(left, top):
        g.sector_db = SectorsDataBase( get_db() )
        id_sector = g.sector_db.getNeigborId(left, top)
        if id_sector: return id_sector
        else: return False

    def getSectorPosition(id_sector):
        g.sector_db = SectorsDataBase( get_db() )
        position = g.sector_db.getSectorPosition(id_sector)
        if position: return position 
        else: return False

    def getAllSectorsPositions():
        g.sector_db = SectorsDataBase( get_db() )
        position = g.sector_db.getAllSectorsPositions()
        if position: return position
        else: return False

    def addUserCreaturesAmount(id_sector, id_user, amount, profile_type):
        g.sector_db = SectorsDataBase( get_db() )
        if g.sector_db.addUserCreaturesAmount(id_sector, id_user, amount, profile_type): return True
        else: return False

    def getUserCreaturesAmount(self, id_user, id_sector):
        with app.app_context():
            g.sector_db = SectorsDataBase( get_db() )
        amount = g.sector_db.getUserCreaturesAmount(id_user, id_sector)
        if amount: return amount
        else: return False

    def getSectorFood(id_sector):
        g.sector_db = SectorsDataBase( get_db() )
        food = g.sector_db.getSectorFood(id_sector)
        if food: return food
        else: return False

    def updateSectorFood(id_sector, food):
        g.sector_db = SectorsDataBase( get_db() )
        if g.sector_db.updateSectorFood(id_sector, food): return True
        else: return False

    def getCreatures():
        g.sector_db = SectorsDataBase( get_db() )
        res = g.sector_db.getCreatures()
        if res: return res
        else: return False

    
    def getHerbAmountInSector(sector_id):
        g.sector_db = CreaturesDataBase( get_db() )
        res = g.sector_db.getHerbAmountInSector(sector_id)
        if res: return res
        else: return False


    def dicreaseFood(sector_id):
        g.creatures_db = CreaturesDataBase( get_db() )
        if g.creatures_db.dicreaseFood(sector_id): return True
        else: return False


    def insreaseAmount( sector_id, user_id ):
        g.creatures_db = CreaturesDataBase( get_db() )
        if g.creatures_db.insreaseAmount(sector_id, user_id): return True
        else: return False