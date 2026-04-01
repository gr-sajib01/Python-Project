import pygame
import settings

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(
            settings.WIDTH//2,
            settings.HEIGHT//2,
            settings.BALL_SIZE,
            settings.BALL_SIZE
        )

        self.dx = settings.BALL_SPEED
        self.dy = -settings.BALL_SPEED

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left <= 0 or self.rect.right >= settings.WIDTH:
            self.dx *= -1

        if self.rect.top <= 0:
            self.dy *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), self.rect)
