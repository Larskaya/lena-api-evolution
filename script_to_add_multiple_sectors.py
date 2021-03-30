# script to add multiple sectors 

from add_multiple_sectors import add_sectors
import random 

def b():
    sectors_num = 0
    counter_x = 1
    while counter_x <= 12:
        counter_y = 10
        while counter_y <= 18:
            food = random.randint(500, 30000)
            print('x:', counter_x, 'y:', counter_y, 'food:', food)
            add_sectors(counter_x, counter_y, food)
            sectors_num += 1
            counter_y += 1
        counter_x += 1
    print('NUM OF SECTORS:', sectors_num)


        
b()