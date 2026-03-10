import pygame
import Settings

class Ball:
    def__init__(self):
        self.rect=pygame.Rect(
            settings.WIDTH//2,
            settings.HEIGHT//2,
            settings.BALL_SIZE,
            settings.BALL_SIZE
        )