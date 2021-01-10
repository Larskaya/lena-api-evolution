import time, psycopg2

def connect_db():
    conn = psycopg2.connect(
        database="evolution", 
        user="postgres", 
        password="4815162342", 
        host="localhost", 
        port="5432"
    )
    return conn    

def updateSectorFood():
    try:
        # get sector id through the number of users 
        sectors = getAllSectors()
        data = getAmountUsersAndIDSectors(sectors)
        print('DATA', data)
        for el in data.keys():
            print(el, type(el))
            print('data lenght', len(data[el]) )
            db = connect_db()
            cur = db.cursor()
            cur.execute("UPDATE sectors_food SET food=food-(%s) WHERE sector_id=(%s)", (len(data[el]), el) )
            db.commit()

        res = cur.fetchall()
        print('result of update food', res)
    except psycopg2.Error as e:
        print( 'error updating '+ str(e) )
        return False
    return True

def updateUserCreaturesAmount():
    try:
        db = connect_db()
        cur = db.cursor()
        cur.execute("UPDATE creatures SET amount=amount+1")
        db.commit()
        res = cur.fetchall()
    except psycopg2.Error as e:
        return False
    return True


def getAllSectors():
    try:
        db = connect_db()
        cur = db.cursor()
        cur.execute(f" SELECT * FROM creatures ")
        res = cur.fetchall()
    except psycopg2.Error as e:
        return False
    return res

def getAmountUsersAndIDSectors(data):
    res = {}
    for a in data:
        res[a] = a
    res = list(res.values())
    print(res, type(res))
    answer = {}
    for el in res:
        if el[0] not in answer.keys():
            answer[el[0]] = [el[1]]
        else:
            answer[el[0]].append(el[1])
    #print('answer', answer)
    return answer



def increase_amount():
    print('function of increase started')
    def increase():
        updateUserCreaturesAmount()
        updateSectorFood()
        print('1')
        time.sleep(5)
        increase()
    increase()

# def decrease_food():
#     print('function of decrease started')
#     def decrease():
#         updateSectorFood()
#         time.sleep(5)
#         decrease()
#     decrease()






increase_amount()