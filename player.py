import pygame
from colors import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
    
        self.image = pygame.Surface([40, 40])
        
        self.image.fill( PLAYER )
        self.rect = self.image.get_rect()
        
        self.rect.x = pos_x
        self.rect.y = pos_y
    
    
    def left(self):
        self.rect.x -= 5


    def right(self):
        self.rect.x += 5
    
    
    def up(self):
        self.rect.y -= 5


    def downd(self):
        self.rect.y += 5    

    def update(self):
        print(self.rect.x)
    
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)