from modelView.Q import Node as queue
from modelView.Character import Character as CH
from model.Characters import Characters as enemies


class Disjoint_Set:
    def __init__(self, size):
        self.size = size
        self.sets = []

    def build(self):
        pass

    def buildSet(self, characterIDs):
        character_queue = queue.Node(4)
        for id in characterIDs:
            character_queue.enqueue(enemies.Characters[id]) #borrar .get 
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
            self.sets[index].enqueue(enemies.Characters[charID])
        else:
            print('position does not exist in list')
            return -1
        
    def removeCharacterAt(self, index):
        if index < len(self.sets):
            self.sets[index].dequeue()
            
    def isSetEmpty(self, index):
        if index < len(self.sets):
            return self.sets[index].is_empty()
        

