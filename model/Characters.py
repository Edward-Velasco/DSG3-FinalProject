# Ejemplo de conjuntos disyuntos
# Cada valor debe ser un objeto de tipo Character!

from modelView.Types import Code, NodeType
from modelView.nodes.NodeSimple import NodeSimple

Characters = {
    # Use this example when Character class is implemented
    # 0: Character("Ironman", "/", "/", "/", NodeSimple("Air battle", ["Stab the head", "Rip off a leg"], [Code.DKTMU, 101])),
 
    # Example for current implementation
    0: {
        'name': "Ironman",
        'pictureRoute': "/",
        'miniatureRoute': "/",
        'miniatureDeadRoute': "/",
        'fightContent': NodeSimple(NodeType.STORY, "Air battle", ["Stab the head", "Rip off a leg"], [Code.DKTMU, 101]),
        'state': True
    },
}

