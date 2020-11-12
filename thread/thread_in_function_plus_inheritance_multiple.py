
"""
    Source:
    https://www.datacamp.com/community/tutorials/threading-in-python
"""


import threading
import time

class DraginoTransmitter():

    def send_message(self, message):
        print('{}'.format(message))
    
    def generate_data_packet(self, message_ID, data1, data2):

        print('Generate data packet')
        print('message_ID: {}\ndata1: {}\ndata2: {}'
        .format(message_ID, data1, data2))

"""
    I created a mother class and the thread are inside function,
    because i need use a common variable for thw two functions 
"""
class SocketAndHeartBeat(DraginoTransmitter):
    def __init__(self):

        self.tx_channel_ocupation = False
        self.current_time = 0
        self.old_time = 0
        self.past_time = 0
        self.heart_beat_number = 0


    """
        This function will be used to run the socket
    """
    def thread_socket(self, thread_name, delay):
        self.delay = delay
        while True:
            print('tcp.accept()')
            time.sleep(10) # blockin_function
            count_receive = 0
            print(thread_name, 'recebeu algo!')
            while True:
                print('reading ...', count_receive)
                count_receive += 1
                exeeded_the_counter = count_receive <= 5

                if not exeeded_the_counter: break
                
                if not self.tx_channel_ocupation:
                    self.tx_channel_ocupation = True
                    print('socket')
                    print('tx_channel_ocupation = ', self.tx_channel_ocupation)
                    self.generate_data_packet('Return', 45, 12.5)
                    self.send_message('Forward message')
                    time.sleep(1)
                    self.tx_channel_ocupation = False
                    print('tx_channel_ocupation = ', self.tx_channel_ocupation)
                    print('\n')
                else: 
                    print('Mesangem nao tetornada: tx_channel_ocupation is busy')
                    time.sleep(1)

    def thread_heart_beat(self, name, heartbeat_interval):
        self.__heartbeat_interval = heartbeat_interval
        time.sleep(1)
        print(name)

        while True:
            self.current_time = time.time()
            self.past_time = self.current_time - self.old_time

            if self.past_time >= self.__heartbeat_interval:
                if not self.tx_channel_ocupation:
                    print('Heart Beat')
                    self.tx_channel_ocupation = True
                    print('tx_channel_ocupation = ', self.tx_channel_ocupation)
                    self.generate_data_packet('Heart beat', self.heart_beat_number, None)
                    self.old_time = self.current_time
                    self.heart_beat_number += 1
                    self.tx_channel_ocupation = False
                    print('tx_channel_ocupation = ', self.tx_channel_ocupation)
                    print('\n')
                else:
                    print('Heartbeat nao enviado: tx_channel_ocupation is busy')
                    time.sleep(1)

        print('Heart beat is complete')

if __name__ == "__main__":


    heartbeat_interval = 1
    delay = 1

    my_process = SocketAndHeartBeat()

    t1 = threading.Thread(target=my_process.thread_socket, args=('Socket', heartbeat_interval))
    t2 = threading.Thread(target=my_process.thread_heart_beat, args=('HeartBeat', delay))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Thread execution is complete!")