from enum import Enum

class NodeType(Enum):
    STORY = "story"
    CONVERSATION = "conversation"
    FIGHT = "fight"
    SPECIAL = "special"
    UNDEFINED = "undefined"

class Option(Enum):
    LEFT = "left"
    RIGHT = "right"
