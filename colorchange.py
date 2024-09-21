import pygame
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Change Sprites")


WHITE = (255, 255, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (75, 0, 130), (238, 130, 238)]


COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COLOR_CHANGE_EVENT, 2000)  

sprite_size = 50
sprite1_pos = [100, 100]
sprite2_pos = [300, 100]


sprite1_color = random.choice(colors)
sprite2_color = random.choice(colors)


running = True
while running:
    screen.fill(WHITE)

    
    pygame.draw.rect(screen, sprite1_color, (sprite1_pos[0], sprite1_pos[1], sprite_size, sprite_size))
    pygame.draw.rect(screen, sprite2_color, (sprite2_pos[0], sprite2_pos[1], sprite_size, sprite_size))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == COLOR_CHANGE_EVENT:
            
            sprite1_color = random.choice(colors)
            sprite2_color = random.choice(colors)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
