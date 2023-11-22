from model.StoryTree import StoryTree
from modelView.Types import NodeType, Option, InfinityStones as St
from modelView.nodes.NodeSimple import NodeSimple
from modelView.nodes.NodeCharacter import NodeCharacter
from modelView.nodes.NodeGift import NodeGift
from main import GUI

class Deadpool:
    def __init__(self):
        self.location = None
        self.next = []
        self.blessings = {
            St.GREEN: False,
            St.BLUE: False,
            St.PURPLE: False,
            St.YELLOW: False,
            St.RED: False,
            St.ORANGE: False
        }

    def start(self):
        self.location = self.buildNode(1)
        childrenRef = self.location.getChildren()
        self.next = [self.buildNode(childrenRef[0]), self.buildNode(childrenRef[1])]
        print(self.location)
        print(self.next)

    def choose(self, option):
        if option == Option.LEFT:
            self.location = self.next[0]
        else:
            self.location = self.next[1]
        childrenRef = self.location.getChildren()
        self.next.clear()
        for i in range(0, len(self.next)):
            self.next.append(self.buildNode(childrenRef[i]))

    def display(self):
        if self.location.getType() == NodeType.UNDEFINED:
            print("Story is over")
        elif self.location.getType() == NodeType.STORY:
            GUI.displayStory(self.location)
        elif self.location.getType() == NodeType.DIALOGUE:
            GUI.displayDialogue(self.location)
        elif self.location.getType() == NodeType.FIGHT:
            GUI.displayFight(self.location)
        elif self.location.getType() == NodeType.SPECIAL:
            GUI.displayDialogue(self.location) # displayFight(self.location) ?
            GUI.displayNewStone(self.location.getStone())

    def buildNode(self, nodeID):
        tmp = StoryTree[nodeID]
        tmpNode = NodeSimple()
        if tmp['type'] == NodeType.STORY:
            tmpNode = NodeSimple()
        elif tmp['type'] == NodeType.DIALOGUE or tmp['type'] == NodeType.FIGHT:
            tmpNode = NodeCharacter()
            tmpNode.setCharacterName(tmp['characterName'])
            tmpNode.setCharacterPictureRoute(tmp['characterPictureRoute'])
        elif tmp['type'] == NodeType.SPECIAL:
            tmpNode = NodeGift()
            tmpNode.setStone(tmp['stone'])
        tmpNode.setType(tmp['type'])
        tmpNode.setContent(tmp['content'])
        tmpNode.setOptions(tmp['options'])
        tmpNode.setChildren(tmp['children'])
        return tmpNode

    def fightSequence(self, index):
        return None

    def markAsDead(self, characterID):
        return None

