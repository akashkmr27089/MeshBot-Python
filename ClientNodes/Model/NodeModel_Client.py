## DataStructure for storing Information about the Node :

class NodeModel_Client:


    def __init__(self, NodeName, Xcorr, Ycorr, ListeningPort,
                 RootInfo = {}):
        self.NodeName = NodeName
        self.Xcorr = Xcorr
        self.Ycorr = Ycorr
        self.ListeningPort = ListeningPort

        # Root Information 
        self.RootInfo = RootInfo
