from modelView.nodes.NodeSimple import NodeSimple

class NodeCharacter(NodeSimple) :
    def __init__(self) :
        super().__init__()
        self.characterName = ""
        self.characterPictureRoute = ""

    def getCharacterName(self):
        return self.characterName
    def getCharacterPictureRoute(self):
        return self.characterPictureRoute

    def setCharacterName(self, characterName):
        self.characterName = characterName
    def setCharacterPictureRoute(self, characterPictureRoute):
        self.characterPictureRoute = characterPictureRoute
