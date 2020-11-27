import threading
import time
from ServerUtils import *

class MyThread(threading.Thread):
  # overriding constructor
  def __init__(self, NodeName, conn, Xcorr, Ycorr, NodeList, listeningPort = None):
    # calling parent class constructor
    threading.Thread.__init__(self)
    self.Xcorr = Xcorr #Coordinte
    self.Ycorr = Ycorr #Coordinte
    self.conn = conn  #Communication channel between MasterServer and Connection
    self.listeningPort = listeningPort  #Listening Port of Node Requesting Node
    self.NodeName = NodeName #NodeId of node which is requesting surrounding nodes information 
    self.NodeList = NodeList  #Contains information about all the nodes 
    
    
  # define your own run method
  def run(self):
    
    #Connnection Information 
    print(" You are connected with Node {} having Corrdinate {} {} having listening port {}"
                    .format(self.NodeName, self.Xcorr, self.Ycorr, self.listeningPort))
    
    # print("NewConnection NodeList :", self.NodeList)
    finalList = ServerUtils().NearestNodeList(Xcorr=self.Xcorr, Ycorr=self.Ycorr, NodeName=self.NodeName, NodeList=self.NodeList)
    print(finalList)
    self.conn.sendall(str(finalList).encode('utf-8'))
    #for closing connection
    self.conn.close()
    

# thread1 = MyThread(" Node 1", 123, 234)
# thread1.start()
# thread2 = MyThread(" Node 2", 434, 22)
# thread2.start()
# thread1.join()
# thread2.join()
