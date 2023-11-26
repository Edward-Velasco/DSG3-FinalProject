from model.StoryTree import StoryTree
from modelView.Types import NodeType, Option, Code, InfinityStones as St
from modelView.nodes.NodeSimple import NodeSimple
from modelView.nodes.NodeCharacter import NodeCharacter
from modelView.nodes.NodeGift import NodeGift
# import threading

class Deadpool:
    def __init__(self, gui_instance, sets_instance):
        self.gui_instance = gui_instance
        self.sets_instance = sets_instance
        self.location = None
        self.next = []
        self.fightID = -1
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
        self.display()

    def choose(self, option):
        if self.fightID != -1:
            if (option == Option.LEFT and self.next[0] != Code.DKTMU) or (option == Option.RIGHT and self.next[1] != Code.DKTMU):
                self.fightID = -1
                # self.response_received.set()
                return self.choose(Option.LEFT)
            elif (option == Option.LEFT and self.next[0] == Code.DKTMU) or (option == Option.RIGHT and self.next[1] == Code.DKTMU):
                # self.response_received.set()

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
            self.gui_instance.display_story_node(self.location)
        elif self.location.getType() == NodeType.DIALOGUE:
            self.gui_instance.display_character_node(self.location)
        elif self.location.getType() == NodeType.FIGHT:
            self.gui_instance.display_character_node(self.location)
            self.fightSequence(self.fightID)
            self.fightID = -1
        elif self.location.getType() == NodeType.SPECIAL:
            self.gui_instance.display_story_node(self.location) # displayFight(self.location) ?
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
            if tmp['type'] == NodeType.FIGHT:
                self.fightID = tmp['set']
        elif tmp['type'] == NodeType.SPECIAL:
            tmpNode = NodeGift()
            tmpNode.setStone(tmp['stone'])
        tmpNode.setType(tmp['type'])
        tmpNode.setContent(tmp['content'])
        tmpNode.setOptions(tmp['options'])
        tmpNode.setChildren(tmp['children'])
        return tmpNode

    # def option_selected_callback(self, option):
    #     self.choose(option)

    def fightSequence(self, index):
        while not self.sets_instance.isSetEmpty(index) and self.fightID != -1: # OR DEADPOOL DOESN'T LOSE
            """ Under the asumption that attribute fightContent of the class Character 
                is of type NodeSimple with NodeType.STORY type """
            tmpCharacter = self.sets_instance.getCharacterAt(index)
            tmp = tmpCharacter.getFightContent() # Is NodeSimple
            self.location = NodeCharacter()
            self.location.setType(NodeType.DIALOGUE)
            self.location.setContent(tmp.getContent())
            self.location.setOptions(tmp.getOptions())
            self.location.setChildren([])
            self.location.setCharacterName(tmpCharacter.getName())
            self.location.setCharacterPictureRoute(tmpCharacter.getPictureRoute())
            """ Miss adding options at the start (or end?) of self.next
                and sending the display (for which might need to build a NodeCharacter node to send to the GameInterface """
            tmpOptions = self.location.getOptions()
            for i in range(0, len(tmpOptions)):
                self.next.insert(i, self.buildNode(tmpOptions[i]))
            self.display()

            # self.gui_instance.setOptionSelectedCallback(self.option_selected_callback())
            # self.response_received = threading.Event()
            # self.gui_instance.display()
            # self.response_received.wait()

            for i in range(0, len(tmpOptions)):
                self.next.pop(0)
            self.sets_instance.removeCharacterAt(index)
        return Code.EXIT_0 # Means Deadpool succesfully murdered a whole superhero group

    def markAsDead(self, characterID):
        # Change character status in the dictionary?
        # Update list of images that should be shown in the Deadbook
        return None

