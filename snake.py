import pygame

def death():
    pygame.mixer.init()
    #Check if file exist
    import os.path
    if os.path.isfile("sound/death.wav"):
       pygame.mixer.music.load("sound/death.wav")
       pygame.mixer.music.play()

    #wait some seconds before the end of the game
    pygame.time.wait(3200)
    #Close pygame window
    pygame.quit()
    
    #Start the game again
    from game import Game
    Game(FPS = 15)

    #Quit current session
    quit()

class Snake():
    # Creates snake taking some parameters like position, size, color etc.
    # Note this only instantiates the object in memory, needing to be rendered to see effects
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
    # Draws snake on screen, managing each body part too
        pygame.draw.rect(screen, self.color, self.head)
        
        #If the snake go to out of the screen, game over
        if (self.head[0] < 0 or self.head[0] > 719 or self.head[1] < 0 or self.head[1] > 479) :
            death()
        for bodypart in self.bodyList:
            pygame.draw.rect(screen, self.bodyColor, bodypart)

    def move(self) -> None:
    # Contains the logic that manages snake movement, mainly passing the last item in the body
    # to the next item's position, doing this until it reaches the head which then moves based on
    # the last key pressed (orientation is defined by this event)
        if self.bodyList:
            for i in range(1, len(self.bodyList)):
                self.bodyList[-i].center = self.bodyList[-i-1].center
            self.bodyList[0].center = self.head.center
        self.head.centerx = self.head.centerx + self.orientation[0]*self.headSize
        self.head.centery = self.head.centery + self.orientation[1]*self.headSize
    
    
    def addBodypart(self, quantity: int = 1) -> None:
    # Contains the logic that places each part of the body in a position relative to the last item of the list
    # in the bodyList, including boundary cases, multiple additions and removing items from the list

    # The algorithm works by using the 2 last items in the body to detect if they are alligned, then puts the
    # new body part in the tail respecting the correct position and spacing relative to itself and the reference

        # If the score was negative, decrease the snake's length
        if quantity < 0:
            for i in range(abs(quantity)):
                if self.bodyList:
                   self.bodyList.pop()
                   pygame.mixer.init()
                   #Check if file exist
                   import os.path
                   if os.path.isfile("sound/damage.wav"):
                      pygame.mixer.music.load("sound/damage.wav")
                      pygame.mixer.music.play()
                else:
                    death()
                    
        else:
        # If the score was greater than 1, increase the snake's length accordingly
            pygame.mixer.init()
            #Check if file exist
            import os.path
            if os.path.isfile("sound/eat.wav"):
               pygame.mixer.music.load("sound/eat.wav")
               pygame.mixer.music.play()
            for i in range(quantity):
                newBody = pygame.Rect((0,0), (self.headSize/2, self.headSize/2))
                reference = self.head
                if self.bodyList:
                    if len(self.bodyList) > 1: reference = self.bodyList[-2]
                    
                    # Detects alignment in x and y directions
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
                    ] # first increment is always opposite to movement direction
                self.bodyList.append(newBody)
    
    # Changes the orientation vector of the snake, influencing movement direction
    def changeOrientation(self, orientation: list = None) -> None:
        if orientation:
            # selfOpposite prevents snake of making a 180 turn
            selfOpposite = [ -self.orientation[0], -self.orientation[1] ]
            if orientation != selfOpposite:
                self.orientation = orientation



