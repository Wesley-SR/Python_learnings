import threading
import time

def volume_cube(a):
    print('Volume of cube: ', a*a*a)

def volume_square(a):
    print("Volume of square: ", a*a)

t1 = threading.Thread(target=volume_cube, args=(2,)) # A virgula e pq o arg espera um tupla

t2 = threading.Thread(target=volume_square, args=(3,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Thread execution is complete!")