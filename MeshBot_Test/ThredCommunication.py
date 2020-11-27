import threading
import time
from queue import Queue

class Producer(threading.Thread):

    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data
        self.id = threading.currentThread().ident

    def run(self):
        i = 0
        while(i != 10):
            i += 1
            self.data.put('Producer ' + str(self.id) + ' ' +str(i))

class Consumer(threading.Thread):

    def __init__(self,data):
        threading.Thread.__init__(self)
        self.data = data
        self.id = threading.currentThread().ident
        
    def run(self):
        i = 0
        while i != 20:
            i += 1
            print('Consumer' + self.data.get())

data = Queue()
pro1 = Producer(data);
pro2 = Producer(data);
cons1 = Consumer(data);
pro1.start()
print("Producer 2 Started")
pro2.start()
cons1.start()
pro1.join()
pro2.join()
cons1.join()


