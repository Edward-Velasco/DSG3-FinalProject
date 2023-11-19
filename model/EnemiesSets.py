# Ejemplo de conjuntos disyuntos

from modelView.enum.Types import NodeType
from queue import Queue

EnemiesSets = {
    0x100: {
        'type': "Group" ,
        'name': "Avengers",
        'elements': Queue()
    }
}

print(EnemiesSets[0x100])
