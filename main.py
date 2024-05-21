import pygame

pygame.init()

pygame.display.set_caption("Space_War")
screen = pygame.display.set_mode((400, 600))

background = pygame.image.load("img/fond.jpeg")
background.convert()

running = True

while running:
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()