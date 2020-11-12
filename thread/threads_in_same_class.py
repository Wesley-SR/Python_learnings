
import threading
import time

class mother():
    def __init__(self):
        self._name = 'Wesley'

class sun(mother):
    def __init__(self):
        super().__init__()
        print('Starting')
    
    def run_thread(self):
        t1 = threading.Thread(target=self.my_thread, args=('name', 'last name'))
        t1.daemon = False
        t1.start()

    def my_thread(self, name, last_name):
        current_time = 0
        last_time = 0
        interval = 5

        while True:
            current_time = time.time()
            past_time = current_time - last_time
            if past_time > interval:
                last_time = current_time
                print('past_time: ', past_time)

if __name__ == "__main__":
    my_process = sun()

    my_process.run_thread()

