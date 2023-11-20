from modelView.Types import Option, InfinityStones as St
from main import deadpool

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
        return None

    def buildNode(self, nodeID):
        return None

    def choose(self, option):
        return None

    def fightSequence(self, index):
        return None

    def markAsDead(self, characterID):
        return None
