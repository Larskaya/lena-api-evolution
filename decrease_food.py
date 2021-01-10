
from time import sleep

from App import App


def decrease_food(id_sector):
    print('function of decrease started')
    food = App.getSectorFood(id_sector)
    sector_users = len(App.getSectorUsers(id_sector))

    if food and sector_users:
        def decrease(food):
            print('new food', food)

            if 'int' in str(type(food)) and 'int' in str(type(sector_users)):
                food -= sector_users
            else:
                food = int(food[0]) - sector_users


            App.updateSectorFood(id_sector, food)
            time.sleep(5)
            decrease(food)
        decrease(food)

