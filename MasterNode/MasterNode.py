from ServerComm.ServerHandle import MasterNodeServer
from ServerComm.NodeModel import NodeModel

# from ServerComm.ServerHandle import MasterNodeServer
# from ServerComm.NodeModel import NodeModel
# from ServerComm.NewConnectionThread import MyThread

doc = MasterNodeServer(
    NodeList = {
        231: NodeModel(231, 123, 234, ListeningPort = 1252),
        551: NodeModel(551, 541, 234, ListeningPort = 2354),
        612: NodeModel(612, 555, 525, ListeningPort = 1300),
        654: NodeModel(654, 985, 201, ListeningPort = 658)
    } 
)
doc.start()