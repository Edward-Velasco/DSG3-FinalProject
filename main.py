# from view.main import start_gui
from modelView.GUI import GUI
from modelView.Deadpool import Deadpool

# disjointSets.build()
gui = GUI()
deadpool = Deadpool(gui)
gui.start(deadpool)

