from modelView.Types import InfinityStones
from modelView.nodes.NodeSimple import NodeSimple

class NodeConversation(NodeSimple) :
    def __init__(self) :
        super().__init__()
        self.stone = None

    def getStone(self):
        return self.stone

    def setStone(self, stone):
        self.stone = stone
