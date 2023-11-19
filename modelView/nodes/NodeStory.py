from Node import Node
from NodeType import NodeType

class NodeStory(Node):
    def __init__(self):
        super().__init__()
        self.type = NodeType.STORY
        self.text = "Deadpool recently lost his wife due to some criminals he had been paid to murder \
                    he commited the mistake of letting one of them live, and even if he already took revenge \
                    that didn't make him feel better, so now he's trying to find a way to die, but how could he \
                    when he's basically inmortal?"
        self.choices = ""
