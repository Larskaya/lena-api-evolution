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
        self.__cur.execute( f"SELECT position_top, position_left FROM sectors_position WHERE id='{sector_id}' " )
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

    def getSectors(self):
        self.__cur.execute(f"SELECT * FROM sectors_position")
        res = self.__cur.fetchall()
        if res: return res
        return False


    def getSectorFood(self, id):
        self.__cur.execute(f"SELECT food FROM sectors_food WHERE id='{id}'")
        res = self.__cur.fetchone()
        #print('result 1 -', res)
        if res: return res
        return False

    def getCreatures(self):
        self.__cur.execute(f"SELECT * FROM creatures")
        res = self.__cur.fetchall()
        if res: return res
        return False



    # def updateSectorFood(self, id_, food):
    #     try:
    #         print('is ID and FOOD -', type(id_), type(food))
    #         self.__cur.execute("UPDATE sectors_food SET food=(%s) WHERE id=(%s)", (food, id_))
    #         self.__db.commit()
    #         res = self.__cur.fetchone()
    #         print('result 2 -', res)
    #         #self.__db.close()
    #     except psycopg2.Error as e:
    #         print( 'error adding '+ str(e) )
    #         return False
    #     return True


    # def updateUserCreaturesAmount(self, id_user, id_sector, amount):
    #     try:
    #         print('update amount')
    #         self.__cur.execute("UPDATE creatures SET amount=(%s) WHERE id_sector=(%s) AND id_user=(%s)", (amount, id_sector, id_user))
    #         self.__db.commit()
    #         res = self.__cur.fetchone()
    #     except psycopg2.Error as e:
    #         #print( 'error adding '+ str(e) )
    #         return False
    #     # finally:
    #     #     self.__db.close()
    #     return True


    # def updateUserCreaturesAmount(self):
    #     try:
    #         self.__cur.execute("UPDATE creatures SET amount=amount+1")
    #         self.__db.commit()
    #         res = self.__cur.fetchall()
    #     except psycopg2.Error as e:
    #         return False
    #     return True



    def addSector(self, positionTop, positionLeft, food):
        try:
            self.__cur.execute("INSERT INTO sectors_position (position_left, position_top) VALUES (%s, %s)", 
            (positionLeft, positionTop)) 
            print('type of food', food, type(food))
            self.__cur.execute("INSERT INTO sectors_food (food) VALUES (%s)", (food,)) 
            self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True



    def addUserToSector(self, sector_id, user_id, amount):
        try:
            self.__cur.execute("INSERT INTO creatures (id_sector, id_user, amount) VALUES (%s, %s, %s)", 
            (sector_id, user_id, amount) )
            self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True




    def getAllSectorsPositions(self):
        try:
            #print('sector id where position', sector_id)
            self.__cur.execute( f"SELECT * FROM sectors_position " )
            res = self.__cur.fetchall()
            if res: return res
        except: 
            print('error reading from db')
        return []



    def checkUserInSector(self, user_id, sector_id):
            self.__cur.execute(f"SELECT COUNT(*) FROM creatures WHERE id_user='{user_id}' AND id_sector={sector_id}")
            res = self.__cur.fetchone()
            print('check user in sector', res)
            if res[0] == 0: 
                print(True)
                return True
            return False

    def addUserCreaturesAmount(self, id_sector, id_user, amount):
        try:
            #print('before check')
            if self.checkUserInSector(id_user, id_sector):
                #print('user:', id_user, 'sector:', id_sector, 'amount:', amounts)
                print('add creatures')
                self.__cur.execute( f"INSERT INTO creatures VALUES(%s, %s, %s)", (id_sector, id_user, amount, ) )
                self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True



    def getUserAmountInNeighbors(self, id_sector, id_user):
        try:
            print('id sector', id_sector, 'id user:', id_user, 'add in DB')
            self.__cur.execute( f"SELECT amount FROM creatures WHERE id_sector='{id_sector}' AND id_user='{id_user}' " )
            res = self.__cur.fetchone()
            if res: return res
        except: 
            print('error reading from db')
        return []




    def getNeigborId(self, left, top):  
        try:
            self.__cur.execute( f"SELECT id FROM sectors_position WHERE position_left='{left}' AND position_top='{top}' " )
            res = self.__cur.fetchone()
            if res: return res
        except: 
            print('error reading from db')
        return []



    def getUserCreaturesAmount(self, id_user, id_sector):
        try:
            self.__cur.execute( f"SELECT amount FROM creatures WHERE id_user='{id_user}' AND id_sector='{id_sector}' " )
            res = self.__cur.fetchone()
            #self.__db.close()
            if res: return res
        except: 
            print('error reading from db')
        return []





    # def getSectorUsers(self, id_sector):
    #     try:
    #         self.__cur.execute( f"SELECT users FROM sectors WHERE id='{id_sector}' " )
    #         res = self.__cur.fetchone()
    #         if res: return res
    #     except: 
    #         print('error reading from db')
    #     return []


