from modelView.Types import NodeType
from modelView.nodes.Node import Node

class NodeFight(Node) :
    def __init__(self) :
        super().__init__()
        self.type = NodeType.FIGHT
        self.oponent = 0x000

    def getOponent(self):
        return self.oponent

    def setOponent(self, oponent):
        self.oponent = oponent
