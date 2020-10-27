'''
Source:
https://www.datacamp.com/community/tutorials/threading-in-python
'''

import threading
import time


# Create a subclass to run my function
class MySocket(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay


    def run(self):
        print('Starting Socket:', self.name)
        self.thread_socket(self.name,self.delay) # Each thread stay here until she finish
        print('Execution of Thread:', self.name, 'is complete!')


    # This is function to perform mt tasks
    def thread_socket(self, thread_name, delay):
        count = 0
        while True:
            print('tcp.accept()')
            time.sleep(15) # blockin_function
            count_receive = 0
            count += 1
            print(thread_name, '-------->', count)
            while True:
                time.sleep(delay)
                count_receive += 1
                exeeded_the_counter = count_receive <= 5
                if not exeeded_the_counter: break
                
                print('Retornando mensagem', count_receive)
                time.sleep(3)


        

class HeartBeat(threading.Thread):
    def __init__(self, heartbeat_interval):
        print('Starting Heart Beat')
        threading.Thread.__init__(self)
        print('Heart Beat inicialized')
        self.__heartbeat_interval = heartbeat_interval
        
    
    def run(self):
        print('Run Heart beat')
        self.thread_heart_beat(self.__heartbeat_interval)
        print('Heart beat is complete')


    def thread_heart_beat(self, heartbeat_interval):
        current_time = 0
        old_time = 0
        past_time = 0
        heart_beat_number = 0

        while True:
            current_time = time.time()
            past_time = current_time - old_time

            if past_time >= heartbeat_interval:
                print('Heart beart number:', heart_beat_number)
                old_time = current_time
                heart_beat_number += 1


socket = MySocket('socket', 1)
heartbeat = HeartBeat(2)

heartbeat.start()

socket.start() # This function excute the run() function

socket.join()

print("Thread execution is complete!")
