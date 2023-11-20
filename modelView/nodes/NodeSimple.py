from modelView.Types import NodeType

class NodeSimple:
    def __init__(self):
        self.type = NodeType.UNDEFINED
        self.content = ""
        self.options = []
        self.children = []

    def getType(self):
        return self.type
    def getContent(self):
        return self.content
    def getOptions(self):
        return self.options
    def getChildren(self):
        return self.children

    def setType(self, type):
        self.type = type
    def setContent(self, content):
        self.content = content
    def setOptions(self, options):
        self.options = options
    def setChildren(self, children):
        self.children = children
