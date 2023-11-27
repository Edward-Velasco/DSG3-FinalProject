from model.StoryTree import StoryTree
from model.Characters import Characters
from modelView.Types import NodeType, Option, Code, InfinityStones as St
from modelView.nodes.NodeSimple import NodeSimple
from modelView.nodes.NodeCharacter import NodeCharacter
from modelView.nodes.NodeGift import NodeGift

class Deadpool:
    def __init__(self, gui_instance, sets_instance):
        self.gui_instance = gui_instance
        self.sets_instance = sets_instance
        self.location = None
        self.next = []
        self.fightID = -1
        self.battleKeys = []
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
        for i in range(0, len(childrenRef)):
            self.next.append(self.buildNode(childrenRef[i]))
        self.display()

    def choose(self, option):
        if self.location.getType() == NodeType.FIGHT:
            self.fightSequence(option)
            self.display()
            return
        if self.fightID != -1:
            self.next.pop(0)
            self.next.pop(0)
            if self.next[option.value] == Code.DKTMU:
                if self.fightSequence(option) == Code.EXIT_0:
                    self.location = self.next[option.value]
                self.display()
            else:
                self.fightID = -1
                self.location = self.next[option.value]
                self.display()
            return
        # if option == Option.LEFT:
        #     self.location = self.next[0]
        # else:
        #     self.location = self.next[1]
        self.location = self.next[option.value]
        childrenRef = self.location.getChildren()
        self.next.clear()
        for i in range(0, len(childrenRef)):
            self.next.append(self.buildNode(childrenRef[i]))
        self.display()

    def display(self):
        if self.location.getType() == NodeType.UNDEFINED:
            print("Story is over")
        elif self.location.getType() == NodeType.STORY or self.location.getType() == NodeType.BLANK:
            self.gui_instance.display_story_node(self.location)
        elif self.location.getType() == NodeType.DIALOGUE or self.location.getType() == NodeType.FIGHT:
            self.gui_instance.display_character_node(self.location)
        elif self.location.getType() == NodeType.SPECIAL:
            self.gui_instance.display_story_node(self.location) # displayFight(self.location) ?
            self.gui_instance.displayNewStone(self.location.getStone())

    def buildNode(self, nodeID):
        tmp = StoryTree[nodeID]
        tmpNode = None
        if tmp['type'] == NodeType.STORY or tmp['type'] == NodeType.BLANK or tmp['type'] == NodeType.UNDEFINED:
            tmpNode = NodeSimple()
        elif tmp['type'] == NodeType.DIALOGUE or tmp['type'] == NodeType.FIGHT:
            tmpNode = NodeCharacter()
            tmpNode.setCharacterName(Characters[tmp['character']].getName())
            tmpNode.setCharacterPictureRoute(Characters[tmp['character']].getPictureRoute())
            if tmp['type'] == NodeType.FIGHT:
                self.battleKeys.append(nodeID)
        elif tmp['type'] == NodeType.SPECIAL:
            tmpNode = NodeGift()
            tmpNode.setStone(tmp['stone'])
        tmpNode.setType(tmp['type'])
        tmpNode.setContent(tmp['content'])
        if tmpNode.getType() != NodeType.BLANK:
            tmpNode.setOptions(tmp['options'])
        else:
            tmpNode.setOptions([])
        tmpNode.setChildren(tmp['children'])
        return tmpNode

    def fightSequence(self, option):
        if self.fightID == -1:
            self.fightID = self.battleKeys[option.value]
            self.battleKeys.clear()
        if not self.sets_instance.isSetEmpty(self.fightID):
            tmpCharacter = self.sets_instance.getCharacterAt(self.fightID)
            tmpNode = tmpCharacter.getFightContent()
            self.location = NodeCharacter()
            self.location.setType(NodeType.DIALOGUE)
            self.location.setContent(tmpNode.getContent())
            self.location.setOptions(tmpNode.getOptions())
            self.location.setCharacterName(tmpCharacter.getName())
            self.location.setCharacterPictureRoute(tmpCharacter.getPictureRoute())
            tmpChildren = tmpNode.getChildren()
            for i in range(0, len(tmpChildren)):
                value = tmpChildren[i] if tmpChildren[i] == Code.DKTMU else self.buildNode(tmpChildren[i])
                self.next.insert(i, value)
        else:
            self.fightID = -1
            return Code.EXIT_0

    def markAsDead(self, characterID):
        self.gui_instance.updateDeadbookLinks(characterID, Characters[characterID].getMiniatureDeadRoute())
        return None

