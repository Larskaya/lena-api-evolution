import psycopg2

class SectorsDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()
    
    def getSectorPosition(self, sector_id):
        self.__cur.execute( f"SELECT position_top, position_left FROM sectors_position WHERE id='{sector_id}'" )
        res = self.__cur.fetchall()
        if res: return res

    def getSectorData(self, sector_id):
        self.__cur.execute(f"SELECT * FROM sectors WHERE id='{id}'")
        res = self.__cur.fetchone()
        if res: return res
        return False

    def getSectors(self):
        self.__cur.execute(f"SELECT * FROM sectors")
        res = self.__cur.fetchall()
        if res: return res
        return False

    def getSectorFood(self, id):
        self.__cur.execute(f"SELECT food FROM sectors WHERE id='{id}'")
        res = self.__cur.fetchone()
        if res: return res
        return False

    def getSectorsFood(self):
        self.__cur.execute(f"SELECT id, food FROM sectors")
        res = self.__cur.fetchall()
        if res: return res
        return False

    def getCreatures(self):
        self.__cur.execute(f"SELECT * FROM creatures")
        res = self.__cur.fetchall()
        if res: return res
        return False

    def getSectorId(self, top, left):
        self.__cur.execute(f"SELECT id FROM sectors WHERE position_top={top} AND position_left={left}")
        res = self.__cur.fatchone()
        if res: return res
        return False


    def addSector(self, positionTop, positionLeft, food):
        try:
            self.__cur.execute("INSERT INTO sectors (position_left, position_top, food) VALUES (%s, %s, %s)", 
            (positionLeft, positionTop, food)) 
            #sector_id = self.getSectorId(top, left)
            #self.__cur.execute("INSERT INTO sectors (food) VALUES (%s)", (food,)) 
            self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True





    def addUserToSector(self, sector_id, user_id, amount, profile_type):
        try:
            self.__cur.execute("INSERT INTO creatures (sector_id, user_id, amount, type) VALUES (%s, %s, %s, %s)", 
            (sector_id, user_id, amount, profile_type) )
            self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True

    def getAllSectorsPositions(self):
        try:
            self.__cur.execute( f"SELECT id, position_top, position_left FROM sectors " )
            res = self.__cur.fetchall()
            if res: return res
        except: 
            print('error reading from db')
        return []

    def checkUserInSector(self, user_id, sector_id):
            self.__cur.execute(f"SELECT COUNT(*) FROM creatures WHERE user_id='{user_id}' AND sector_id={sector_id}")
            res = self.__cur.fetchone()
            print('check user in sector', res)
            if res[0] == 0: 
                print(True)
                return True
            return False




    def addUserCreaturesAmount(self, id_sector, id_user, amount, profile_type):
        #if profile_type == 'хищник':
        try:
            if self.checkUserInSector(id_user, id_sector):
                print('add creatures')
                self.__cur.execute( f"INSERT INTO creatures VALUES(%s, %s, %s, %s)", (id_sector, id_user, amount, profile_type, ) )
                self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True







    def getUserAmountInNeighbors(self, id_sector, id_user):
        try:
            print('id sector', id_sector, 'id user:', id_user, 'add in DB')
            self.__cur.execute( f" SELECT amount FROM creatures WHERE sector_id='{id_sector}' AND user_id='{id_user}' " )
            res = self.__cur.fetchone()
            if res: return res
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) ) 
            print('error reading from db')
        return []

    def getNeigborId(self, left, top):  
        try:
            self.__cur.execute( f"SELECT id FROM sectors WHERE position_left='{left}' AND position_top='{top}' " )
            res = self.__cur.fetchone()
            if res: return res
        except: 
            print('error reading from db')
        return []

    def getUserCreaturesAmount(self, id_user, id_sector):
        try:
            self.__cur.execute( f"SELECT amount FROM creatures WHERE user_id='{id_user}' AND sector_id='{id_sector}' " )
            res = self.__cur.fetchone()
            if res: return res
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) ) 
            #print('error reading from db')
        return []




    def getSectorCreatures(self, sector_id):
        #try:
        self.__cur.execute( f"SELECT user_id FROM creatures WHERE sector_id='{sector_id}' " )
        res = self.__cur.fetchall()
        if res: return res



    def getCreatureDataByUserId(self, user_id):
        self.__cur.execute(f"SELECT amount, type FROM creatures WHERE user_id='{user_id}'")
        res = self.__cur.fetchone()
        if res: return res
        return []