import pygame
from colors import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
    
        self.image = pygame.Surface([20, 20])
        
        self.image.fill( ENEMY )
        self.rect = self.image.get_rect()
        
        self.rect.x = pos_x
        self.rect.y = pos_y


    def update(self):
        self.rect.y += 5
        