import pygame
from snake import Snake
from fruit import Fruit
from game import Game

# This class should handle all collision conditions and "emit" events based on game settings,
# I was planning to make different game modes including different behaviours on collision events
class CollisionManager():
    def __init__(self, game: Game, snake: Snake, fruit: Fruit) -> None:
        self.snake = snake
        self.fruit = fruit
        self.maxWidth = Game.width
        self.maxHeight = Game.height
        self.borders = [
            pygame.Rect((-1, 0), (1, self.maxHeight)),
            pygame.Rect((self.maxWidth, 0), (1, self.maxHeight)),
            pygame.Rect((0, -1), (self.maxWidth, 1)),
            pygame.Rect((0, self.maxHeight), (self.maxWidth, 1))
        ]
    
    def fruitCollision(self):
        if self.snake.head.colliderect(self.fruit.body):
                self.fruit.shuffle(self.maxWidth, self.maxHeight)
                self.snake.addBodypart(self.fruit.score)