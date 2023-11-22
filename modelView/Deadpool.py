from model.StoryTree import StoryTree
from modelView.Types import NodeType, Option, InfinityStones as St
from modelView.nodes.NodeSimple import NodeSimple
from modelView.nodes.NodeCharacter import NodeCharacter
from modelView.nodes.NodeGift import NodeGift

class Deadpool:
    def __init__(self, gui_instance):
        self.gui_instance = gui_instance
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
        print("HERE I AM BABY")
        self.display()

    def choose(self, option):
        if option == Option.LEFT:
            self.location = self.next[0]
        else:
            self.location = self.next[1]
        childrenRef = self.location.getChildren()
        self.next.clear()
        for i in range(0, len(childrenRef)):
            self.next.append(self.buildNode(childrenRef[i]))
        self.display()

    def display(self):
        if self.location.getType() == NodeType.UNDEFINED:
            print("Story is over")
        elif self.location.getType() == NodeType.STORY:
            self.gui_instance.displayStory(self.location)
        elif self.location.getType() == NodeType.DIALOGUE:
            self.gui_instance.displayDialogue(self.location)
        elif self.location.getType() == NodeType.FIGHT:
            self.gui_instance.displayFight(self.location)
        elif self.location.getType() == NodeType.SPECIAL:
            self.gui_instance.displayDialogue(self.location) # displayFight(self.location) ?
            self.gui_instance.displayNewStone(self.location.getStone())

    def buildNode(self, nodeID):
        tmp = StoryTree[nodeID]
        tmpNode = None

        if tmp['type'] == NodeType.STORY or tmp['type'] == NodeType.UNDEFINED:
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
        # Determine when to start and stop dequeing characters
        return None

    def markAsDead(self, characterID):
        # Change character status in the dictionary?
        # Update list of images that should be shown in the Deadbook
        return None

