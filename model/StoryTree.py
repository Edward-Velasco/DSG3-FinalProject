# Ejemplo de estructura de árbol

from modelView.Types import NodeType, InfinityStones

StoryTree = {
    1: {
        'type': NodeType.BLANK,
        'content': '''"Ah... ¿o sea que tu eres el idiota que va a estar jugando mi videojuego? Esperaba a alguien más guapo, pero como sea, supongo que este videojuego tuvo tanto éxito que llegó a las manos de cualquiera.

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
        'content': '''"Entonces, ¿qué dices? ¿Listo para patear los supertraseros de algunos superidiotas?

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
    5: {
        'type': NodeType.FIGHT,
        'content': '"¿¿Pero cuál es tu puto problema, anciano??"',
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
        'content': '"Pero que malos modales, chico. ¿No querías una reunión para charlar? Baja el arma y hablémoslo"',
        'options': ['"Habla con la mano"', '"Eso no pasará"'],
        'children': [13,13],
        'characterName': "Iron Man",
        'characterPictureRoute': "view/assets/characters/ironman.png"
    },
    13: {
        'type': NodeType.FIGHT,
        'content': '"¿Qué es lo que quieres, Deadpool?"',
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
        'options': ['el Sanctum Sanctorum','Wakanda'],
        'children': [17,18],
        'stone': InfinityStones.GREEN
    },
    17: {
        'type': NodeType.BLANK,
        'content': '''Te teletransportas a el Sanctum Sanctorum.''',
        'children': [19]
    },
    18: {
        'type': NodeType.BLANK,
        'content': '''Te teletransportas a Wakanda.''',
        'children': [19]
    },
    19: {
        'type': NodeType.UNDEFINED,
        'content': "",
        'options': [],
        'children': []
    },
}

