# Ejemplo de conjuntos disyuntos
# Cada valor debe ser un objeto de tipo Character!

from modelView.Types import Code, NodeType
from modelView.Character import Character
from modelView.nodes.NodeSimple import NodeSimple

Characters = {
    0: Character("Ironman",
                 "view/assets/characters/ironman.png",
                 "/",
                 "/",
                 NodeSimple(
                    NodeType.STORY,
                    "Air battle",
                    ["Stab the head", "Rip off a leg"],
                    [Code.DKTMU, 101])
                 ),
    1: Character("Hulk",
                 "/",
                 "/",
                 "/",
                 NodeSimple(
                    NodeType.STORY,
                    "Hulk smash",
                    ["Call spidey", "Pray for it not to be painful"],
                    [101, 101])
                 ),
}

