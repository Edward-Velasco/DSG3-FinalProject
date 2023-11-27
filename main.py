from view.main import GameInterface
from modelView.DisjointSets import Disjoint_Set as DisjointSets
from modelView.Deadpool import Deadpool

sets = DisjointSets(100)
sets.build()
GameScreen = GameInterface()
deadpool = Deadpool(GameScreen, sets)
GameScreen.set_deadpool(deadpool)
GameScreen.start_gui()
# sets.set_deadpool(deadpool)

