# Ejemplo de conjuntos disyuntos
# Cada valor debe ser un objeto de tipo Character!

from modelView.Types import Code
from modelView.nodes.NodeSimple import NodeSimple

Characters = {

    0: Character("Ironman", "/", "/", "/", NodeSimple("Air battle", ["Stab the head", "Rip off a leg"], [Code.DKTMU, 101])),
    
    # 0: {
    #     'name': "Ironman",
    #     'pictureRoute': "/",
    #     'miniatureRoute': "/",
    #     'miniatureDeadRoute': "/",
    #     'fightContent': NodeSimple("Air battle", ["Stab the head", "Rip off a leg"], [Code.DKTMU, 101]),
    #     'state': True
    # },

}

