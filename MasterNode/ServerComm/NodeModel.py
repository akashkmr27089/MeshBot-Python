## DataStructure for storing Information about the Node :

class NodeModel:

    def __init__(self, NodeName, Xcorr, Ycorr, ListeningPort):
        self.NodeName = NodeName
        self.Xcorr = Xcorr
        self.Ycorr = Ycorr
        self.ListeningPort = ListeningPort
