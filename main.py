from modelView.GUI import GUI
from modelView.Deadpool import Deadpool

# disjointSets.build()
gui = GUI()
deadpool = Deadpool(gui)
gui.start(deadpool)

from view.main import GameInterface
from view.test import Root_test_tree, Dialogue_test_node, Fight_test_node

GameScreen = GameInterface(deadpool)
GameScreen.start_gui()
#GameScreen.display_story_node(Root_test_tree)
#GameScreen.display_character_node(Fight_test_node)
