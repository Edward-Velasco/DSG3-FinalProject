from enum import Enum

class NodeType(Enum):
    STORY = "story"
    DIALOGUE = "dialogue"
    FIGHT = "fight"
    SPECIAL = "special"
    BLANK = "blank"
    UNDEFINED = "undefined"

class Option(Enum):
    LEFT = "left"
    RIGHT = "right"

class InfinityStones(Enum):
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"
    YELLOW = "yellow"
    RED = "red"
    ORANGE = "orange"

