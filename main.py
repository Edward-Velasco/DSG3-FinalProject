from modelView.Deadpool import Deadpool
from view.main import start_gui

disjointSets.build()
deadpool = Deadpool()
# La interfaz llama a deadpool.start()
deadpool.start()

GUI = GUI()
GUI.start()
deadpool.start()

start_gui()
