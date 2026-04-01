import pygame
import settings
from ball import Ball
from paddle import Paddle
from brick import Brick

pygame.init()

screen = pygame.display.set_mode((settings.WIDTH,settings.HEIGHT))
pygame.display.set_caption("Brick Breaker")

clock = pygame.time.Clock()

paddle=Paddle()
ball=Ball()

bricks=[]
for row in range(settings.BRICK_ROWS):
    for col in range(settings.BRICK_COLS):
        b=Brick(
            col * settings.BRICK_WIDTH,
            row * settings.BRICK_HEIGHT
            )
        bricks.append(b)
        
score = 0
game_over = False
font = pygame.font.SysFont(None, 40)
        
running = True
while running:
        clock.tick(60)
        screen.fill((0, 0, 0))
            
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                    
        keys=pygame.key.get_pressed()
        
        if not game_over:
            paddle.move(keys)
            ball.move()
                
        if ball.rect.colliderect(paddle.rect):
            ball.dy *=-1
                    
        for brick in bricks:
            if brick.alive and ball.rect.colliderect(brick.rect):
                brick.alive=False
                ball.dy*=-1
                score +=10
        if ball.rect.bottom>=settings.HEIGHT:
            game_over=True
                                
        paddle.draw(screen)
        ball.draw(screen)
        
        for brick in bricks:                        
            brick.draw(screen)
            
        score_Text=font.render(f"Score:{score}" ,True, (255,255,255))
        screen.blit(score_Text, (10,10))
        
        if game_over:
            text=font.render("Game Over!!",True,(255,255,255))
            screen.blit(text, (settings.WIDTH//2 - 120, settings.HEIGHT//2))
                                
        pygame.display.flip()
                                
pygame.quit()