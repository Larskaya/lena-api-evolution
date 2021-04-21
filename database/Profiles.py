import psycopg2

class ProfilesDB:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()  
  
  
    def profileAlreadyExist(self, id_):
        self.__cur.execute(f"SELECT COUNT(*) FROM profiles WHERE user_id={id_} ")
        res = self.__cur.fetchone()
        #print('profile already excist:', res)
        if res[0] > 0:
            return False
        return True

    # def checkIdAndCodeForAddProfile(self, id_, code):
    #     self.__cur.execute(f"SELECT COUNT(*) FROM auth_users WHERE id={id_} AND code='{code}'")
    #     res = self.__cur.fetchone()
    #     if res[0] > 0:
    #         return True
    #     return False


    def addProfile(self, id_, color):
        try:
            self.__cur.execute('INSERT INTO profiles (user_id, color) VALUES (%s, %s)', (id_, color))
            self.__db.commit()
        except psycopg2.Error as e:
            print('error adding', str(e))
        return True
