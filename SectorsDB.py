import sqlite3

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


    def getSectorUsers(self):
        self.__cur.execute(f"SELECT users FROM sectors")
        res = self.__cur.fetchall()
        if res: return res
        return False



    def userVerificationWhenAddingToSector(self, user_id):
        users = self.getSectorUsers()
        users_lst = []
        for user in users:
            print('every USER:', user[0])
            if str(user[0]) != '0':
                users_lst.append(str(user[0]))
        if len(users_lst) > 0:
            if str(user_id) not in users_lst[0].split(','):
                return True
        elif len(users_lst) == 0:
            return True
        return False


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
            self.__cur.execute( f"UPDATE sectors SET users='{user_id}' WHERE id='{sector_id}' " )
            self.__db.commit()
        except sqlite3.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True

