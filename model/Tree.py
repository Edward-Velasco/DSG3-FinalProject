from ..modelView.enum.Types import NodeType

Tree = {
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
        'content': "You go to a bar",
        'children': [0x006]
    },
    0x005: {
        'type': NodeType.FIGHT,
        'content': ""
    }
}
