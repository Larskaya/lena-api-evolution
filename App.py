from __main__ import get_db
import flask
from flask import g
from database.Creatures import CreaturesDB
from database.Sectors import SectorsDB
from database.Users import UsersDB
from database.Profiles import ProfilesDB
from database.Messages import MessagesDB 

class App():
    def add_profile(id_, type_, color, code):
        g.data = ProfilesDB( get_db() )
        if g.data.addProfile(id_, type_, color, code):
            return True
        return False

    def auth(user_id, code):
        g.data = UsersDB( get_db() )
        if g.data.isAuthValid(user_id, code):
            return True
        return False

    def registration(name, hash, login, email):
        g.data = UsersDB( get_db() )
        if g.data.addUser( name, hash, login, email ):
            return True
        return False

    def login(login):
        g.data = UsersDB( get_db() )
        user_id = g.data.getUserId( login )[0]
        user_hpsw = g.data.getUserPsw( user_id )[0]
        code = g.data.addAuthUser( user_id )
        if user_id and user_hpsw and code:
            return user_id, user_hpsw, code
        return False

    def add_sector(position_top, position_left, food):
        g.data = SectorsDB( get_db() )
        if g.data.addSector(position_top, position_left, int(food)):
            return True
        return False

    def getSectors():
        g.data = SectorsDB( get_db() )
        sectors = g.data.getSectors()
        if sectors: return sectors
        else: return False

    def getUserAmountInNeighbors(id_sector, id_user):
        g.data = SectorsDB( get_db() )
        ngbrs = g.data.getUserAmountInNeighbors(id_sector, id_user)
        if ngbrs: return ngbrs
        else: return False

    def getNeigborId(left, top):
        g.data = SectorsDB( get_db() )
        id_sector = g.data.getNeigborId(left, top)
        if id_sector: return id_sector
        else: return False

    def addUserCreaturesAmount(id_sector, id_user, amount, profile_type):
        g.data = CreaturesDB( get_db() )
        if g.data.addUserCreaturesAmount(id_sector, id_user, amount, profile_type): return True
        else: return False

    def getUserCreaturesAmount(self, id_user, id_sector):
        with app.app_context():
            g.data = CreaturesDB( get_db() )
        amount = g.data.getUserCreaturesAmount(id_user, id_sector)
        if amount: return amount
        else: return False

    def getSectorFood(id_sector):
        g.data = SectorsDB( get_db() )
        food = g.data.getSectorFood(id_sector)
        if food: return food
        else: return False
        
    def getCreatures():
        g.data = CreaturesDB( get_db() )
        res = g.data.getCreatures()
        if res: return res
        else: return False

    