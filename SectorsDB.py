import sqlite3

FIRST_AMOUNT = 1

class SectorsDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


    def getAllData(self):
        try:
            self.__cur.execute(f"SELECT * FROM sectors")
            res = self.__cur.fetchall()
            if res: return res
        except:
            print('error reading from db')
        return []

    def getSectorsUsers(self):
        self.__cur.execute(f"SELECT users FROM sectors")
        res = self.__cur.fetchall()
        if res: return res
        return False

    
    def getSectorsID(self):
        self.__cur.execute(f"SELECT id FROM sectors")
        res = self.__cur.fetchall()
        if res: return res
        return False


    def getSectors(self):
        try:
            self.__cur.execute(f"SELECT * FROM sectors")
            res = self.__cur.fetchall()
            if res: return res
        except: 
            print('error reading from db')
        return []




    def getUsersToSector(self, sector_id):
        try:
            self.__cur.execute( f"SELECT users FROM sectors WHERE id='{sector_id}' " )
            res = self.__cur.fetchall()
            if res: return res
        except: 
            print('error reading from db')
        return []



    def addUserToSector(self, sector_id, user_id):
        try:
            print('add user to sector USER ID', user_id)
            self.__cur.execute( f"UPDATE sectors SET users=users || ', {str(user_id)}', amounts='{user_id}/{FIRST_AMOUNT}' WHERE id='{sector_id}' " )
            self.__db.commit()
        except sqlite3.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True

