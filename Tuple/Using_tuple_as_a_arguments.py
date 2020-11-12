# Pass tuple as a arguments
import threading


class my_class():

    def my_function(self, thistuple):
        print('Size Tuple: {}'.format(len(thistuple)))
        print(thistuple)

    def run_my_function(self, thistuple):
        t = threading.Thread(target = self.my_function,
            args=(thistuple, ))
        t.daemon = False
        t.start()



if __name__ == "__main__":
    
    thistuple = ("apple:2", "banana:2", "cherry:3", "orange:5")
    my_object = my_class()
    my_object.run_my_function(thistuple)