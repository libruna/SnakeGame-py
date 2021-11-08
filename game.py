import pygame
from fruit import Fruit, GoldenFruit, ToxicFruit
from snake import Snake
from controls import Controller

class Game():
    # Setups the game, creates the screen canvas, instantiating variables like the snake 
    # and the fruits, positions snake and fruits on the canvas and starts the main loop
    # which detects key events, renders the objects of the game and handle frame rate
    def __init__(self, width: int = 720, height: int = 480, initialPosition: tuple = None, FPS: float = 12, unitSize: int = None) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.setupScreen(width, height, unitSize)

        snake = Snake(initialPosition = self.unitCenter, unitSize = self.unitSize)
        
        fruit = Fruit(unitSize = self.unitSize)
        fruit2 = ToxicFruit(unitSize = self.unitSize)
        fruit3 = GoldenFruit(unitSize = self.unitSize)
        fruit.shuffle(width, height)
        fruit2.shuffle(width, height)
        fruit3.shuffle(width, height)
        while 1:
            eventList = pygame.event.get()
            Controller(snake, eventList)               

            snake.move()

            if snake.head.colliderect(fruit.body):
                fruit.shuffle(width, height)
                snake.addBodypart(fruit.score)
            if snake.head.colliderect(fruit2.body):
                fruit2.shuffle(width, height)
                snake.addBodypart(fruit2.score)
            if snake.head.colliderect(fruit3.body):
                fruit3.shuffle(width, height)
                snake.addBodypart(fruit3.score)

            self.screen.fill((0, 0, 0))
            snake.render(self.screen)
            fruit.render(self.screen)
            fruit2.render(self.screen)
            fruit3.render(self.screen)
    
            pygame.display.flip()
            self.clock.tick(FPS)

    # Creates screen for rendering, adequating dimensions to unitSize, which should be
    # the unit vector of the space created, all measures being multiples of unitSize
    def setupScreen(self, width: int, height: int, unitSize: int = None) -> None:
        if not unitSize: self.unitSize = 20

        self.width, self.height = width, height
        
        self.width = self.width - self.width%self.unitSize
        self.height = self.height - self.height%self.unitSize

        self.size = (self.width, self.height)

        self.screen = pygame.display.set_mode(self.size)
        
        self.unitCenter = (self.width/2 - (self.width/2)%self.unitSize , self.height/2 - (self.height/2)%self.unitSize)