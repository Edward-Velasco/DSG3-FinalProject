# Ejemplo de estructura de árbol

from modelView.Types import NodeType

StoryTree = {
    1: {
        'type': NodeType.STORY,
        'content': "Welcome to this new world",
        'options': ["Suicide", "Give up"],
        'children': [2, 3]
    },
    2: {
        'type': NodeType.FIGHT,
        'content': "- Face the death\n- Oh no, you are immortal",
        'options': ["ButtonText"],
        'children':[5],
        'characterName': "unknown",
        'characterPictureRoute': "/"
    },
    3: {
        'type': NodeType.DIALOGUE,
        'content': "Alright, you are getting therapy",
        'options': ["Try again", "Fuck it"],
        'children': [4,5],
        'characterName': "Your head",
        'characterPictureRoute': "/"
    },
    4: {
        'type': NodeType.SPECIAL,
        'content': "Has recibido la gema verde.",
        'options': ["Decir gracias","Irte"],
        'children': [5,5],
        'stone': InfinityStones.GREEN
    },
    5: {
        'type': NodeType.UNDEFINED,
        'content': "",
        'options': [],
        'children': []
    }
}

