"""
from modelView.GUI import GUI
from modelView.Deadpool import Deadpool

# disjointSets.build()
gui = GUI()
deadpool = Deadpool(gui)
gui.start(deadpool)"""

from view.main import GameInterface
from model.StoryTree import StoryTree

GameScreen = GameInterface()
#GameScreen.start_gui()

GameScreen.display_story_node(StoryTree[1])
