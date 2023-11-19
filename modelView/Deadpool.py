from modelView.Tree import Tree

class Deadpool:
    def __init__(self):
        self.blessings = {'green': False, 'blue': False, 'purple': False, 'yellow': False, 'red': False, 'orange': False}
        self.location = 0x001

    def getBlessings(self):
        return self.blessings
    def updateBlessings(self, gem):
        self.blessings[gem] = True

    def moveLeft(self):
        return None
    def moveRight(self):
        return None
