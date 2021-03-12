import psycopg2

class CreaturesDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getHerbAmountInSector(sector_id):
        try:
            self.__cur.execute(f"SELECT amount FROM creatures WHERE sector_id='{sector_id}'")
            res = self.__cur.fetchall()
            if res: return res
        except psycopg2 as e:
            print('error reading from db', str(e))
        return []

    def dicreaseFood(sector_id):
        try:
            self.__cur.execute(f"UPDATE sectors SET food = food - 1 WHERE sector_id='{sector_id}'")
            self.__db.commit()
            if self.__cur.rowcount == 0: return False
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True

    def dicreaseFood(sector_id):
        try:
            self.__cur.execute(f"UPDATE creatures SET amount = amount + 1 WHERE sector_id='{sector_id}' AND user_id='{user_id}'")
            self.__db.commit()
            if self.__cur.rowcount == 0: return False
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True
