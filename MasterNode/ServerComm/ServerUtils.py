import math

class ServerUtils:
    
    def __init__(self):
        pass 

    def ManhatanDistance(self, node1, node2):
        #implementation of ManhatanDistance
        return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

    def EuclidianDistance(self, node1, node2):
        #implementation of Euclidian Distance
        return math.sqrt( (node1[0] - node2[0])**2 + (node1[1] - node2[1])**2 )

    def NearestNodeList(self, Xcorr, Ycorr, NodeName, NodeList):
        # print(Xcorr, Ycorr, NodeName, NodeList)
        MinDistanceNode = []
        # print("NodeList ", Xcorr, Ycorr, NodeName, NodeList)
        for NodeDetails in NodeList:
            if NodeList[NodeDetails].NodeName == NodeName:
                continue
            else:
                #for Appling Euclidian Distance Betweeen Nodes (Option 2)
                val = self.EuclidianDistance([Xcorr, Ycorr], [NodeList[NodeDetails].Xcorr, NodeList[NodeDetails].Ycorr])
                
                #for Appling Manhatan Distance Between Nodes (Option 1)
                # val = self.ManhatanDistance([Xcorr, Ycorr], [NodeDetails.Xcorr, NodeDetails.Ycorr])

                MinDistanceNode.append([val, NodeList[NodeDetails].ListeningPort])

        MinDistanceNode.sort()
        print("Final Output :", MinDistanceNode)
        NearestNode = [x[1] for x in MinDistanceNode]
        if len(NearestNode) > 3:
            return NearestNode[:3]
        else:
            return NearestNode
                

