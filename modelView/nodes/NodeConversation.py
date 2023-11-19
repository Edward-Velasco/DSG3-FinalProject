from modelView.Types import NodeType
from modelView.nodes.Node import Node

class NodeConversation(Node) :
    def __init__(self) :
        super().__init__()
        self.type = NodeType.FIGHT
        self.options = []

    def getOptions(self):
        return self.options

    def setOptions(self, options):
        self.options = options
