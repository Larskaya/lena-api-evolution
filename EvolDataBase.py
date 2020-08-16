import sqlite3

class EvolDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


    def getAuthUser(self, id):
        try:
            self.__cur.execute(f"SELECT name FROM users WHERE id='{id}'")
            res = self.__cur.fetchone()
            if res: return res
        except:
            print('error reading from db')
        return []


    def getUserId(self, email):
        try:
            self.__cur.execute(f" SELECT id FROM users WHERE email='{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if res: return res
        except:
            print('error reading from db')
        return []


    def checkAddingUser(self, email):
        self.__cur.execute(f" SELECT COUNT() as 'count' FROM users WHERE email LIKE '{email}' ")
        res = self.__cur.fetchone()
        if res['count'] > 0:
            print('error - such email already exists')
            return False
        return True

    def addUser(self, name, psw, email):
        try:
            if self.checkAddingUser(email):
                self.__cur.execute( "INSERT INTO users VALUES(null, ?, ?, ?)", (name, psw, email,) )
                self.__db.commit()
        except sqlite3.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True

    def check(self, id):
        self.__cur.execute(f" SELECT COUNT() as 'count' FROM auth_users WHERE id LIKE '{id}' ")
        res = self.__cur.fetchone()
        if res['count'] > 0:
            print('error - such email already exists')
            return False
        return True


    def addAuthUser(self, id):
        try:
            if self.check( id ):
                code = 'afwqaimrj3e21r'
                self.__cur.execute( "INSERT INTO auth_users VALUES(?, ?)", (id, code,) )
                self.__db.commit()
        except sqlite3.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True

