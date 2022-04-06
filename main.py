import pygame, sys

from random import randint

from player import Player
from enemy import Enemy

from colors import *

pygame.init()

surface = pygame.display.set_mode((500, 500))
pygame.display.set_caption('CódigoFacilito')

clock = pygame.time.Clock()

enemies = pygame.sprite.Group()
player = Player(250, 250)

game = True
contador = 0


while True:
    clock.tick(60)
    
    if len(enemies) == 0:
        for _ in range(0, 20):
            enemy = Enemy( randint(0, 500),  randint(-3000, -100) )
            enemies.add(enemy)

    
    key_pressed = pygame.key.get_pressed()
    
    if key_pressed[pygame.K_LEFT]:
        player.left()

    
    if key_pressed[pygame.K_RIGHT]:
        player.right()


    if key_pressed[pygame.K_UP]:
        player.up()

    
    if key_pressed[pygame.K_DOWN]:
        player.downd()
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    for enemy in enemies:
        if enemy.rect.y > 600:
            enemies.remove(enemy)
            contador += 1
            print(contador)
    
    
    if pygame.sprite.spritecollideany(player, enemies):
        game = False
    
    
    if game:
        surface.fill(WHITE)
        player.draw(surface)
    
        enemies.update()
        enemies.draw(surface)
    
    pygame.display.update()
