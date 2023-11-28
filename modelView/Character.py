class Character:
    def __init__(self, name, picRoute, miniatureRoute, minDeadRoute, graphic_coordinates, figthContent):
        self.name = name
        self.picRoute = picRoute
        self.miniatureRoute = miniatureRoute
        self.minDeadRoute = minDeadRoute
        self.coords = graphic_coordinates
        self.figthContent = figthContent
        self.state = True

    def getName(self):
        return self.name

    def getPictureRoute(self):
        return self.picRoute

    def getMiniatureRoute(self):
        return self.miniatureRoute

    def getMiniatureDeadRoute(self):
        return self.minDeadRoute

    def getFightContent(self):
        return self.figthContent

    def getState(self):
        return self.state

    def setName(self, name):
        self.name = name

    def setPictureRoute(self, pictureRoute):
        self.picRoute = pictureRoute

    def setMiniatureRoute(self, miniatureRoute):
        self.miniatureRoute = miniatureRoute

    def setMiniatureDeadRoute(self, miniatureDeadRoute):
        self.minDeadRoute = miniatureDeadRoute

    def setFightContent(self, fightContent):
        self.figthContent = fightContent

    def setState(self, state):
        self.state = state

    def murder(self):
        self.setState(False)

