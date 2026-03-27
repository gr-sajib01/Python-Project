import pygame
import settings

class Paddle:
    def_init_(self):
    self.rect=pygame.rect(
      settings.WIDTH/2-settings.PADDLE_WIDTH/2,
      settings.HEIGHT-50,
      settings.PADDLE_WIDTH,
      settings.PADDLE_HEIGHT
    )
    def move(self,keys):
        if keys[pygame.k_left]and self.rect.left>0:
            self.rect.x-=settings.PADDLE_SPEED

        if keys[pygame.k_right]and self.rect.right<settings.WIDTH:
            self.rect.x+=settings.PADDLE_SPEED

        def draw(self,screen):
        pygame.draw.rect(screen,(255,255,255),self.rect)