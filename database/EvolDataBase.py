import psycopg2, random
from datetime import datetime

class EvolDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


    def get_empty_table(self):
        try:
            self.__cur.execute("DELETE FROM users")
            self.__db.commit()
        except psycopg2.Error as e:
            print( 'error delete '+ str(e) )
            return False
        return True


    # def getUser(self, id):
    #     try:
    #         self.__cur.execute(f"SELECT name FROM users WHERE id='{id}'")
    #         res = self.__cur.fetchone()
    #         if res: return res
    #     except:
    #         print('error reading from db')
    #     return []

    # def getUsers(self):
    #     try:
    #         self.__cur.execute(f"SELECT * FROM users")
    #         res = self.__cur.fetchall()
    #         if res: return res
    #     except:
    #         print('error reading from db')
    #     return []





    def getUserId(self, login):
        try:
            #print('login for check -', login, type(login))
            self.__cur.execute(f"SELECT id FROM users WHERE login='{login}'")
            res = self.__cur.fetchone()
            print('result -', res)
            if res: return res
        except:
            print('error reading from db')
        return []





    def checkAddingUser(self, login):
        self.__cur.execute(f" SELECT COUNT(*) FROM users WHERE login LIKE '{login}' ")
        res = self.__cur.fetchone()
        #print('COUNT -', res)
        if res[0] > 0:
            print('error - such email already exists')
            return False
        return True


    def addUser(self, name, hpsw, login, email):
        try:
            if self.checkAddingUser(login):
                self.__cur.execute( "INSERT INTO users (name, login, email, password) VALUES(%s, %s, %s, %s)", (name, login, email, hpsw))
                self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True


    # AIUTHORIZED USERS

    # def getAuthUsers(self, id):
    #     try:
    #         self.__cur.execute(f"SELECT * FROM auth_users")
    #         res = self.__cur.fetchone()
    #         if res: return res
    #     except:
    #         print('error reading from db')
    #     return []

    def getAuthUser(self, id):
        try:
            self.__cur.execute(f"SELECT * FROM auth_users WHERE id='{id}'")
            res = self.__cur.fetchone()
            if res: return res
        except:
            print('error reading from db')
        return []

    # def checkAuthUserById(self, id):
    #     self.__cur.execute(f"SELECT COUNT() as 'count' FROM auth_users WHERE id='{id}' ")
    #     res = self.__cur.fetchone()
    #     #print('FUNCTION CHECK')
    #     if res['count'] > 0:
    #         return False
    #     return True






    def updateAuthUser(self, code, id):
        try:
            self.__cur.execute(f"UPDATE auth_users SET code='{code}' WHERE id='{id}'")
            print('ROW COUNT', self.__cur.rowcount)
            self.__db.commit()
            if self.__cur.rowcount == 0: return False
        except sqlite3.Error as e:
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



    def userVerificationWhenSendingMessage(self, id, code):
        self.__cur.execute(f"SELECT COUNT(*) FROM auth_users WHERE id='{id}' AND code='{code}'")
        res = self.__cur.fetchone()
        if res[0] > 0:
            return True
        return False


    
    def getUserPsw(self, id):
        try:
            print('ID:', id)
            self.__cur.execute(f"SELECT password FROM users WHERE id={id}")
            res = self.__cur.fetchone()
            print('result:', res)
            if res: return res
        except:
            print('error reading from db')
        return []




    # MESSAGES 

    def addMessageInDB(self, id, msg):
        try:
            self.__cur.execute( "INSERT INTO messages VALUES(%s, %s, %s)", (id, msg, datetime.now(), ) )
            self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True

    def getMessages(self):
        try:
            self.__cur.execute(f"SELECT * FROM messages")
            res = self.__cur.fetchall()
            if res: return res
        except:
            print('error reading from db')
        return []



    def isAuthValid(self, id, code):
        try:
            self.__cur.execute(f"SELECT * FROM auth_users WHERE id='{id}' AND code='{code}'")
            res = self.__cur.fetchone()
            #print('AUTH USER:', res, None, res!=None)
            if res != None: return True
        except:
            print('error reading from db')
        return False