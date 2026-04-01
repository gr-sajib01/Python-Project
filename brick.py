import pygame
import settings

class Brick:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x, y, settings.BRICK_WIDTH, settings.BRICK_HEIGHT)
        self.alive = True

    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen, (200,50,50), self.rect)