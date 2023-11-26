import Q as queue
import Character as CH
import Characters as enemies

class Disjoint_Set:
    def __init__(self, size):
        self.size = size
        self.sets = []

    def build(self):
        pass

    def buildSet(self, characterIDs):
        character_queue = queue.Node(4)
        for id in characterIDs:
            character_queue.enqueue(enemies.Characters[id].get('name')) #borrar .get 
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
            self.sets[index].enqueue(enemies.Characters[charID].get('name'))
        else:
            print('position does not exist in list')
            return -1
        
    def removeCharacterAt(self, index):
        if index < len(self.sets):
            self.sets[index].dequeue()
            
    def isSetEmpty(self, index):
        if index < len(self.sets):
            return self.sets[index].is_empty()
        

"""
dset = Disjoint_Set(4)
print(dset.getCharacterAt(0))
dset.buildSet([2,1,3])
print(dset.getCharacterAt(0))
dset.addCharacterTo(1,0)
dset.addCharacterTo(0,0)
print(dset.sets[0].body)
dset.removeCharacterAt(0)
print(dset.sets[0].body)
print(dset.isSetEmpty(0))
dset.removeCharacterAt(0)
dset.removeCharacterAt(0)
dset.removeCharacterAt(0)
print(dset.isSetEmpty(0))
"""