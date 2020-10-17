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

# Já iniciou todos os t(i) e vai imprimir a string
print("Thread execution is complete! 1")

t3.join()
t4.join()

# Essa string so sera impressa depois que o t(3) e t(4) for finalizado
print("Thread execution is complete! 2")
