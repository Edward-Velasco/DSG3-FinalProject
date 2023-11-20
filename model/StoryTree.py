# Ejemplo de estructura de árbol

from modelView.Types import NodeType

StoryTreeCorrect = {
    0x001: {
        'type': NodeType.STORY,
        'content': "Hello world!",
        'options': ["Hello there", "General Kenobi"],
        'children': [0x002, 0x003]
    },
    0x002: {
        'type': NodeType.CONVERSATION,
        'image': "route/Image",
        'content': "Idk",
        'options': ["A", "B"],
        'children': [0x004, 0x005]
    },
    0x003: {
        'type': NodeType.FIGHT,
        'content': ""
    }
}




StoryTree = {
    0x001: {
        'type': NodeType.STORY,
        'content': "Hello world!",
        'children': [0x002]
    },
    0x002: {
        'type': NodeType.STORY,
        'content': "Story starts",
        'children': [0x003]
    },
    0x003: {
        'type': NodeType.CONVERSATION,
        'content': "There you are!",
        'options': ["Smile", "Run away"],
        'children': [0x004, 0x005]
    },
    0x004: {
        'type': NodeType.STORY,
        'content': "You go to a bar, talking goes wrong and you go outside",
        'children': [0x005]
    },
    0x005: {
        'type': NodeType.FIGHT,
        'oponent': 0x100,
        'content': ["You get charged", "0x101 Jumps to attack you", "0x101 Plans to attack you from the back"],
        'options': [['Sword', 'Gun'], ['Gun'], ['Sword', 'Gun']],
        'children': [0x006, 0x007]
    },
    0x006: {
        'type': NodeType.STORY,
        'content': "They dodged, you lost your head",
        'children': [0x008]
    },
    0x007: {
        'type': NodeType.STORY,
        'content': "Woah you murdered them, bad luck for them",
        'children': [0x008]
    },
    0x008: {
        'type': NodeType.UNDEFINED,
        'content': "Game development in progres.."
    }
}

