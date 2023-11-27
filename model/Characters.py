# Ejemplo de conjuntos disyuntos
# Cada valor debe ser un objeto de tipo Character!

from modelView.Types import Code, NodeType
from modelView.nodes.NodeSimple import NodeSimple

Characters = {
    # Use this example when Character class is implemented
    # 0: Character("Ironman", "/", "/", "/", NodeSimple("Air battle", ["Stab the head", "Rip off a leg"], [Code.DKTMU, 101])),
 
    # Example for current implementation
    0: {
        'name': "Negasonic T. W.",
        'pictureRoute': "/",
        'miniatureRoute': "/",
        'miniatureDeadRoute': "/",
        'fightContent': NodeSimple(NodeType.STORY, '''"¿Ah, o sea que sí puedes enojarte? Pensé que los adolescentes de hoy en día ya no sentían nada" gritaste en tono de burla. Negasonic Teenage Warhead usó sus poderes para lanzar una onda de energía hacia ti, que te lanzó volando a través de la sala hasta chocar con el sofá, rompiéndolo.

Te pusiste de pie rápidamente y decidiste atacarla con''', ['tus Katanas', 'tu arma'], [6, Code.DKTMU]),
        'state': True
    },
    1: {
        'name': "Yukio",
        'pictureRoute': "/",
        'miniatureRoute': "/",
        'miniatureDeadRoute': "/",
        'fightContent': NodeSimple(NodeType.STORY, '''Terminaste con ella con un sólo disparo en la frente y su cuerpo inerte cayó al suelo.

Cegada por su amor por Negasonic Teenage Warhead y conmocionada por su muerte, Yukio salió corriendo hacia ti mientras gritaba "¡Maldito! ¡¡Mataste a mi novia!!". En un rápido movimiento decidiste''', ['hacerle zancadilla', 'dispararle'], [Code.DKTMU, 7]),
        'state': True
    },
    2: {
        'name': "Coloso",
        'pictureRoute': "/",
        'miniatureRoute': "/",
        'miniatureDeadRoute': "/",
        'fightContent': NodeSimple(NodeType.STORY, '''Coloso llegó corriendo a la sala y al ver los cadáveres de Negasonic Teenage Warhead y de Yukio se abalanzó sobre ti furioso, derribándote al suelo. "¿No has considerado una dieta?" dijiste, sin poder respirar por el peso de su cuerpo sobre el tuyo. "Te vendría bien adelgazar unos cuantos kilos".

Al levantarse, Coloso te lanzó por los aires, pero por suerte al caer notaste cerca a ti en el suelo''', ['un hacha', 'un taladro'], [8, Code.DKTMU]),
        'state': True
    },
    3: {
        'name': "Iron Man",
        'pictureRoute': "/",
        'miniatureRoute': "/",
        'miniatureDeadRoute': "/",
        'fightContent': NodeSimple(NodeType.STORY, '''"Te sugiero que discutamos esto con un whiskey y no con armas, o si no las cosas se pondrán feas" aconsejó Iron Man en un tono serio. "¿Feas dices?" soltaste una fuerte risa. "Cariño, las cosas siempre se ponen feas cuando estoy involucrado".

Ponto comenzaron una pelea, Iron Man disparándote ráfagas de energía con sus repulsores y tú contraatacando con tus katanas. Lograste romper su traje metálico y dejar el rostro de Iron Man al aire libre. Entonces le''', ['disparaste en la frente', 'cortaste la cabeza'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
    4: {
        'name': "Hulk",
        'pictureRoute': "/",
        'miniatureRoute': "/",
        'miniatureDeadRoute': "/",
        'fightContent': NodeSimple(NodeType.STORY, '''"¿Pero qué demonios está pasando aquí?" justo en el segundo en que matabas a Iron Man escuchaste la voz de Bruce Banner saliendo del ascensor y entrando a la sala de reuniones. Al ver el cadáver de Tony en el suelo y a ti junto a él se transformó en Hulk inmediatamente.

"¡Hulk aplasta mariquita!" gritó corriendo hacia ti. "Espera, ¿en serio acabas de llamarme mariquita?" soltaste una fuerte carcajada, pero Hulk no hablaba en broma y te aplastó contra el piso de un fuerte puño.''', ['burlarte de él', 'sacar tus katanas'], [Code.DKTMU, Code.DKTMU]),
        'state': True
    },
}

