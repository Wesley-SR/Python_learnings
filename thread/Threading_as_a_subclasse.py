'''
Source:
https://www.datacamp.com/community/tutorials/threading-in-python
'''

import threading
import time

# This is function to perform mt tasks
def thread_delay(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(thread_name, '-------->', time.time())

# Create a subclass to run my function
class DataCampThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay


    def run(self):
        print('Starting Thread:', self.name)
        thread_delay(self.name,self.delay) # Each thread stay here until she finish
        print('Execution of Thread:', self.name, 'is complete!')


t1 = DataCampThread('t1', 1)
t2 = DataCampThread('t2', 3)    

t1.start() # This function excute the run() function
t2.start()

t1.join()
t2.join()

print("Thread execution is complete!")