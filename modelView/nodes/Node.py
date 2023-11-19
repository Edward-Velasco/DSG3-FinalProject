from modelView.enum.Types import NodeType

class Node:
    def __init__(self):
        self.type = NodeType.STORY
        self.content = []
        self.children = []

    def getType(self):
        return self.type
    def getContent(self):
        return self.content
    def getChildren(self):
        return self.children

    def setType(self, type):
        self.type = type
    def setContent(self, content):
        self.content = content
    def setChildren(self, children):
        self.children = children
