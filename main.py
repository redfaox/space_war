import pygame

pygame.init()

pygame.display.set_caption("Space_War")
screen = pygame.display.set_mode((400, 600))

background = pygame.image.load("img/fond.jpeg")

running = True

while running:
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()