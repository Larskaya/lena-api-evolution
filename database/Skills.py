import psycopg2

class SkillsDB:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def addFirstSkill(self, user_id, skills):
        try:
            self.__cur.execute("INSERT INTO skills (user_id, skills) VALUES (%s, %s)", (user_id, skills))
            self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True 

    def addSkill(self, user_id, skills):
        try:
            self.__cur.execute(f"UPDATE skills SET skills ='{skills}' WHERE user_id = {user_id}")
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