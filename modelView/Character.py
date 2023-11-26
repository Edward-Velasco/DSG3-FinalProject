class Character:
    def __init__(self, name, figthContent, fightButtonText, picRoute, miniatureRoute, minDeadRoute):
        self.name = name
        self.figthContent = figthContent
        self.fightButtonText = fightButtonText
        self.picRoute = picRoute
        self.miniatureRoute = miniatureRoute
        self.minDeadRoute = minDeadRoute
        self.state = True

    def getName(self):
        return self.name 

    def getFightContent(self):
        return self.figthContent
    
    def getFightButtonText(self):
        return self.fightButtonText
    
    def getPictureRoute(self):
        return self.picRoute
    
    def getMiniatureRoute(self):
        return self.miniatureRoute
    
    def getMiniatureDeadRoute(self):
        return self.minDeadRoute
    
    def getState(self):
        return self.state

    def setName(self, name):
        self.name = name

    def setFightContent(self, fightContent):
        self.figthContent = fightContent
     
    def setFightButtonText(self, fightButtonText):
        self.fightButtonText = fightButtonText
    
    def setPictureRoute(self, pictureRoute):
        self.picRoute = pictureRoute
    
    def setMiniatureRoute(self, miniatureRoute):
        self.miniatureRoute = miniatureRoute
    
    def setMiniatureDeadRoute(self, miniatureDeadRoute):
        self.minDeadRoute = miniatureDeadRoute
    
    def setState(self, state):
        self.state = state
    
    def murder(self):
        self.setState(False)  
    
    
    
