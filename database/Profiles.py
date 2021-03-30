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

    def checkIdAndCodeForAddProfile(self, id_, code):
        self.__cur.execute(f"SELECT COUNT(*) FROM auth_users WHERE id={id_} AND code='{code}'")
        res = self.__cur.fetchone()
        if res[0] > 0:
            return True
        return False


    def addProfile(self, id_, type_, color, code):
        try:
            if self.checkIdAndCodeForAddProfile(id_, code) and self.profileAlreadyExist(id_):
                #print('INSERT INRO PROFILE !')
                self.__cur.execute('INSERT INTO profiles (user_id, type, color) VALUES (%s, %s, %s)', (id_, type_, color))
                self.__db.commit()
            else: return False
        except psycopg2.Error as e:
            print('error adding', str(e))
        return True