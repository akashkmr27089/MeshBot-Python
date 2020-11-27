import socket
import NewConnectionThread
from NewConnectionThread import *
from NodeModel import *

class MasterNodeServer():

    def __init__ (self, NodeList = {}, StartPort = 0):
        self.HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        self.PORT = 65432        # Port to listen on (non-privileged ports are > 1023) 
        self.NodeList = NodeList

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                s.bind((self.HOST, self.PORT))
            except Exception as ex:
                print(str(ex))
                raise Exception(" Binding Process Failed ")
            s.listen()
            print(" Server Started with Port Address {} ".format(self.PORT))
            while True:
                try:
                    conn, addr = s.accept()
                    print(conn, addr)
                    data = conn.recv(1024)
                    data_string = str(data).strip('b')
                    doc = data_string.strip('b').strip("/'/'").strip('[]').split(',')
                    NodeName, Xcorr, Ycorr, MasterGroup, listeningPort, Joined = int(doc[0]), int(doc[1]), int(doc[2]), int(doc[3]), int(doc[4]), bool(doc[5])
                    print(Xcorr, Ycorr, MasterGroup, listeningPort, Joined)
                    NodeConnection = MyThread(NodeName, conn, Xcorr, Ycorr, self.NodeList, listeningPort)
                    NodeConnection.start()
                    NodeConnection.join()
                except KeyboardInterrupt:
                    print("KeyBoard Escape")
                    break

#Staring MasterNode
doc = MasterNodeServer(
    NodeList = {
        231: NodeModel(231, 123, 234, ListeningPort = 1252),
        551: NodeModel(551, 541, 234, ListeningPort = 2354),
        612: NodeModel(612, 555, 525, ListeningPort = 1300),
        654: NodeModel(654, 985, 201, ListeningPort = 658)
    } 
)
doc.start()
