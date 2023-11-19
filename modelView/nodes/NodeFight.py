from modelView.Types import NodeType
from modelView.nodes.Node import Node

class NodeFight(Node) :
    def __init__(self) :
        super().__init__()
        self.type = NodeType.FIGHT
        self.oponent = 0x000
        self.options = []

    def getOponent(self):
        return self.oponent
    def getOptions(self):
        return self.options

    def setOponent(self, oponent):
        self.oponent = oponent
    def setOptions(self, options):
        self.options = options
