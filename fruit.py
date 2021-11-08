import pygame, random

# Fruit colors to be used, score depends on color
GOLDEN = (219, 165, 20)
STANDARD = (255, 102, 99)
TOXIC = (177, 219, 48)

class Fruit():
    # Creates the fruit object based on screen unitSize and fruitSize given
    def __init__(self, fruitSize: int = None, color: tuple = None, unitSize: int = None, score: int = 1) -> None:
        if not unitSize: unitSize = 20      
        
        if fruitSize:
            self.spacing = unitSize - fruitSize
            self.fruitSize = fruitSize
        else:
            self.spacing = 3
            self.fruitSize = unitSize-2*self.spacing

        if color:
            self.color = color
        else:
            self.color = STANDARD
        
        if score:
            self.score = score
        else:
            self.score = 1

        self.size = (self.fruitSize, self.fruitSize)
        self.body = pygame.Rect((0, 0), self.size)

    # Draws fruit rectangle into the screen canvas
    def render(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.body)

    # Changes the fruit's position to another random position, respecting screen size and spacing given
    def shuffle(self, xLimit: int, yLimit: int):
        step = self.fruitSize+2*self.spacing
        newPosition = (
            random.randrange(0, xLimit, step)+self.spacing,
            random.randrange(0, yLimit, step)+self.spacing,
        )
        self.body.topleft = newPosition

# Golden fruit should be a special fruit which gives the snake 3 score points instead of 1
class GoldenFruit(Fruit):
    def __init__(self, unitSize: int = None) -> None:
        super().__init__(fruitSize=16, color=GOLDEN, unitSize=unitSize, score=3)

# Toxic fruit should be an special fruit which removes 2 points from the snake, killing it
# if current score - 2 < 0
class ToxicFruit(Fruit):
    def __init__(self, unitSize: int = None) -> None:
        super().__init__(color=TOXIC, unitSize=unitSize, score=-2)