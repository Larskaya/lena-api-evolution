import psycopg2
from datetime import datetime

class MessagesDB:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def addMessageInDB(self, id_, msg):
        try:
            self.__cur.execute( "INSERT INTO messages VALUES(%s, %s, %s)", (id_, msg, datetime.now(), ) )
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