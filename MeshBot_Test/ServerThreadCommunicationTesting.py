import Socket
import threading
from queue import Queue
import time

class ChildNodeConnection(threading.Thread):

    def __init__(self. conn, addr, queue):
        threading.Thread.__inti__(self)
        self.conn = conn
        self.addr = addr
        self.queue = queue

    def run(self):
        pass
        

class Server:

    def __init__(self):
        self.Connection_Pool = {}
        self.queue = Queue()
        self.Port = 23232
        self.Host = '127.0.0.1'

    def start():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                s.bind((self.Host, self.Port))
            except Exception as ex:
                print(str(ex))
            s.listen()
            while True:
                try:
                    conn, addr = s.accept()
                    data = ChildNodeConnection(conn, addr, queue)
                    
                    
