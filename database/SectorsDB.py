import psycopg2
from datetime import datetime

FIRST_AMOUNT = 1

class SectorsDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    # def getSectorsUsers(self):
    #     self.__cur.execute(f"SELECT users FROM sectors")
    #     res = self.__cur.fetchall()
    #     if res: return res
    #     return False

    
    def getSectorPosition(self, sector_id):
        #print('sector id where position', sector_id)
        self.__cur.execute( f"SELECT positionTop, positionLeft FROM sectors WHERE id='{sector_id}' " )
        res = self.__cur.fetchall()
        if res: return res



    def getSectorData(self, sector_id):
        try:
            print('ID HERE -', sector_id)
            self.__cur.execute(f"SELECT * FROM sectors WHERE id='{id}'")
            res = self.__cur.fetchone()
            if res: return res
            return False
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return False

    def getSectorsData(self):
        self.__cur.execute(f"SELECT * FROM sectors")
        res = self.__cur.fetchall()
        if res: return res
        return False

    def getSectorFood(self, id):
        self.__cur.execute(f"SELECT food FROM sectors WHERE id='{id}'")
        res = self.__cur.fetchone()
        print('result 1 -', res)
        if res: return res
        return False


    def updateSectorFood(self, id_, food):
        try:
            print('is ID and FOOD -', type(id_), type(food))
            self.__cur.execute("UPDATE sectors SET food=(%s) WHERE id=(%s)", (food, id_))
            self.__db.commit()
            res = self.__cur.fetchone()
            print('result 2 -', res)
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True


    def getSectors(self):
        try:
            self.__cur.execute(f"SELECT * FROM sectors")
            res = self.__cur.fetchall()
            if res: return res
        except: 
            print('error reading from db')
        return []



    def addSector(self, positionTop, positionLeft, users, food):
        try:
            self.__cur.execute("INSERT INTO sectors (positionTop, positionLeft, users, food) VALUES (%s, %s, %s, %s)", 
            (positionTop, positionLeft, users, food)) 
            self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True



    def checkUserInSector(self, user_id):
        self.__cur.execute(f"SELECT COUNT(*) FROM creatures WHERE id_user='{user_id}' ")
        res = self.__cur.fetchone()
        if res: return False
        return True


    def addUserToSector(self, sector_id, user_id):
        try:
            self.__cur.execute( f"UPDATE sectors SET users='{user_id} ' WHERE id='{sector_id}' " )
            self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True




    def getAllSectorsPositions(self):
        try:
            #print('sector id where position', sector_id)
            self.__cur.execute( f"SELECT positionTop, positionLeft, id FROM sectors " )
            res = self.__cur.fetchall()
            if res: return res
        except: 
            print('error reading from db')
        return []


    def addUserCreaturesAmount(self, id_sector, id_user, amounts):
        try:
            if self.checkUserInSector(id_user):
                #print('user:', id_user, 'sector:', id_sector, 'amount:', amounts)
                self.__cur.execute( f"INSERT INTO creatures VALUES(%s, %s, %s)", (id_sector, id_user, amounts, ) )
                self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True



    def getUserAmountsInNeighbors(self, id_sector, id_user):
        try:
            print('id sector', id_sector, 'id user:', id_user, 'add in DB')
            self.__cur.execute( f"SELECT amounts FROM creatures WHERE id_sector='{id_sector}' AND id_user='{id_user}' " )
            res = self.__cur.fetchone()
            if res: return res
        except: 
            print('error reading from db')
        return []




    def getNeigborId(self, left, top):  
        try:
            self.__cur.execute( f"SELECT id FROM sectors WHERE positionLeft='{left}' AND positionTop='{top}' " )
            res = self.__cur.fetchone()
            if res: return res
        except: 
            print('error reading from db')
        return []

