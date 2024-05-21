import pygame
from player import Player

pygame.init()

pygame.display.set_caption("Space_War")
screen = pygame.display.set_mode((400, 600))

background = pygame.image.load("img/fond.jpeg")
background.convert()

player = Player()

running = True

while running:
    screen.blit(background, (0, 0))
    screen.blit(player.image, player.rect)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()