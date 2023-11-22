from modelView.Types import Option
from modelView.Deadpool import Deadpool
import time

class GUI:
    def __init__(self):
        self.deadpool_instance = None
        self.text = "Displaying graphical interface..."
        self.deadBookLocations = []
        self.deadBookLinks = []

    def start(self, deadpool_instance):
        self.deadpool_instance = deadpool_instance
        print(self.text)
        print("Waiting for deadpool...")
        time.sleep(1.5)
        deadpool_instance.start()

    def displayStory(self, node):
        print(node.getContent())
        self.displayOptions(node.getOptions())

    def displayDialogue(self, node):
        print(f'Character: {node.getCharacterName()}')
        print(node.getContent())
        self.displayOptions(node.getOptions())

    def displayFight(self, node):
        print("FIGHT")
        print(f'Character: {node.getCharacterName()}')
        print(node.getContent())
        self.displayOptions(node.getOptions())

    def displayNewStone(self, stoneRoute):
        pass

    def updateDeadbookLinks(self, deadbookLinks):
        pass

    def removeMask(self):
        pass

    def displayOptions(self, options):
        print("Select your option:")
        for i in range(0, len(options)):
            print(f'{i + 1}. {options[i]}')
        optionSelected = input(": ")

        while not optionSelected.isdigit() or 0 > int(optionSelected) - 1 or len(options) <= int(optionSelected) - 1:
            print("Invalid input, try again")
            optionSelected = input(": ")

        optionSelected = int(optionSelected)

        if optionSelected == 1:
            self.deadpool_instance.choose(Option.LEFT)
            # print(f'Option selected: {Option.LEFT}')
        elif optionSelected == 2:
            self.deadpool_instance.choose(Option.RIGHT)
            # print(f'Option selected: {Option.RIGHT}')

    # def Buttons events

