import pygame, random

class Fruit():
    spacing = 3
    def __init__(self, fruitSize: int = None, color: tuple = None, unitSize: int = None) -> None:

        if fruitSize:
            self.fruitSize = fruitSize
        else:
            self.fruitSize = unitSize-2*self.spacing

        if color:
            self.color = color
        else:
            self.color = (255, 102, 102)

        if not unitSize: unitSize = 20

        self.size = (self.fruitSize, self.fruitSize)
        self.body = pygame.Rect((0, 0), self.size)

    def render(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.body)

    def shuffle(self, xLimit: int, yLimit: int):
        step = self.fruitSize+2*self.spacing
        newPosition = (
            random.randrange(0, xLimit, step)+self.spacing,
            random.randrange(0, yLimit, step)+self.spacing,
        )
        self.body.topleft = newPosition
