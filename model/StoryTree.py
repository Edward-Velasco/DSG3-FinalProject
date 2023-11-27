# Ejemplo de estructura de árbol

from modelView.Types import NodeType, InfinityStones

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
        'character': 0,
        'set': 0
    },
    3: {
        'type': NodeType.DIALOGUE,
        'content': "Alright, you are getting therapy",
        'options': ["Try again", "Fuck it"],
        'children': [4,5],
        'character': 0
    },
    4: {
        'type': NodeType.SPECIAL,
        'content': "Has recibido la gema verde.",
        'options': ["Decir gracias","Irte"],
        'children': [5,5],
        'stone': InfinityStones.GREEN
    },

    # Used to tell the program the story is over
    5: {
        'type': NodeType.UNDEFINED,
        'content': "",
        'options': [],
        'children': []
    },

    # Independant nodes (defeat nodes)
    101: {
        'type': NodeType.BLANK,
        'content': "Ironman made a hole in your liver, you are imposibilited to fight",
        'options': [],
        'children': [5]
    }
}

