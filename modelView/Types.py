from enum import Enum

class NodeType(Enum):
    STORY = "story"
    DIALOGUE = "dialogue"
    FIGHT = "fight"
    SPECIAL = "special"
    BLANK = "blank"
    UNDEFINED = "undefined"

class Option(Enum):
    LEFT = 0
    RIGHT = 1

class Code(Enum):
    DKTMU = "Deadpool Kills The Marvel Universe"
    EXIT_0 = 0

class InfinityStones(Enum):
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"
    YELLOW = "yellow"
    RED = "red"
    ORANGE = "orange"

class ConsoleColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
