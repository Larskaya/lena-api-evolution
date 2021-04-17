import psycopg2

class SectorsDB:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()
    
    def getSectorData(self, sector_id):
        self.__cur.execute(f"SELECT * FROM sectors WHERE id='{id}'")
        res = self.__cur.fetchone()
        if res: return res
        return False

    def getSectors(self):
        self.__cur.execute(f"SELECT * FROM sectors")
        res = self.__cur.fetchall()
        if res: return res
        return False

    def getSectorFood(self, id):
        self.__cur.execute(f"SELECT food FROM sectors WHERE id='{id}'")
        res = self.__cur.fetchone()
        if res: return res
        return False

    def getSectorsFood(self):
        self.__cur.execute(f"SELECT id, food FROM sectors")
        res = self.__cur.fetchall()
        if res: return res
        return False

    def getSectorId(self, top, left):
        self.__cur.execute(f"SELECT id FROM sectors WHERE position_top={top} AND position_left={left}")
        res = self.__cur.fatchone()
        if res: return res
        return False

    def addSector(self, positionTop, positionLeft, food, type_):
        try:
            self.__cur.execute("INSERT INTO sectors (position_left, position_top, food, type) VALUES (%s, %s, %s, %s)", 
            (positionLeft, positionTop, food, type_)) 
            self.__db.commit()
        except psycopg2.Error as e:
            print( 'error adding '+ str(e) )
            return False
        return True

    def getNeigborId(self, left, top):  
        try:
            self.__cur.execute( f"SELECT id FROM sectors WHERE position_left='{left}' AND position_top='{top}' " )
            res = self.__cur.fetchone()
            if res: return res
        except: 
            print('error reading from db')
        return []

    def getAllSectorsPositions(self):
        try:
            self.__cur.execute( f"SELECT position_top, position_left FROM sectors" )
            res = self.__cur.fetchall()
            if res: return res
        except: 
            print('error reading from db')
        return []