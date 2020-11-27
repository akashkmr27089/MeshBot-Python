class NodeGroupDisplay:

    def __init__(self):
        self.colors = ['k', 'b', 'r']
        self.grpColors = {}
        self.leftGropColors = self.colors.copy()

    def getColor(self, MasterNodeNumber, MasterAvailable):
        if MasterAvailable == False:
            return 'g'
        if MasterNodeNumber in self.grpColors:
            return self.grpColors[MasterNodeNumber]
        else:
            try:
                if(len(self.leftGropColors) != 0):
                    self.grpColors.update({MasterNodeNumber :self.leftGropColors[0]})
                    del self.leftGropColors[0]
                    return self.grpColors[MasterNodeNumber]
                else:
                    raise Exception
            except Exception:
                raise Exception("Not Enough Group Color Available as GropColors")

    def CorrdinateSeperator(self, x_data):
        Xcorr = []
        Ycorr = []
        NodeMaster = []
        try:
            for data in x_data:
                Xcorr += [data[0]]
                Ycorr += [data[1]]
                NodeMaster += [self.getColor(data[2], data[3])]
            return (Xcorr, Ycorr, NodeMaster)
        except Exception as ex:
            print(ex)
            return (None, None, None)

    
