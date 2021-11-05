import pygame
from fruit import Fruit
from snake import Snake
from controls import Controller

class Game():
    def __init__(self, width: int = 720, height: int = 480, initialPosition: tuple = None, FPS: float = 12) -> None:

        pygame.init()
        self.clock = pygame.time.Clock()
        self.setupScreen(width, height)

        snake = Snake(initialPosition = self.unitCenter, unitSize = self.unitSize)
        
        fruit = Fruit(unitSize = self.unitSize)
        fruit.shuffle(width, height)

        while 1:
            eventList = pygame.event.get()
            Controller(snake, eventList)               

            snake.move()

            if snake.head.colliderect(fruit.body):
                fruit.shuffle(width, height)
                snake.addBodypart()

            self.screen.fill((0, 0, 0))
            snake.render(self.screen)
            fruit.render(self.screen)
    
            pygame.display.flip()
            self.clock.tick(FPS)

    def setupScreen(self, width: int, height: int, unitSize: int = None) -> None:
        if not unitSize: self.unitSize = 20

        self.width, self.height = width, height
        
        self.width = self.width - self.width%self.unitSize
        self.height = self.height - self.height%self.unitSize

        self.size = (self.width, self.height)

        self.screen = pygame.display.set_mode(self.size)
        
        self.unitCenter = (self.width/2 - (self.width/2)%self.unitSize , self.height/2 - (self.height/2)%self.unitSize)