
from __main__ import app, get_db
from SectorsDB import SectorsDataBase

import flask, time
from flask import request, jsonify
from time import sleep

import threading
print(threading)


@app.route('/food')
def get_sector(sector_id):
    db = SectorsDataBase(get_db())
    sector = db.getSectorFood(sector_id)
    return sector 


def test_red(sector, event_for_wait, event_for_set):
    for food in sector['food']:
        event_for_wait.wait() 
        event_for_wait.clear()
        print('threading FOOD (test) -', food)
        time.sleep(5)
        event_for_set.set() 

"""
e1 = threading.Event()
e2 = threading.Event()

t1 = threading.Thread(target=test_red, args=(get_sector('1/1'), e1, e2))
t2 = threading.Thread(target=test_red, args=(get_sector('1/1'), e2, e1))

t1.start()
t2.start()

e1.set()

t1.join()
t2.join()
"""




