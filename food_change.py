from __main__ import app, get_db
from SectorsDB import SectorsDataBase

import flask, time
from flask import request, jsonify
from time import sleep


def increase_the_food(sector_id):
    dbase = SectorsDataBase( get_db() )
    start_food = dbase.getSectorFood(sector_id)

    def increase(food):
        food = dbase.getSectorFood(sector_id)
        food = food[0]
        
        if food:
            print('food before -', food)
            food = food - 1
            print('start first 5 sec, food', food)
            time.sleep(5)
            print('update here -', dbase.updateSectorFood(int(sector_id), food))
            if dbase.updateSectorFood(int(sector_id), food):
                #print('increase food -', food, '+ time sleep (10)')
                print('start second 5 sec')
                time.sleep(5)
                return increase(food)

            else:
                return jsonify( {'success': False, 'error': 'data not update'} )
        return jsonify( {'success': False, 'error': 'no food'} )

    return increase(start_food)


def text_increase():
    pass
