from modelView.Character import Character
import modelView.Q as queue
from model.Characters import Characters
from modelView.Types import ConsoleColor



class Disjoint_Set:
    def __init__(self, size):
        self.size = size
        self.sets = []
        self.deadPoolInstance = None

    def build(self):
        self.buildSet([0, 1, 2])
        self.buildSet([3, 4])
        self.buildSet([5])
        self.buildSet([6, 7, 8])
        self.buildSet([9, 10])
        self.buildSet([11])
        self.buildSet([12, 13])
        self.buildSet([14, 15, 16, 17])
        self.buildSet([18, 19])

    def buildSet(self, characterIDs):
        character_queue = queue.Node(4)
        for id in characterIDs:
            character_queue.enqueue(Characters[id]) #borrar .get
        self.sets.append(character_queue)

    def getCharacterAt(self, index):
        if index < len(self.sets):
            if self.sets[index]:
                return self.sets[index].peek()
            else:
                print('node not yet occupied')
                return -1
        else:
            print('position does not exist')
            return -1

    def addCharacterTo(self, index, charID):
        if index < len(self.sets):
            self.sets[index].enqueue(Characters[charID])
        else:
            print('position does not exist in list')
            return -1

    def removeCharacterAt(self, index):
        killedCharacter = None
        if index < len(self.sets):
            killedCharacter = self.sets[index].dequeue()
        for i in range(len(Characters)-1):
            if killedCharacter.getName() == Characters[i].getName():
                Characters[i].murder()

    def isSetEmpty(self, index):
        if index < len(self.sets):
            return self.sets[index].is_empty()

    def setDeadPool(self, deadPoolInstance):
        self.deadPoolInstance = deadPoolInstance


