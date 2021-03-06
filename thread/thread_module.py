'''
Source:
https://www.datacamp.com/community/tutorials/threading-in-python
'''

import _thread #thread module imported
import time #time module

def thread_delay(thread_name, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(thread_name, '-------->', time.time())

_thread.start_new_thread

t1 = _thread.start_new_thread(thread_delay, ('t1', 1))
t2 = _thread.start_new_thread(thread_delay, ('t2', 3))

t1.start()
t2.start()