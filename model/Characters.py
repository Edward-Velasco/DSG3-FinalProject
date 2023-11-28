# Ejemplo de conjuntos disyuntos
# Cada valor debe ser un objeto de tipo Character!

from modelView.Types import Code, NodeType
from modelView.Character import Character
from modelView.nodes.NodeSimple import NodeSimple

Characters = {
    # Use this example when Character class is implemented
    # 0: Character("Ironman", "/", "/", "/", NodeSimple("Air battle", ["Stab the head", "Rip off a leg"], [Code.DKTMU, 101])),

    0: Character("Negasonic T. W.",
                 "view/assets/characters/nodes/negasonic.png",
                 "view/assets/characters/mini_alive/negasonic-vivo.png",
                 "view/assets/characters/mini_dead/negasonic-muerto.png",
                 (175,160),
                 NodeSimple(NodeType.STORY, '''"Ah, o sea que sí puedes enojarte? Pensé que los adolescentes de hoy en día ya no sentían nada" gritaste en tono de burla. Negasonic Teenage Warhead usó sus poderes para lanzar una onda de energía hacia ti, que te lanzó volando a través de la sala hasta chocar con el sofá, rompiéndolo.

Te pusiste de pie rápidamente y decidiste atacarla con''', ['tus Katanas', 'tu arma'], [6, Code.DKTMU])
                ),
    1: Character("Yukio",
                "view/assets/characters/nodes/yukio.png",
                "view/assets/characters/mini_alive/yukio-vivo.png",
                "view/assets/characters/mini_dead/yukio-muerto.png",
                (380,160),
                NodeSimple(NodeType.STORY, '''Terminaste con ella con un solo disparo en la frente y su cuerpo inerte cayó al suelo.

Cegada por su amor por Negasonic Teenage Warhead y conmocionada por su muerte, Yukio salió corriendo hacia ti mientras gritaba "¡Maldito! ¡¡Mataste a mi novia!!". En un rápido movimiento decidiste''', ['hacerle zancadilla', 'dispararle'], [Code.DKTMU, 7])
                ),
    2: Character("Coloso",
                "view/assets/characters/nodes/coloso.png",
                "view/assets/characters/mini_alive/coloso-vivo.png",
                "view/assets/characters/mini_dead/coloso-muerto.png",
                (275, 265),
                NodeSimple(NodeType.STORY, '''Coloso llegó corriendo a la sala y al ver los cadáveres de Negasonic Teenage Warhead y de Yukio se abalanzó sobre ti furioso, derribándote al suelo. "No has considerado una dieta?" dijiste, sin poder respirar por el peso de su cuerpo sobre el tuyo. "Te vendría bien adelgazar unos cuantos kilos".

Al levantarse, Coloso te lanzó por los aires, pero por suerte al caer notaste cerca a ti en el suelo''', ['un hacha', 'un taladro'], [8, Code.DKTMU])
                ),
    3: Character("Iron Man",
                "view/assets/characters/nodes/ironman.png",
                "view/assets/characters/mini_alive/ironman-vivo.png",
                "view/assets/characters/mini_dead/ironman-muerto.png",
                (520,160),
                NodeSimple(NodeType.STORY, '''"Te sugiero que discutamos esto con un whiskey y no con armas, o si no las cosas se pondrán feas" aconsejó Iron Man en un tono serio. "Feas dices?" soltaste una fuerte risa. "Cariño, las cosas siempre se ponen feas cuando estoy involucrado".

Ponto comenzaron una pelea, Iron Man disparándote ráfagas de energía con sus repulsores y tú contraatacando con tus katanas. Lograste romper su traje metálico y dejar el rostro de Iron Man al aire libre. Entonces le''', ['disparaste en la frente', 'cortaste la cabeza'], [Code.DKTMU, Code.DKTMU])
                ),
    4: Character("Hulk",
                "view/assets/characters/nodes/hulk.png",
                "view/assets/characters/mini_alive/hulk-vivo.png",
                "view/assets/characters/mini_dead/hulk-muerto.png",
                (670,160),
                NodeSimple(NodeType.STORY, '''"Pero qué demonios está pasando aquí?" justo en el segundo en que matabas a Iron Man escuchaste la voz de Bruce Banner saliendo del ascensor y entrando a la sala de reuniones. Al ver el cadáver de Tony en el suelo y a ti junto a él se transformó en Hulk inmediatamente.

"¡Hulk aplasta mariquita!" gritó corriendo hacia ti. "Espera, en serio acabas de llamarme mariquita?" soltaste una fuerte carcajada, pero Hulk no hablaba en broma y te aplastó contra el piso de un fuerte puño.''', ['burlarte de él', 'sacar tus katanas'], [Code.DKTMU, Code.DKTMU])
                ),
    5: Character("Doctor Strange",
                "view/assets/characters/nodes/doctor.png",
                "view/assets/characters/mini_alive/doctor-vivo.png",
                "view/assets/characters/mini_dead/doctor-muerto.png",
                (1020, 160),
                NodeSimple(NodeType.STORY, '''Doctor Strange se acercó a ti con las manos en alto, rindiéndose. "Espera, maguito. De verdad no piensas pelear?" interrogaste. "Ya vi todos los futuros posibles y en todos me matas y te llevas el Ojo de Agamotto. No tiene caso pelear" explicó resignado.

"Oh, es una lástima, Harry Potter. Pensé que iba a divertirme contigo y con tu capita mágica".''', ['Cortar cabeza', 'Tiro en la frente'], [Code.DKTMU, Code.DKTMU])
                ),
    6: Character("Star-Lord",
                "view/assets/characters/nodes/starlord.png",
                "view/assets/characters/mini_alive/starlord-vivo.png",
                "view/assets/characters/mini_dead/starlord-muerto.png",
                (810, 160),
                NodeSimple(NodeType.STORY, '''Disparaste, pero Star-Lord fue más rápido y no sólo se agachó antes de la bala saliera de tu arma, sino que además te hizo zancadilla en un rápido movimiento y luego te apuntó con su arma psicodélica. O se llamaba arma intergaláctica?

"Explícate. Quién te mandó?" exigió Star-Lord, sin mover su arma.''', ['"Tu mamá"', '"Vengo del futuro"'], [Code.DKTMU, Code.DKTMU])
                ),
    7: Character("Groot",
                "view/assets/characters/nodes/groot.png",
                "view/assets/characters/mini_alive/groot-vivo.png",
                "view/assets/characters/mini_dead/groot-muerto.png",
                (930, 260),
                NodeSimple(NodeType.STORY, '''En un rápido movimiento te pusiste de pie mientras sacabas tus katanas y le cortaste la garganta a Star-Lord, quien cayó de rodillas agonizando.

El mapache se acercó para ayudar a Star-Lord, mientras que el hombre árbol salió corriendo hacia ti.''', ['Burlarte', 'Hacer un chiste'], [Code.DKTMU, Code.DKTMU])
                ),
    8: Character("Rocket Raccoon",
                "view/assets/characters/nodes/rocket.png",
                "view/assets/characters/mini_alive/rocket-vivo.png",
                "view/assets/characters/mini_dead/rocket-muerto.png",
                (810,370),
                NodeSimple(NodeType.STORY, '''"Cuál es tu poder especial? Hacer fotosíntesis?" preguntaste, riendo. Groot alargó una de sus manos y la usó para estrangularte, pero rápidamente la cortaste usando tus katanas. Luego seguiste cortando hasta que en unos segundos Groot no era más que tajadas de papel.

"Pagarás por esto!" gritó el mapache, Rocket Raccoon, corriendo hacia ti.''', ['"No lo creo"', '"Algún día"'], [Code.DKTMU, Code.DKTMU])
                ),
    9: Character("Gamora",
                "view/assets/characters/nodes/gamora.png",
                "view/assets/characters/mini_alive/gamora-vivo.png",
                "view/assets/characters/mini_dead/gamora-muerto.png",
                (670,375),
                NodeSimple(NodeType.STORY, '''Gamora hizo un movimiento ágil para agacharse al suelo, tomar de vuelta su daga y luego clavarla en tu pecho, pero entonces quedó perpleja al ver como tú no morías ni aparentabas dolor.

Mientras Gamora estaba sorprendida e inmóvil tú le disparaste''', ['en el cuello', 'en el pecho'], [Code.DKTMU, Code.DKTMU])
                ),
    10: Character("Thanos",
                 "view/assets/characters/nodes/thanos.png",
                 "view/assets/characters/mini_alive/thanos-vivo.png",
                 "view/assets/characters/mini_dead/thanos-muerto.png",
                 (560,515),
                 NodeSimple(NodeType.STORY, '''Disparaste una, dos y tres veces y Gamora cayó muerta. "Ain, pensé que pelear con la chica Grinch iba a ser más divertido" fue tu única reacción.

"Pero qué has hecho??" Thanos, enfúrecido, te lanza fuera de la montaña de un golpe y al caer de tal altura te rompes la mayoría de los huesos. Después de unos minutos, ya recuperado, te teletransportas junto a Thanos y gritas''', ['"Debilucho decías??"', '"No hemos terminado"'], [Code.DKTMU, Code.DKTMU])
                 ),
    11: Character("Red Skull",
                 "view/assets/characters/nodes/skull.png",
                 "view/assets/characters/mini_alive/skull-vivo.png",
                 "view/assets/characters/mini_dead/skull-muerto.png",
                 (1020,400),
                 NodeSimple(NodeType.STORY, '''"Por tu cabeza... Bueno, por tu cráneo. Tú entiendes a lo que me refiero" el chiste no salió tan bien, pero estabas aquí por la pelea. 

Disparaste varias veces, pero las balas parecían no hacerle ningún efecto a Red Skull, por lo que usaste la Gema de''', ['el Espacio', 'el Poder'], [59, Code.DKTMU])
                 ),
    12: Character("Thor",
                 "view/assets/characters/nodes/thor.png",
                 "view/assets/characters/mini_alive/thor-vivo.png",
                 "view/assets/characters/mini_dead/thor-muerto.png",
                 (550,285),
                 NodeSimple(NodeType.STORY, '''"Una pelea, eso es lo que quiero. Una buena pelea en serio" explicaste, sacando tus katanas. "Con que Dios del Trueno, no es así? Muéstrame lo que tienes".

Thor lanzó tu martillo a tu entrepierna y caíste de rodillas del dolor.''', ['"Auch! Tacho"', '"No se vale!"'], [Code.DKTMU, Code.DKTMU])
                 ),
    13: Character("Loki",
                 "view/assets/characters/nodes/loki.png",
                 "view/assets/characters/mini_alive/loki-vivo.png",
                 "view/assets/characters/mini_dead/loki-muerto.png",
                 (440,420),
                 NodeSimple(NodeType.STORY, '''Te tomó unos minutos recuperarte, pero Thor te esperó como un caballero. Luego le cortaste la cabeza.

"Pero qué demonios??" gritó Loki, quien no alcanzó a reaccionar antes para evitar su muerte.''', ['"Toma eso!"', '"Y sin gemas!"'], [Code.DKTMU, Code.DKTMU])
                 ),
    14: Character("Black Panther",
                 "view/assets/characters/nodes/black.png",
                 "view/assets/characters/mini_alive/black-vivo.png",
                 "view/assets/characters/mini_dead/black-muerto.png",
                 (170,375),
                 NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                 ),
    15: Character("Shuri",
                 "view/assets/characters/nodes/shuri.png",
                 "view/assets/characters/mini_alive/shuri-vivo.png",
                 "view/assets/characters/mini_dead/shuri-muerto.png",
                 (310,375),
                 NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                 ),
    16: Character("Wanda",
                 "view/assets/characters/nodes/wanda.png",
                 "view/assets/characters/mini_alive/wanda-vivo.png",
                 "view/assets/characters/mini_dead/wanda-muerto.png",
                 (170,515),
                 NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                 ),
    17: Character("Vision",
                 "view/assets/characters/nodes/vision.png",
                 "view/assets/characters/mini_alive/vision-vivo.png",
                 "view/assets/characters/mini_dead/vision-muerto.png",
                 (310,515),
                 NodeSimple(NodeType.STORY, '''XXX''', ['1', '2'], [Code.DKTMU, Code.DKTMU])
                 ),
    18: Character("Black Widow",
                 "view/assets/characters/nodes/widow.png",
                 "view/assets/characters/mini_alive/widow-vivo.png",
                 "view/assets/characters/mini_dead/widow-muerto.png",
                 (755,515),
                 NodeSimple(NodeType.STORY, '''"No, no lo soy. Pero ese fantasmón ya no les va a servir de nada" dijiste mientras le cortabas el cuello a Black Widow con una de tus katanas.

Haweye sacó su arco rápidamente y comenzó a lanzarte flechas, que simplemente atravesaban tu cuerpo sin matarte. "O, pero miren que tenemos aquí, es''', ['Robin Hood!"', 'Legolas!"'], [Code.DKTMU, Code.DKTMU])
                 ),
    19: Character("Hawkeye",
                 "view/assets/characters/nodes/hawkeye.png",
                 "view/assets/characters/mini_alive/hawkeye-vivo.png",
                 "view/assets/characters/mini_dead/hawkeye-muerto.png",
                 (920,515),
                 NodeSimple(NodeType.STORY, '''Después de tu mal chiste te acercaste al arquerito y cortaste su cuello al igual que habías hecho con Black Widow. Ya no quedaba más sino teletransportarte de vuelta a la tierra para''', ['Comer', 'Bailar'], [Code.DKTMU, Code.DKTMU])
                 )
}

