import threading
import time

def volume_cube(a):
    print('Volume of cube: ', a*a*a)

def volume_square(a):
    print("Volume of square: ", a*a)

# Uses a comma because the argument expects a tuple
t1 = threading.Thread(target=volume_cube, args=(2,))
t2 = threading.Thread(target=volume_square, args=(3,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Thread execution is complete!")