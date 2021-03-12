from predators_amount import creatures_amount_changes
from herbivorous_amount import increase_herb
import time, psycopg2

# import sys
# sys.path.append('../')

# from App import App


def connect_db():
    conn = psycopg2.connect(
        database="evolution", 
        user="postgres", 
        password="user", 
        host="localhost", 
        port="5432"
    )
    return conn    

db = connect_db()
cursor = db.cursor()
 

# counter = 0
while True:
    creatures_amount_changes()
    increase_herb()
    # counter += 1
    time.sleep(15)
    # if counter == 20:
    #     break

    