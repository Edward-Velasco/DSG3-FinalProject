from view.main import GameInterface
from modelView.DisjointSets import Disjoint_Set as DisjointSets
from modelView.Deadpool import Deadpool

sets = DisjointSets(4)
sets.build()
GameScreen = GameInterface()
deadpool = Deadpool(GameScreen, sets)
GameScreen.set_deadpool(deadpool)
sets.setDeadPool(deadpool)
GameScreen.start_gui()

