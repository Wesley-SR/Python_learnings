import threading
import time

def thread_delay(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(thread_name, '-------->', time.time())


t1 = threading.Thread(target=thread_delay, args=('t1', 1))
t2 = threading.Thread(target=thread_delay, args=('t2', 2))
t3 = threading.Thread(target=thread_delay, args=('t3', 0.5))
t4 = threading.Thread(target=thread_delay, args=('t4', 0.5))

t1.start()
t2.start()
t3.start()
t4.start()

# You have already started all t (i) and will print the string
print("Thread execution is complete! 1")

t3.join()
t4.join()

# This string will only be printed after t (3) and t (4) are finished
print("Thread execution is complete! 2")
