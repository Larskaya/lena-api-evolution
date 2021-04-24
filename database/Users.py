import psycopg2, random
from datetime import datetime

class UsersDB:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getUserId(self, login):
        try:
            self.__cur.execute(f"SELECT id FROM users WHERE login='{login}'")
            res = self.__cur.fetchone()
            if res: return res
        except:
            print('error reading from db')
        return []

    def checkAddingUser(self, login):
        self.__cur.execute(f"SELECT COUNT(*) FROM users WHERE login='{login}' ")
        res = self.__cur.fetchone()
        if res[0] > 0:
            return False
        return True

    def addUser(self, name, hpsw, login, email):
        try:
            if self.checkAddingUser(login):
                self.__cur.execute( "INSERT INTO users (name, login, email, hpsw) VALUES(%s, %s, %s, %s)", (name, login, email, hpsw))
                self.__db.commit()
            else:
                return False
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True

    def getAuthUser(self, id):
        try:
            self.__cur.execute(f"SELECT * FROM auth_users WHERE id='{id}'")
            res = self.__cur.fetchone()
            if res: return res
        except:
            print('error reading from db')
        return []

    def updateAuthUser(self, code, id):
        try:
            self.__cur.execute(f"UPDATE auth_users SET code='{code}' WHERE id='{id}'")
            self.__db.commit()
            if self.__cur.rowcount == 0: return False
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True

    def addAuthUser(self, id):
        code = ''
        try:
            lst = random.sample(range(0, 10), 10)  
            
            for n in lst:
                code+=str(n)
            is_auth_updated = self.updateAuthUser(code, id)
            if not is_auth_updated:   
                self.__cur.execute( "INSERT INTO auth_users VALUES(%s, %s)", (id, code,) )
                self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        print('CODE:', code)
        return code

    def userVerificationWhenSendingMessage(self, id_, code):
        self.__cur.execute(f"SELECT COUNT(*) FROM auth_users WHERE id={id_} AND code='{code}'")
        res = self.__cur.fetchone()
        if res[0] > 0:
            return True
        return False

    def getUserPsw(self, id):
        try:
            self.__cur.execute(f"SELECT hpsw FROM users WHERE id={id}")
            res = self.__cur.fetchone()
            print('result:', res)
            if res: return res
        except:
            print('error reading from db')
        return []

    # def isAuthValid(self, id_, code):
    #     self.__cur.execute(f"SELECT COUNT(*) FROM auth_users WHERE id=(%s) AND code=(%s)", (id_, code,))
    #     res = self.__cur.fetchone()
    #     if res[0] > 0:
    #         return True
    #     return False

    def deleteUser(self, user_id):
        try:
            self.__cur.execute(f"DELETE FROM auth_users WHERE id=(%s)", (user_id, ))
            self.__db.commit()
            if self.__cur.rowcount == 0: return False
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True

    def getUsers(self):
        try:
            self.__cur.execute(f"SELECT * FROM users")
            res = self.__cur.fetchall()
            if res: return res
        except:
            print('error reading from db')
        return []