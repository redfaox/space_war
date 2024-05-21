import pygame


class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 170
        self.rect.y = 500