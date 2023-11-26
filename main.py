from modelView.Deadpool import Deadpool
# from modelView.DisjointSets import DisjointSets
from view.main import GameInterface
from view.test import Root_test_tree, Dialogue_test_node, Fight_test_node

sets = DisjointSets()
sets.build()

GameScreen = GameInterface()
deadpool = Deadpool(GameScreen, sets)
GameScreen.start_gui(deadpool)
#GameScreen.display_story_node(Root_test_tree)
#GameScreen.display_character_node(Fight_test_node)
