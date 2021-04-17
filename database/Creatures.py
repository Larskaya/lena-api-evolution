import psycopg2

class CreaturesDB:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getCreatures(self):
        self.__cur.execute(f"SELECT * FROM creatures")
        res = self.__cur.fetchall()
        if res: return res
        return False

    def getUserCreaturesAmount(self, id_user, id_sector):
        try:
            self.__cur.execute( f"SELECT amount FROM creatures WHERE user_id='{id_user}' AND sector_id='{id_sector}' " )
            res = self.__cur.fetchone()
            if res: return res
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) ) 
        return []

    def getSectorCreatures(self, sector_id):
        self.__cur.execute( f"SELECT user_id FROM creatures WHERE sector_id='{sector_id}' " )
        res = self.__cur.fetchall()
        if res: return res

    def getCreatureDataByUserId(self, user_id):
        self.__cur.execute(f"SELECT amount, type FROM creatures WHERE user_id='{user_id}'")
        res = self.__cur.fetchone()
        if res: return res
        return []

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

    def addUserToSector(self, sector_id, user_id, amount, profile_type):
        try:
            self.__cur.execute("INSERT INTO creatures (sector_id, user_id, amount, type) VALUES (%s, %s, %s, %s)", 
            (sector_id, user_id, amount, profile_type) )
            self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True

    def checkUserInSector(self, user_id, sector_id):
        self.__cur.execute(f"SELECT COUNT(*) FROM creatures WHERE user_id='{user_id}' AND sector_id={sector_id}")
        res = self.__cur.fetchone()
        print('check user in sector', res)
        if res[0] == 0: 
            print(True)
            return True
        return False

    def addUserCreaturesAmount(self, id_sector, id_user, amount):
        try:
            if self.checkUserInSector(id_user, id_sector):
                print('add creatures')
                self.__cur.execute( f"INSERT INTO creatures VALUES(%s, %s, %s)", (id_sector, id_user, amount, ) )
                self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True
