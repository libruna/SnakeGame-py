import pygame, snake, sys
from orientation import LEFT, RIGHT, UP, DOWN

class Controller():
    def __init__(self, snake: snake.Snake, eventList: list) -> None:
        for event in eventList:
            if event.type == pygame.QUIT: sys.exit()
        
            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_UP:
                    snake.changeOrientation(UP)
                if event.key == pygame.K_DOWN:
                    snake.changeOrientation(DOWN)
                if event.key == pygame.K_LEFT:
                    snake.changeOrientation(LEFT)
                if event.key == pygame.K_RIGHT:
                    snake.changeOrientation(RIGHT)
        