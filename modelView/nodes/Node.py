from ..enum.Types import NodeType

class Node:
    def __init__(self):
        self.type = NodeType.UNDEFINED
        self.children = []
        self.choices = []
