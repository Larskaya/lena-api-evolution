
import threading
print(threading)

import time
from time import sleep


def test_func(string, event_for_wait, event_for_set):
    for el in string:
        event_for_wait.wait() 
        event_for_wait.clear()
        print('threading -', el)
        time.sleep(5)
        event_for_set.set() 


def test_reduc(num, event_for_wait, event_for_set):
    for _ in range(num):
        num = num - 1
        print('num after red -', num)
        event_for_wait.wait() 
        event_for_wait.clear()
        time.sleep(2)
        #num = num - 1
        #print('num after red -', num)
        event_for_set.set() 
        #time.sleep(2)


e1 = threading.Event()
e2 = threading.Event()
#e3 = threading.Event()

a = 10
b = 10

t1 = threading.Thread(target=test_reduc, args=(a, e1, e2))
t2 = threading.Thread(target=test_reduc, args=(b, e2, e1))

t1.start()
t2.start()

e1.set()

t1.join()
t2.join()




"""
t1 = threading.Thread(target=test_func, args=(a, e1, e2))
t2 = threading.Thread(target=test_func, args=(b, e2, e1))
t3 = threading.Thread(target=test_func, args=(c, e1, e2))

t1.start()
t2.start()
t3.start()


e1.set()
e2.set()

t1.join()
t2.join()
t3.join()
"""