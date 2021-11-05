import pygame
class Snake():
    def __init__(self, color: tuple = None, bodyColor: tuple = None, initialPosition: tuple = None, unitSize: int = None) -> None:
        if color:
            self.color = color
        else:
            self.color = (0, 255, 0) # colors are defined using rgb
        
        if bodyColor:
            self.bodyColor = bodyColor
        else:
            self.bodyColor = (0, 255, 0)   
        
        if initialPosition:
            self.initialPosition = initialPosition
        else:
            self.initialPosition = (0, 0)

        # only indicates which way the snake is going, starts parked in the center
        self.orientation = [0, 0]     

        if not unitSize: unitSize = 20

        self.headSize = unitSize
        self.bodyList = []
        self.head = pygame.Rect(initialPosition, (self.headSize, self.headSize))

    def render(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.color, self.head)
        for bodypart in self.bodyList:
            pygame.draw.rect(screen, self.bodyColor, bodypart)

    def move(self) -> None:
        if self.bodyList:
            for i in range(1, len(self.bodyList)):
                self.bodyList[-i].center = self.bodyList[-i-1].center
            self.bodyList[0].center = self.head.center
        self.head.centerx = self.head.centerx + self.orientation[0]*self.headSize
        self.head.centery = self.head.centery + self.orientation[1]*self.headSize
        
    def addBodypart(self, quantity: int = 1) -> None:
        for i in range(quantity):
            newBody = pygame.Rect((0,0), (self.headSize/2, self.headSize/2))
            reference = self.head
            if self.bodyList:
                if len(self.bodyList) > 1: reference = self.bodyList[-2]
                
                if self.bodyList[-1].centerx - reference.centerx == 0:
                    offset = self.bodyList[-1].centery - reference.centery
                    addDirection = offset/abs(offset)
                    newBody.center = [
                        self.bodyList[-1].centerx, 
                        self.bodyList[-1].centery + addDirection*self.headSize
                    ]
                if self.bodyList[-1].centery - reference.centery == 0:
                    offset = self.bodyList[-1].centerx - reference.centerx
                    addDirection = offset/abs(offset)
                    newBody.center = [
                        self.bodyList[-1].centerx + addDirection*self.headSize, 
                        self.bodyList[-1].centery
                    ]
            else:
                newBody.center = [
                    self.head.centerx - self.orientation[0]*self.headSize,
                    self.head.centery - self.orientation[1]*self.headSize
                ] # first increment depends on direction
            self.bodyList.append(newBody)
    
    def changeOrientation(self, orientation: list = None) -> None:
        if orientation:
            # snake cannot make 180 turn
            selfOpposite = [ -self.orientation[0], -self.orientation[1] ]
            if orientation != selfOpposite:
                self.orientation = orientation



