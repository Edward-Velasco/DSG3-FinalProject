# Ejemplo de estructura de árbol

from modelView.Types import NodeType, InfinityStones

StoryTree = {
    1: {
        'type': NodeType.BLANK,
        'content': '''"Ah... o sea que tu eres el idiota que va a estar jugando mi videojuego? Esperaba a alguien más guapo, pero como sea, supongo que este videojuego tuvo tanto éxito que llegó a las manos de cualquiera.

Empecemos con la acción. Supongo que te estás preguntando cuál es el plan tan asombroso que mencioné. Bueno, es muy sencillo: últimamente mientras cago he estado leyendo los cómics de payasos coloridos de esta empresa llamada "Marvel" y me llegó la inspiración de repente..."''',
        'children': [2]
    },
    2: {
        'type': NodeType.BLANK,
        'content': '''"Hay tantos héroes de colorcitos con poderes tan diversos que quizás alguno de ellos tenga los suficientes huevos como para matarme. Y con huevos me refiero a algún poder extraño, algo que sea más fuerte que mi maldita mutación que me mantiene vivo.

Así que no, este no es un videojuego sobre un héroe lameculos con calzones de colores que salva gatitos en peligro. Este es un videojuego sobre mí, un imbécil que debería estar muerto y va a hacer enojar a todo el puto Universo Marvel con la esperanza de que alguien logre matarlo..."''',
        'children': [3]
    },
    3: {
        'type': NodeType.BLANK,
        'content': '''"Entonces, qué dices? Listo para patear los supertraseros de algunos superidiotas?

Comencemos por Coloso, el grandulón que está a punto de entrar por esa puerta."''',
        'children': [4]
    },
    4: {
        'type': NodeType.STORY,
        'content': '''Después de hacer explotar todo tu cuerpo en pedazos Coloso te encuentra y te lleva a la mansión de los X-men, donde después de dos días de reposo todo tu cuerpo vuelve a regenerarse hasta quedar como nuevo.

Y claro, con "como nuevo" nos referimos a que sigues teniendo esa cara horrenda que siempre has tenido desde la mutación que te transformó en Deadpool.

Después de dos días de comer y beber a gusto decides que es momento de iniciar tu plan, por lo que''',
        'options': ['le disparas a Negasonic T. W.', 'insultas a Yukio'],
        'children': [5, 5]
    },

    # Used to tell the program the story is over
    5: {
        'type': NodeType.FIGHT,
        'content': '"Pero cuál es tu puto problema, anciano??"',
        'options': ['Iniciar una pelea'],
        'children':[9],
        'character': 0,
        'set': 0
    },
    6: {
        'type': NodeType.BLANK,
        'content': '''No, eso fue una muy mala idea... Intentaste acercarte a Negasonic Teenage Warhead una y otra vez con tus Katanas, pero ella usaba sus poderes para sacarte volando. Después de sólo unos minutos una gran parte de la mansión estaba destrozada, columnas y ventanas rotas, muebles hechos trizas...

Cuando Coloso llegó a la sala y vio el alboroto te sacó de la mansión X-men y te tiró al suelo, diciendo que no quería volver a verte.''',
        'children': [10]
    },
    7: {
        'type': NodeType.BLANK,
        'content': '''Le disparaste a Yukio una, dos, tres, cuatro veces, pero logró esquivar todas tus balas haciendo una voltereta doble y al caer partió tu cuello de una fuerte patada.

Coloso llegó corriendo a la sala por todo el alboroto y detuvo a Yukio antes de que pudiera matarte, pero al ver el cadáver de Negasonic Teenage Warhead enfureció y te lanzó por la ventana, gritando que nunca más quería volver a verte en la mansión X-men.''',
        'children': [10]
    },
    8: {
        'type': NodeType.BLANK,
        'content': '''Tomaste el hacha del suelo y golpeaste a Coloso en el cuello, esperando cortar su cabeza de lado a lado, pero, olvidaste un pequeño detalle: Coloso está hecho de metal y ningún tipo de metal puede cortarlo... Es como intentar romper una cuchara con un tenedor.

Todavía enfurecido, Coloso te lanzó por la ventana, gritando que nunca más quería volver a verte en la mansión X-men.''',
        'children': [10]
    },
    9: {
        'type': NodeType.BLANK,
        'content': '''Perforaste el pecho de Coloso usando el taladro para metal que encontraste convenientemente en el suelo y pronto cayó muerto. Luego, en una escena de transición, te pusiste de pie y comenzaste a recorrer la mansión X-men bailando al buen ritmo de la canción «Young Guns» de Wham! para celebrar tu victoria.

Fue entonces cuando notaste algo inusual pegado a la nevera con un imán: una tarjeta con el número de Tony Stark. Ahí estaba tu próximo rival.''',
        'children': [11]
    },
    10: {
        'type': NodeType.BLANK,
        'content': '''Lo que Coloso no sabía es que todo era parte de tu plan y mientras peleabas no estabas pensando en ganar, sino simplemente en robarte una tarjeta que estaba pegada en la nevera...

Una tarjeta que tenía el número de Tony Stark. Y ahora estaba en tus manos.''',
        'children': [11]
    },
    11: {
        'type': NodeType.BLANK,
        'content': '''Llamaste a Tony Stark y le pediste una reunión formal, con la supuesta excusa de querer unirte a los Vengadores, para combatir contra los chicos malos que amenazan con destruir el universo como lo conocemos.

Una vez en la Torre Stark sacaste tu pistola y le apuntaste a Tony. No estabas de ánimos para fingir que te importaba una mierda el destino del universo. Tony se transformó rápidamente en Iron Man con su traje portátil y te apuntó con una mano.''',
        'children': [12]
    },
    12: {
        'type': NodeType.DIALOGUE,
        'content': '''"Pero que malos modales, chico. No querías una reunión para charlar? Baja el arma y hablémoslo"''',
        'options': ['"Habla con la mano"', '"Eso no pasará"'],
        'children': [13,13],
        'character': 3
    },
    13: {
        'type': NodeType.FIGHT,
        'content': '"Qué es lo que quieres, Deadpool?"',
        'options': ['"Tu cabeza"'],
        'children':[14],
        'character': 3,
        'set': 1
    },
    14: {
        'type': NodeType.BLANK,
        'content': '''"Calma, Shrek" dijiste poniéndote de pie mientras tu cuerpo se recomponía. "Si quieres puedo darte el número de mi terapeuta, para que hablen de esos problemitas de ira que tienes".

Después de unos cuantos movimientos rápidos, pero que fueron mostrados en cámara lenta para que se viera más épico, dejas a Hulk muerto en el suelo, con varios tiros en su frente y varias partes de su cuerpo cortadas por tus rápidas katanas.''',
        'children': [15]
    },
    15: {
        'type': NodeType.BLANK,
        'content': '''Decides darte un paseito por la Torre Stark, matando a uno que otro guardia que se cruza por tu camino mientras suena una buena música de fondo, y cuando llegas al último piso descubres algo extraño: una gema azul, brillante, dentro de lo que parece ser un laboratorio del fallecido Tony Stark.''',
        'children': [16]
    },
    16: {
        'type': NodeType.SPECIAL,
        'content': '''Rompes todo el laboratorio y tomas la gema azul con tus manos. Al verla de cerca te das cuenta de que es justo lo que pensaste: se trata de la famosa Gema del Espacio, de la que habías leído antes en tus cómics de Marvel.

Usando su poder decides teletransportarte a''',
        'options': ['el Sanctum Sanctorum','una galaxia lejana'],
        'children': [17,18],
        'stone': InfinityStones.BLUE
    },
    17: {
        'type': NodeType.BLANK,
        'content': '''Te teletransportas a el Sanctum Sanctorum para buscar al maguito de capa que habías visto en tus cómics y rápidamente lo encuentras en la biblioteca leyendo un librito misterioso.''',
        'children': [19]
    },
    18: {
        'type': NodeType.BLANK,
        'content': '''Te teletransportas a una galaxia lejana aleatoria. De inmediato le preguntas a un nativo de la zona dónde te encuentras y te responde que estás en el planeta Morag.

Caminando por allí mientras buscas un bar ves a los Guardianes de la Galaxia protegiendo el Orbe. Sin dudarlo te acercas a saludar muy amablemente, es decir, con tu arma le apuntas en la cabeza a quien parece ser el líder.''',
        'children': [29]
    },
    19: {
        'type': NodeType.DIALOGUE,
        'content': '''"Sabía que vendrías, Deadpool"''',
        'options': ['"Ah sí?"', 'Reír'],
        'children': [20,21],
        'character': 5
    },
    20: {
        'type': NodeType.BLANK,
        'content': '''"Ah sí?" respondiste sacando una de tus katanas. "Entonces también sabes que vengo a cortarte el cuello".''',
        'children': [22]
    },
    21: {
        'type': NodeType.BLANK,
        'content': '''Reíste sacando una de tus katanas. "Entonces también sabes que vengo a cortarte el cuello".''',
        'children': [22]
    },
    22: {
        'type': NodeType.FIGHT,
        'content': '''Hagamos esto rápido.''',
        'options': ['"Más rápido, bebé?"'],
        'children':[23],
        'character': 5,
        'set': 2
    },
    23: {
        'type': NodeType.BLANK,
        'content': '''Cuando Doctor Strange cayó al piso muerto te acercaste a su cadáver para quitarle el collar místico. "Ojo de qué cosa? Como sea, sólo me importa la piedrita verde que está adentro" al decir esto rompiste la reliquia y sacaste la gema verde.''',
        'children': [24]
    },
    24: {
        'type': NodeType.SPECIAL,
        'content': '''Ahora tienes en tu posesión la inigualable Gema del Tiempo. Podrías usarla para ver todos los futuros posibles o podrías simplemente seguir con tu vida matando héroes como si nunca hubieras encontrado la gema.

Decides''',
        'options': ['Ver los futuros','Seguir adelante'],
        'children': [25,26],
        'stone': InfinityStones.GREEN
    },
    25: {
        'type': NodeType.BLANK,
        'content': '''Con la Gema del Tiempo en tus manos te sientas en el suelo de la biblioteca, sabiendo que esto tomará un rato, y observas todos los futuros posibles.

Y entonces lo ves. Ves un futuro en el que logras revivir a Vanessa y son felices juntos.''',
        'children': [27]
    },
    26: {
        'type': NodeType.BLANK,
        'content': '''Ignorando los poderes de la Gema del Tiempo, decides googlear "planetas épicos del Universo Marvel" y entre las opciones te llama la atención un planeta llamado Morag.

Suena a un planeta con gente poderosa en el que ocurren peleas épicas... o también suena como la banda 'Morat', pero decidiste ignorar eso.''',
        'children': [28]
    },
    27: {
        'type': NodeType.BLANK,
        'content': '''Así que harás todo lo posible por seguir ese plan al pie de la letra.

Primera parada: un planeta llamado Morag, un lugar en el que nunca has estado pero sin problema matarás a todo el mundo de todas formas.''',
        'children': [28]
    },
    28: {
        'type': NodeType.BLANK,
        'content': '''Te teletransportas a Morag y de inmediato ves a los Guardianes de la Galaxia protegiendo el Orbe. 

Sin duda te acercas a saludar muy amablemente, es decir, con tu arma le apuntas en la cabeza a quien parece ser el líder.''',
        'children': [29]
    },
    29: {
        'type': NodeType.DIALOGUE,
        'content': '''"Baja el arma. Ya mismo" dijo, apuntándote con una pistola que era casi tan grande como todo su cuerpo.''',
        'options': ['"Aw, un mapache"', '"No lo haré"'],
        'children': [30,30],
        'character': 8
    },
    30: {
        'type': NodeType.DIALOGUE,
        'content': '''"Calma, Rocket. Lo tengo bajo control" dijo hacia su compañero y luego te habló a ti a los ojos. "Quién putas eres y qué clase de arma patética es esa?"''',
        'options': ['Reír', 'Explicar'],
        'children': [31,32],
        'character': 6
    },
    31: {
        'type': NodeType.BLANK,
        'content': '''"Ah, no conocen mi nombre?" preguntaste riendo. "Pues no lo necesitan, de todas formas morirán en unos cuantos minutos".''',
        'children': [33]
    },
    32: {
        'type': NodeType.BLANK,
        'content': '''"Mi nombre es Deadpool, pero el día de hoy estoy interpretando el papel de 'El puto asesino que les vuela los sesos'" explicaste, sin retirar la pistola de la cabeza del muchacho.''',
        'children': [33]
    },
    33: {
        'type': NodeType.FIGHT,
        'content': '''"Ah sí? Pues eso lo veremos"''',
        'options': ['Pelear'],
        'children':[34],
        'character': 6,
        'set': 3
    },
    34: {
        'type': NodeType.BLANK,
        'content': '''Saltas por los aires y clavas al mapache al suelo con una de tus katanas.

"Dime dónde está la chica de su grupo" exiges mientras Rocket agoniza sin poder moverse.''',
        'children': [36]
    },
    36: {
        'type': NodeType.BLANK,
        'content': '''"Quién? Mantis?" respondió Rocket, con dificultad por el dolor.

"No, no la chica insecto" explicaste exacerbado. "La chica verde, la super asesina".''',
        'children': [37]
    },
    37: {
        'type': NodeType.BLANK,
        'content': '''"Gamora" respondió Rocket. "No sé dónde está ahora... La última vez que hablamos por WhatsApp me dijo que estaba con su padre y que iban a buscar la Gema del Alma juntos. Ya sabes, como plan familiar".

"Gracias por tu servicio, mapache" fue lo último que dijiste antes de dispararle en la cabeza y terminar con su vida definitivamente.''',
        'children': [38]
    },
    38: {
        'type': NodeType.BLANK,
        'content': '''Googleaste "dónde se encuentra la gema del alma" y el todopoderoso Dios Google te respondió que estaba en el planeta Vormir.

Ibas a teletransportarte de inmediato allá, pero entonces notaste el Orbe, el objeto misterioso que los Guardianes de la Galaxia estaban cargando cuando los emboscaste y ahora estaba en el suelo sin protección.''',
        'children': [39]
    },
    39: {
        'type': NodeType.BLANK,
        'content': '''Los objetos místicos dentro del Universo Marvel sólo pueden significar algo muy poderoso, así sin esperar ni un segundo tomaste el arma del mapache muerto y le disparaste al Orbe.

Al abrirse encontraste en su interior una brillante gemita morada.''',
        'children': [40]
    },
    40: {
        'type': NodeType.SPECIAL,
        'content': '''No sabías su nombre así que lo googleaste. 'Gema del Poder', así se llamaba. Era un nombre genial, mucho mejor que el de todas las otras gemas.

Como propietario de la Gema del Poder decides probar sus poderes destruyendo''',
        'options': ['todo Morag','un edificio'],
        'children': [41,42],
        'stone': InfinityStones.PURPLE
    },
    41: {
        'type': NodeType.BLANK,
        'content': '''Como propietario de la Gema del Poder decides probar sus poderes destruyendo todo el planeta Morag. Tarea que te resulta bastante sencilla.

Justo antes de que el planeta colapse sobre sí mismo bajo tus pies logras teletransportarte a Vormir para seguir con tu misión de enfrentarte a todo el Universo Marvel.''',
        'children': [43]
    },
    42: {
        'type': NodeType.BLANK,
        'content': '''Como propietario de la Gema del Poder decides probar sus poderes destruyendo un edificio cercano. Tarea que te resulta bastante sencilla, pero luego sueltas un pequeño "Ups" al ver a varias personas cayendo por las ventanas del edificio y luego muriendo aplastadas por él.

Decides ignorar lo que pasó y teletransportarte a Vormir para seguir con tu misión de enfrentarte a todo el Universo Marvel.''',
        'children': [43]
    },
    43: {
        'type': NodeType.BLANK,
        'content': '''Al llegar a Vormir divisas a Thanos y a Gamora subiendo una montaña oscura. En seguida te teletrasportas a su lado y sigues subiendo la montaña junto a ellos.

"Hola. Cómo están?" saludas con naturalidad. "Que buen día para hacer senderismo, no creen?".''',
        'children': [44]
    },
    44: {
        'type': NodeType.DIALOGUE,
        'content': '''"Quién eres? También vienes por la Gema del Alma?" preguntó sosteniendo su daga frente a tu cuello.''',
        'options': ['Negar', 'Coquetearle'],
        'children': [45,45],
        'character': 9
    },
    45: {
        'type': NodeType.BLANK,
        'content': '''"No. En realidad vengo por ti, guapa" dijiste haciendo un gesto coqueto, pero por desgracia cayendo en cuenta tarde de que no se vería a través de la máscara. Gamora se mantuvo inmóvil.

"Verás, mi nombre es Deadpool y según los cómics tú eres una de las asesinas más temidas del universo" seguiste. "Por eso vengo a proponerte un duelo".''',
        'children': [46]
    },
    46: {
        'type': NodeType.DIALOGUE,
        'content': '''"Y qué te hace creer que eres digno de tener un duelo conmigo?"''',
        'options': ['"Mi reputación"', '"Mi carisma"'],
        'children': [47,47],
        'character': 9
    },
    47: {
        'type': NodeType.DIALOGUE,
        'content': '''"Déjalo, Gamora. Tenemos una misión importante que cumplir, no podemos perder tiempo con este debilucho."''',
        'options': ['Ofenderte', 'Amenazar'],
        'children': [48,49],
        'character': 10
    },
    48: {
        'type': NodeType.BLANK,
        'content': '''"Perdón?? Debilucho dijiste??" preguntaste completamente ofendido. "Apuesto a que no imaginas de lo que soy capaz".

Rápidamente golpeaste el brazo de Gamora, haciendo que dejara caer su daga al suelo, y luego le apuntaste en el cuello con tu pistola. "Si quieres seguir acompañando a tu papá en su salida familiar entonces tendrás que pasar sobre mi cadáver".''',
        'children': [50]
    },
    49: {
        'type': NodeType.BLANK,
        'content': '''Rápidamente golpeaste el brazo de Gamora, haciendo que dejara caer su daga al suelo, y luego le apuntaste en el cuello con tu pistola.

"Pues lamento informártelo hasta ahora, grandulón, pero la princesa Fiona tendrá que pasar sobre mi cadáver si quiere seguir con esa misión que tiene pendiente contigo".''',
        'children': [50]
    },
    50: {
        'type': NodeType.DIALOGUE,
        'content': '''"Quieres que lo aplaste de un sólo puño, querida?"''',
        'options': ['"Awww"', '"Inténtalo"'],
        'children': [51,51],
        'character': 10
    },
    51: {
        'type': NodeType.FIGHT,
        'content': '''"No. Déjalo, papá. Quiero matar a este yo misma"''',
        'options': ['"Éntrale entonces"'],
        'children':[52],
        'character': 9,
        'set': 4
    },
    52: {
        'type': NodeType.BLANK,
        'content': '''Thanos, aún enojado por la muerte de su hija favorita, te aplasta contra el suelo y en ese momento, mientras agonizas, recuerdas que tienes la Gema del Poder contigo.

Al recuperarte del golpe sacas la gema moradita de tu bolsillo y acabas con Thanos en una explosión que destruye gran parte de la montaña. "Miren eso! Monstruo morado vencido con una gema morada" dices al aire sonriendo satisfecho.''',
        'children': [53]
    },
    53: {
        'type': NodeType.BLANK,
        'content': '''De repente curioso por la misión familiar de los fallecidos Gamora y Thanos decides terminar de subir la montaña, pero pronto te cansas y mejor te teletransportas hasta la cima.

Allí encuentras a un tipo rojo con capa negra.''',
        'children': [54]
    },
    54: {
        'type': NodeType.DIALOGUE,
        'content': '''"Es gracioso, esta es la primera vez que pasa esto".''',
        'options': ['"Me hablas a mí?"', '"Tú eres?"'],
        'children': [55,55],
        'character': 11
    },
    55: {
        'type': NodeType.DIALOGUE,
        'content': '''"Mi nombre es Red Skull. Fui desterrado aquí para guíar a quienes vengan a Vormir hacia la Gema del Alma y al verte iba a comenzar con mi discurso, todo eso de 'Para reclamar la Gema del Alma debes sacrificar aquello que más amas, blablabla'... pero esta es la primera vez que no es necesario".''',
        'options': ['"Qué?"', '"Explícate"'],
        'children': [56,56],
        'character': 11
    },
    56: {
        'type': NodeType.DIALOGUE,
        'content': '''"Es cierto, para poder tener la Gema del Alma tienes que perder aquello que más amas... pero tú ya lo perdiste. Ya no queda nada en este mundo que ames.

Así que la gema es tuya".''',
        'options': ['"En serio?"', '"Así sin más?"'],
        'children': [57,57],
        'character': 11
    },
    57: {
        'type': NodeType.SPECIAL,
        'content': '''Viste una luz azul cubrir toda la montaña y luego, sin darte cuenta cómo habías llegado ahí, te encontrabas flotando en un lago, sosteniendo la Gema del Alma en tus manos.

Saltaste de la alegría y decidiste volver a teletransportarte a la cima de la montaña para agradecerle a Red Skull, es decir pegarle un tiro en el cráneo... Literalmente en el cráneo.''',
        'options': ['"Hola bebé"','"Regresé"'],
        'children': [58,58],
        'stone': InfinityStones.ORANGE
    },
    58: {
        'type': NodeType.FIGHT,
        'content': '''"Oh, volviste."''',
        'options': ['"Por tu cabeza"'],
        'children':[60],
        'character': 11,
        'set': 5
    },
    59: {
        'type': NodeType.BLANK,
        'content': '''Decidiste usar la Gema del Espacio para teletransportarte a otra parte alejada de la montaña. No porque seas un cobarde, sino porque Red Skull no estaba dando una buena pelea así que no tenía sentido seguir con ella.

Entonces viste a Black Widow y a Hawkeye, que venían subiendo la montaña de Vormir mientras charlaban.''',
        'children': [61]
    },
    60: {
        'type': NodeType.BLANK,
        'content': '''Usaste la Gema del Poder nuevamente y convertiste a Red Skull en polvo instantáneamente. Esa gemita morada se estaba convirtiendo en tu mejor amiga.

Sin más que hacer decidiste viajar a otro lugar de la galaxia, un lugar donde sí hubieran buenas peleas. El destino que elegiste fue Asgard, el hogar de los dioses griegos. O eran noruegos? Como sea, de seguro ellos sí saben pelear de verdad.''',
        'children': [65]
    },
    61: {
        'type': NodeType.DIALOGUE,
        'content': '''"Después de salvar el mundo deberíamos sentar cabeza... comprar una cabaña... mudarnos a Canadá... No sé, qué opinas?" habló sonriéndole a Black Widow.''',
        'options': ['"Recién casados?"', '"Awww"'],
        'children': [62,62],
        'character': 19
    },
    62: {
        'type': NodeType.FIGHT,
        'content': '''"Quién eres y qué haces aquí?" preguntó apuntándote con su arma. "Ah, espera... Tú eres Red Skull?"''',
        'options': ['Asesinar'],
        'children':[63],
        'character': 18,
        'set': 8
    },
    63: {
        'type': NodeType.BLANK,
        'content': '''Usaste la Gema del Espacio para transportarte de vuelta a la Tierra y mientras bailabas al ritmo de tu playlist de Wham! con tus audífonos puestos compraste una chimichanga en uno de tus restaurantes de confianza.

No hay nada como el hogar. En especial después de haber asesinado a tantas personas.''',
        'children': [64]
    },
    64: {
        'type': NodeType.BLANK,
        'content': '''Quizás coleccionar piedritas de colores y matar a tantos héroes no te había curado el corazón, pero definitivamente te había permitido volver a sentirte vivo.

Después de tu aventura ya era hora de descansar, comer y quitarte esa máscara que llevabas puesta todo el día...''',
        'children': [101]
    },
    65: {
        'type': NodeType.DIALOGUE,
        'content': '''"Quién eres?"''',
        'options': ['"Yo"', '"Deadpool"'],
        'children': [66,66],
        'character': 12
    },
    66: {
        'type': NodeType.DIALOGUE,
        'content': '''"Genial! Otro loco que termina varado en Asgard! Ves, hermano?? Por eso digo que deberíamos ser más cuidadosos con el ingreso de extrangeros"''',
        'options': ['"Sigo aquí"', '"No pues perdón?"'],
        'children': [67,67],
        'character': 13
    },
    67: {
        'type': NodeType.FIGHT,
        'content': '''"Qué es lo que quieres?"''',
        'options': ['Una pelea'],
        'children':[68],
        'character': 12,
        'set': 6
    },
    68: {
        'type': NodeType.BLANK,
        'content': '''Loki se acercó a ti dispuesto a asesinarte, pero ya estabas algo cansado así que simplemente usaste de nuevo la Gema del Poder en tu bolsillo y lo mataste rápidamente.''',
        'children': [69]
    },
    69: {
        'type': NodeType.SPECIAL,
        'content': '''Caminaste por Asgard a tu antojo y en el sótano, en la colección de reliquias Asgardianas, te encontraste con una gema roja, así que la llevaste contigo ya que al parecer ahora coleccionabas piedras.

"Hmn, ¿ahora a dónde debería ir?" te preguntabas. "Que sea un lugar divertido y al que no haya ido aún... Ah, ya sé, a Wakanda! Por favor, jugador, por favor, por favor vamos a Wakanda".''',
        'options': ['Está bien','Nop'],
        'children': [70,35],
        'stone': InfinityStones.RED
    },
    35: {
        'type': NodeType.STORY,
        'content': '''"Pero por favoooor. Por favorcito, jugador. Vamos a Wakanda"''',
        'options': ['Agt, está bien', 'Ok, Deadpool!'],
        'children': [70, 70]
    },
    70: {
        'type': NodeType.BLANK,
        'content': '''Te teletransportaste a Wakanda y en un pasillo de la fortaleza real viste a Black Panther pasar, así que te acercaste a saludar.

"Black Panther! No puede ser. Hola! Soy un gran admirador tuyo" dijiste alegre.''',
        'children': [71]
    },
    71: {
        'type': NodeType.DIALOGUE,
        'content': '''"Hola... No sé quién eres ni qué haces aquí pero tengo una reunión muy importante justo ahora"''',
        'options': ['"Entiendo"', '"Ainnn"'],
        'children': [72,72],
        'character': 14
    },
    72: {
        'type': NodeType.DIALOGUE,
        'content': '''"Vamos, hermano. Wanda y Visión ya nos están esperando en el laboratorio"''',
        'options': ['"Los sigo"', '"Entonces vamos"'],
        'children': [73,73],
        'character': 15
    },
    73: {
        'type': NodeType.BLANK,
        'content': '''Aunque no sabían quién eras todos en Wakanda eran tan amables que mientras caminaban, Shuri y su hermano te explicaron lo que estaban tramando: querían quitarle a Visión la Gema de la Mente de una forma segura, sin que eso implique matarlo.''',
        'children': [74]
    },
    74: {
        'type': NodeType.DIALOGUE,
        'content': '''"Me alegra que llegaran! Shuri, nos han dicho que si existe una persona que pueda separar a Visión de la Gema de la Mente eres tú. Ah, hola T'Challa, no te habíá visto y hola... no sé quién eres, tú, el de rojo"''',
        'options': ['"Pool, Dead-pool"', '"No soy nadie"'],
        'children': [75,75],
        'character': 16
    },
    75: {
        'type': NodeType.DIALOGUE,
        'content': '''"Como sea. Shuri, te estaba diciendo... Necesitamos que hagas esto, por favor. Thanos está buscando la Gema y sabemos que va a asesinar a Visión de ser necesario".''',
        'options': ['"Thanos? JAJAJA"', '"No se preocupen"'],
        'children': [76,77],
        'character': 16
    },
    76: {
        'type': NodeType.BLANK,
        'content': '''"Thanos? JAJAJA" interrumpiste con una carcajada. "No tienen nada de qué preocuparse. Thanos ya no es un peligro para ustedes".''',
        'children': [79]
    },
    77: {
        'type': NodeType.BLANK,
        'content': '''"No se preocupen" interrumpiste. "Thanos ya no es un peligro para ustedes".''',
        'children': [79]
    },
    79: {
        'type': NodeType.DIALOGUE,
        'content': '''"Y cómo lo sabes?"''',
        'options': ['Decir la verdad', '"Lo presiento"'],
        'children': [80,81],
        'character': 17
    },
    80: {
        'type': NodeType.BLANK,
        'content': '''"Porque yo mismo lo maté" explicaste.

Todos soltaron una fuerte carcajada, así que fingiste reír con ellos.''',
        'children': [82]
    },
    81: {
        'type': NodeType.BLANK,
        'content': '''"No lo sé pero... Lo presiento." disimulaste. "Presiento que ya no quiere ir a buscar la Gema de la Mente"''',
        'children': [83]
    },
    82: {
        'type': NodeType.DIALOGUE,
        'content': '''"Sí, claro" Shuri rio una vez más antes de seguir hablando y luego volvió a la conversación seria que estaban teniendo antes del aporte de Deadpool. "Wanda, Visión... Creo que puedo hacerlo. Pero no sé cuánto tiempo tarde."''',
        'options': ['"Sí, ignórenme..."', '"Por qué no me oyen?"'],
        'children': [84,84],
        'character': 15
    },
    83: {
        'type': NodeType.DIALOGUE,
        'content': '''"Si presientes eso es porque no conoces a Thanos" señaló Shuri con dureza, para luego volver a la conversación seria que estaban teniendo antes del aporte de Deadpool. "Wanda, Visión... Creo que puedo hacerlo. Pero no sé cuánto tiempo tarde."''',
        'options': ['"Sí, ignórenme..."', '"Por qué no me oyen?"'],
        'children': [84,84],
        'character': 15
    },
    84: {
        'type': NodeType.DIALOGUE,
        'content': '''"Gracias, Shuri. Significa mucho para nosotros"''',
        'options': ['"Estoy pintado en la pared"', '"Siguen ignorándome..."'],
        'children': [85,85],
        'character': 16
    },
    85: {
        'type': NodeType.FIGHT,
        'content': '''"Bien. Entonces comencemos con el procedimiento" dijo acomodando una especie de camilla. "Sigue, Visión, puedes sentarte por aquí".''',
        'options': ['"Nop, se cancela"'],
        'children':[86],
        'character': 14,
        'set': 7
    },
    86: {
        'type': NodeType.SPECIAL,
        'content': '''Por desgracia no supiste la respuesta a esa pregunta porque mataste a Visión con una segunda explosión morada en el laboratorio al haber olvidado que aún sostenías la Gema del Poder en tu mano.

"Ups. Perdona, laboratorio, no quería herirte a ti" avanzaste entre los escombros hasta el cadáver de Visión y luego arrancaste la Gema de la Mente de su Frente para guardarla en tu bolsillo junto a las demás.''',
        'options': ['Celebrar','Probar su poder'],
        'children': [87,88],
        'stone': InfinityStones.YELLOW
    },
    87: {
        'type': NodeType.BLANK,
        'content': '''Decidiste celebrar tu adquisisión con una buena comida, así que volviste a la tierra y mientras bailabas al ritmo de tu playlist de Wham! con tus audífonos puestos compraste una chimichanga en uno de tus restaurantes de confianza.

No hay nada como el hogar. En especial después de haber asesinado a tantas personas.''',
        'children': [64]
    },
    88: {
        'type': NodeType.BLANK,
        'content': '''Querías probar los poderes de la Gema de la Mente, así que te divertiste un buen rato controlando las mentes de los habitantes de Wakanda y haciéndolos hacer cosas absurdas, como bailar la macarena con los pies o ver las películas estúpidas de Wolverine.''',
        'children': [89]
    },
    89: {
        'type': NodeType.BLANK,
        'content': '''Cuando te cansaste de todo eso decidiste que querías disfrutar de uno de los más básicos y hermosos placeres terrenales: una buena comida.

Así que volviste a la tierra y mientras bailabas al ritmo de tu playlist de Wham! con tus audífonos puestos compraste una chimichanga en uno de tus restaurantes de confianza.''',
        'children': [90]
    },
    90: {
        'type': NodeType.BLANK,
        'content': '''No hay nada como el hogar. En especial después de haber asesinado a tantas personas.

Quizás coleccionar piedritas de colores y matar a tantos héroes no te había curado el corazón, pero definitivamente te había permitido volver a sentirte vivo.''',
        'children': [91]
    },
    91: {
        'type': NodeType.BLANK,
        'content': '''Después de tu aventura ya era hora de descansar, comer y quitarte esa máscara que llevabas puesta todo el día...''',
        'children': [101]
    },
    101: {
        'type': NodeType.UNDEFINED,
        'content': "",
        'options': [],
        'children': []
    },
}

