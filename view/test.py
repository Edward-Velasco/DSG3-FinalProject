from modelView.nodes.NodeSimple import NodeSimple, NodeType
from modelView.nodes.NodeCharacter import NodeCharacter

Root_test_tree = NodeSimple()

Root_test_tree.setType(NodeType.STORY)
Root_test_tree.setContent("Welcome to this new world")
Root_test_tree.setOptions(["Suicide", "Give up"])
# Root_test_tree.setChildren()

Dialogue_test_node = NodeCharacter()

Dialogue_test_node.setType(NodeType.DIALOGUE)
Dialogue_test_node.setContent("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
Dialogue_test_node.setOptions(["Traques", "Billullo 🤑"])
Dialogue_test_node.setCharacterPictureRoute("view/assets/characters/ironman.png")
Dialogue_test_node.setCharacterName("Iron Man")

Fight_test_node = NodeCharacter()

Fight_test_node.setType(NodeType.FIGHT)
Fight_test_node.setContent("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
Fight_test_node.setOptions(["Saltar por la ventana"])
Fight_test_node.setCharacterPictureRoute("view/assets/characters/ironman.png")
Fight_test_node.setCharacterName("Iron Man")