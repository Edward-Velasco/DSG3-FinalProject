from modelView.Types import InfinityStones
from modelView.nodes.NodeCharacter import NodeCharacter

class NodeGift(NodeCharacter) :
    def __init__(self) :
        super().__init__()
        self.stone = None

    def getStone(self):
        return self.stone

    def setStone(self, stone):
        self.stone = stone
