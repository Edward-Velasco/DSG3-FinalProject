# Ejemplo de conjuntos disyuntos

from modelView.Types import SetType
from queue import Queue

EnemiesSets = {
    0x100: {
        'type': SetType.GROUP,
        'name': "Avengers",
        'elements': Queue()
    },
    0x200: {
        'type': SetType.INDIVIDUAL,
        'name': "Spider-Man",
        'elements': Queue()
    }
}

EnemiesSets[0x100]['elements'].put(["Ironman", "route/Ironman"])
EnemiesSets[0x100]['elements'].put(["Captain America", "route/CaptainAmerica"])
EnemiesSets[0x200]['elements'].put(["Spider-Man", "route/Spider-Man"])

