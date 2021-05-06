import psycopg2

class SkillsDB:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def addFirstSkill(self, user_id, skills, ab):
        try:
            self.__cur.execute("INSERT INTO skills (user_id, skills, fight, friend, hide, eat, fertile) VALUES (%s, %s, %s, %s, %s, %s, %s)", (user_id, skills, ab['fight'], ab['friend'], ab['hide'], ab['eat'], ab['fertile']))
            self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True 

    def addSkill(self, user_id, skills, ab):
        try:
            self.__cur.execute(f"UPDATE skills SET skills ='{skills}' AND fight={ab['fight']} AND friend={ab['friend']} AND hide={ab['hide']} AND eat ={ab['eat']} AND fertile={ab['fertile']} WHERE user_id = {user_id}")
            self.__db.commit()
            if self.__cur.rowcount == 0: return False
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True

    def getSkills(self, user_id):
        self.__cur.execute(f"SELECT skills FROM skills WHERE user_id={user_id}")
        res = self.__cur.fetchone()
        if res: return res
        return False


    # def addAbilities(self, user_id, ab):
    #     # abilities = {'eat': 1, 'fight': 1, 'fertile': 0, 'friend': 0, 'hide': -1}
    #     print('aBBBB:', ab)
    #     try:
    #         self.__cur.execute(f"UPDATE skills SET fight={ab['fight']} AND friend={ab['friend']} AND hide={ab['hide']} AND eat ={ab['eat']} AND AND fertile={ab['fertile']} WHERE user_id = {user_id}")
    #         self.__db.commit()
    #         if self.__cur.rowcount == 0: return False
    #     except psycopg2.Error as e:
    #         print( 'error adding '+ str(e) )
    #         return False
    #     return True

