# Ejemplo de conjuntos disyuntos
# Cada valor debe ser un objeto de tipo Character!

from modelView.Types import Code, NodeType
from modelView.Character import Character
from modelView.nodes.NodeSimple import NodeSimple

Characters = {
    # Use this example when Character class is implemented
    # 0: Character("Ironman", "/", "/", "/", NodeSimple("Air battle", ["Stab the head", "Rip off a leg"], [Code.DKTMU, 101])),
 
    # Example for current implementation
    0: {
        'name': "Negasonic T. W.",
        'pictureRoute': "view/assets/characters/negasonic.png",
        'miniatureRoute': "view/assets/characters/negasonic-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/negasonic-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''"¿Ah, o sea que sí puedes enojarte? Pensé que los adolescentes de hoy en día ya no sentían nada" gritaste en tono de burla. Negasonic Teenage Warhead usó sus poderes para lanzar una onda de energía hacia ti, que te lanzó volando a través de la sala hasta chocar con el sofá, rompiéndolo.

Te pusiste de pie rápidamente y decidiste atacarla con''', ['tus Katanas', 'tu arma'], [6, Code.DKTMU]),
        'state': True
    },
    1: {
        'name': "Yukio",
        'pictureRoute': "view/assets/characters/yukio.png",
        'miniatureRoute': "view/assets/characters/yukio-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/yukio-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''Terminaste con ella con un sólo disparo en la frente y su cuerpo inerte cayó al suelo.

Cegada por su amor por Negasonic Teenage Warhead y conmocionada por su muerte, Yukio salió corriendo hacia ti mientras gritaba "¡Maldito! ¡¡Mataste a mi novia!!". En un rápido movimiento decidiste''', ['hacerle zancadilla', 'dispararle'], [Code.DKTMU, 7]),
        'state': True
    },
    2: {
        'name': "Coloso",
        'pictureRoute': "view/assets/characters/coloso.png",
        'miniatureRoute': "view/assets/characters/coloso-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/coloso-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''Coloso llegó corriendo a la sala y al ver los cadáveres de Negasonic Teenage Warhead y de Yukio se abalanzó sobre ti furioso, derribándote al suelo. "¿No has considerado una dieta?" dijiste, sin poder respirar por el peso de su cuerpo sobre el tuyo. "Te vendría bien adelgazar unos cuantos kilos".

Al levantarse, Coloso te lanzó por los aires, pero por suerte al caer notaste cerca a ti en el suelo''', ['un hacha', 'un taladro'], [8, Code.DKTMU]),
        'state': True
    },
    3: {
        'name': "Iron Man",
        'pictureRoute': "view/assets/characters/ironman.png",
        'miniatureRoute': "view/assets/characters/ironman-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/ironman-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''"Te sugiero que discutamos esto con un whiskey y no con armas, o si no las cosas se pondrán feas" aconsejó Iron Man en un tono serio. "¿Feas dices?" soltaste una fuerte risa. "Cariño, las cosas siempre se ponen feas cuando estoy involucrado".

Ponto comenzaron una pelea, Iron Man disparándote ráfagas de energía con sus repulsores y tú contraatacando con tus katanas. Lograste romper su traje metálico y dejar el rostro de Iron Man al aire libre. Entonces le''', ['disparaste en la frente', 'cortaste la cabeza'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    4: {
        'name': "Hulk",
        'pictureRoute': "view/assets/characters/hulk.png",
        'miniatureRoute': "view/assets/characters/hulk-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/hulk-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''"¿Pero qué demonios está pasando aquí?" justo en el segundo en que matabas a Iron Man escuchaste la voz de Bruce Banner saliendo del ascensor y entrando a la sala de reuniones. Al ver el cadáver de Tony en el suelo y a ti junto a él se transformó en Hulk inmediatamente.

"¡Hulk aplasta mariquita!" gritó corriendo hacia ti. "Espera, ¿en serio acabas de llamarme mariquita?" soltaste una fuerte carcajada, pero Hulk no hablaba en broma y te aplastó contra el piso de un fuerte puño.''', ['burlarte de él', 'sacar tus katanas'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    5: {
        'name': "Doctor Strange",
        'pictureRoute': "view/assets/characters/doctor.png",
        'miniatureRoute': "view/assets/characters/doctor-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/doctor-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    6: {
        'name': "Star-Lord",
        'pictureRoute': "view/assets/characters/starlord.png",
        'miniatureRoute': "view/assets/characters/starlord-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/starlord-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    7: {
        'name': "Groot",
        'pictureRoute': "view/assets/characters/groot.png",
        'miniatureRoute': "view/assets/characters/groot-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/groot-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    8: {
        'name': "Rocket Raccoon",
        'pictureRoute': "view/assets/characters/rocket.png",
        'miniatureRoute': "view/assets/characters/rocket-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/rocket-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    9: {
        'name': "Gamora",
        'pictureRoute': "view/assets/characters/gamora.png",
        'miniatureRoute': "view/assets/characters/gamora-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/gamora-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    10: {
        'name': "Thanos",
        'pictureRoute': "view/assets/characters/thanos.png",
        'miniatureRoute': "view/assets/characters/thanos-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/thanos-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    11: {
        'name': "Red Skull",
        'pictureRoute': "view/assets/characters/skull.png",
        'miniatureRoute': "view/assets/characters/skull-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/skull-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    12: {
        'name': "Thor",
        'pictureRoute': "view/assets/characters/thor.png",
        'miniatureRoute': "view/assets/characters/thor-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/thor-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    13: {
        'name': "Loki",
        'pictureRoute': "view/assets/characters/loki.png",
        'miniatureRoute': "view/assets/characters/loki-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/loki-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    14: {
        'name': "Black Panther",
        'pictureRoute': "view/assets/characters/black.png",
        'miniatureRoute': "view/assets/characters/black-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/black-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    15: {
        'name': "Shuri",
        'pictureRoute': "view/assets/characters/shuri.png",
        'miniatureRoute': "view/assets/characters/shuri-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/shuri-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    16: {
        'name': "Wanda",
        'pictureRoute': "view/assets/characters/wanda.png",
        'miniatureRoute': "view/assets/characters/wanda-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/wanda-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    17: {
        'name': "Vision",
        'pictureRoute': "view/assets/characters/vision.png",
        'miniatureRoute': "view/assets/characters/vision-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/vision-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    18: {
        'name': "Black Widow",
        'pictureRoute': "view/assets/characters/widow.png",
        'miniatureRoute': "view/assets/characters/widow-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/widow-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    19: {
        'name': "Hawkeye",
        'pictureRoute': "view/assets/characters/hawkeye.png",
        'miniatureRoute': "view/assets/characters/hawkeye-vivo.png",
        'miniatureDeadRoute': "view/assets/characters/hawkeye-muerto.png",
        'fightContent': NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    }
}

