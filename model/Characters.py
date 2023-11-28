# Ejemplo de conjuntos disyuntos
# Cada valor debe ser un objeto de tipo Character!

from modelView.Types import Code, NodeType
from modelView.Character import Character
from modelView.nodes.NodeSimple import NodeSimple

Characters = {
    # Use this example when Character class is implemented
    # 0: Character("Ironman", "/", "/", "/", NodeSimple("Air battle", ["Stab the head", "Rip off a leg"], [Code.DKTMU, 101])),
 
    0: Character("Negasonic T. W.",
                 "view/assets/characters/negasonic.png",
                 "view/assets/characters/negasonic-vivo.png",
                 "view/assets/characters/negasonic-muerto.png",
                 NodeSimple(NodeType.STORY, '''"¿Ah, o sea que sí puedes enojarte? Pensé que los adolescentes de hoy en día ya no sentían nada" gritaste en tono de burla. Negasonic Teenage Warhead usó sus poderes para lanzar una onda de energía hacia ti, que te lanzó volando a través de la sala hasta chocar con el sofá, rompiéndolo.

Te pusiste de pie rápidamente y decidiste atacarla con''', ['tus Katanas', 'tu arma'], [6, Code.DKTMU])
                ),
    1: Character("Yukio",
                "view/assets/characters/yukio.png",
                "view/assets/characters/yukio-vivo.png",
                "view/assets/characters/yukio-muerto.png",
                NodeSimple(NodeType.STORY, '''Terminaste con ella con un solo disparo en la frente y su cuerpo inerte cayó al suelo.

Cegada por su amor por Negasonic Teenage Warhead y conmocionada por su muerte, Yukio salió corriendo hacia ti mientras gritaba "¡Maldito! ¡¡Mataste a mi novia!!". En un rápido movimiento decidiste''', ['hacerle zancadilla', 'dispararle'], [Code.DKTMU, 7])
                ),
    2: Character("Coloso",
                "view/assets/characters/coloso.png",
                "view/assets/characters/coloso-vivo.png",
                "view/assets/characters/coloso-muerto.png",
                NodeSimple(NodeType.STORY, '''Coloso llegó corriendo a la sala y al ver los cadáveres de Negasonic Teenage Warhead y de Yukio se abalanzó sobre ti furioso, derribándote al suelo. "¿No has considerado una dieta?" dijiste, sin poder respirar por el peso de su cuerpo sobre el tuyo. "Te vendría bien adelgazar unos cuantos kilos".

Al levantarse, Coloso te lanzó por los aires, pero por suerte al caer notaste cerca a ti en el suelo''', ['un hacha', 'un taladro'], [8, Code.DKTMU])
                ),
    3: Character("Iron Man",
                "view/assets/characters/ironman.png",
                "view/assets/characters/ironman-vivo.png",
                "view/assets/characters/ironman-muerto.png",
                NodeSimple(NodeType.STORY, '''"Te sugiero que discutamos esto con un whiskey y no con armas, o si no las cosas se pondrán feas" aconsejó Iron Man en un tono serio. "¿Feas dices?" soltaste una fuerte risa. "Cariño, las cosas siempre se ponen feas cuando estoy involucrado".

Ponto comenzaron una pelea, Iron Man disparándote ráfagas de energía con sus repulsores y tú contraatacando con tus katanas. Lograste romper su traje metálico y dejar el rostro de Iron Man al aire libre. Entonces le''', ['disparaste en la frente', 'cortaste la cabeza'], [Code.DKTMU, Code.DKTMU])
                ),
    4: Character("Hulk",
                "view/assets/characters/hulk.png",
                "view/assets/characters/hulk-vivo.png",
                "view/assets/characters/hulk-muerto.png",
                NodeSimple(NodeType.STORY, '''"¿Pero qué demonios está pasando aquí?" justo en el segundo en que matabas a Iron Man escuchaste la voz de Bruce Banner saliendo del ascensor y entrando a la sala de reuniones. Al ver el cadáver de Tony en el suelo y a ti junto a él se transformó en Hulk inmediatamente.

"¡Hulk aplasta mariquita!" gritó corriendo hacia ti. "Espera, ¿en serio acabas de llamarme mariquita?" soltaste una fuerte carcajada, pero Hulk no hablaba en broma y te aplastó contra el piso de un fuerte puño.''', ['burlarte de él', 'sacar tus katanas'], [Code.DKTMU, Code.DKTMU])
                ),
    5: Character("Doctor Strange",
                "view/assets/characters/doctor.png",
                "view/assets/characters/doctor-vivo.png",
                "view/assets/characters/doctor-muerto.png",
                NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                ),
    6: Character("Star-Lord",
                "view/assets/characters/starlord.png",
                "view/assets/characters/starlord-vivo.png",
                "view/assets/characters/starlord-muerto.png",
                NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                ),
    7: Character("Groot",
                "view/assets/characters/groot.png",
                "view/assets/characters/groot-vivo.png",
                "view/assets/characters/groot-muerto.png",
                NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                ),
    8: Character("Rocket Raccoon",
                "view/assets/characters/rocket.png",
                "view/assets/characters/rocket-vivo.png",
                "view/assets/characters/rocket-muerto.png",
                NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                ),
    9: Character("Gamora",
                "view/assets/characters/gamora.png",
                "view/assets/characters/gamora-vivo.png",
                "view/assets/characters/gamora-muerto.png",
                NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                ),
    10: Character("Thanos",
                 "view/assets/characters/thanos.png",
                 "view/assets/characters/thanos-vivo.png",
                 "view/assets/characters/thanos-muerto.png",
                 NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                 ),
    11: Character("Red Skull",
                 "view/assets/characters/skull.png",
                 "view/assets/characters/skull-vivo.png",
                 "view/assets/characters/skull-muerto.png",
                 NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                 ),
    12: Character("Thor",
                 "view/assets/characters/thor.png",
                 "view/assets/characters/thor-vivo.png",
                 "view/assets/characters/thor-muerto.png",
                 NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                 ),
    13: Character("Loki",
                 "view/assets/characters/loki.png",
                 "view/assets/characters/loki-vivo.png",
                 "view/assets/characters/loki-muerto.png",
                 NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                 ),
    14: Character("Black Panther",
                 "view/assets/characters/black.png",
                 "view/assets/characters/black-vivo.png",
                 "view/assets/characters/black-muerto.png",
                 NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                 ),
    15: Character("Shuri",
                 "view/assets/characters/shuri.png",
                 "view/assets/characters/shuri-vivo.png",
                 "view/assets/characters/shuri-muerto.png",
                 NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                 ),
    16: Character("Wanda",
                 "view/assets/characters/wanda.png",
                 "view/assets/characters/wanda-vivo.png",
                 "view/assets/characters/wanda-muerto.png",
                 NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                 ),
    17: Character("Vision",
                 "view/assets/characters/vision.png",
                 "view/assets/characters/vision-vivo.png",
                 "view/assets/characters/vision-muerto.png",
                 NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                 ),
    18: Character("Black Widow",
                 "view/assets/characters/widow.png",
                 "view/assets/characters/widow-vivo.png",
                 "view/assets/characters/widow-muerto.png",
                 NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                 ),
    19: Character("Hawkeye",
                 "view/assets/characters/hawkeye.png",
                 "view/assets/characters/hawkeye-vivo.png",
                 "view/assets/characters/hawkeye-muerto.png",
                 NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                 )
}

