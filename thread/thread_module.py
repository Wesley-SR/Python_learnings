import _thread #thread module imported
import time #time module
print('aaa')

def thread_delay(thread_name, delay):
    print('bbb')
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(thread_name, '-------->', time.time())

print('ccc')
_thread.start_new_thread(thread_delay, ('t1', 1))
print('ddd')
_thread.start_new_thread(thread_delay, ('t2', 3))