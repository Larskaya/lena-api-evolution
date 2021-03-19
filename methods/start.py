from predators_amount import creatures_amount_changes
from herbivorous_amount import increase_herb
import time, psycopg2

while True:
    creatures_amount_changes()
    increase_herb()
    time.sleep(15)

    