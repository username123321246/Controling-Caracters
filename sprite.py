import pygame
from pygame.locals import *
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
p_x =400
p_y = 300

image = pygame.image.load("dog.png")
size = pygame.transform.scale(image, (100, 70))

keys = [False, False, False, False]

while True:
    screen.fill((255,255,255))
    screen.blit(size, (p_x, p_y))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:     
                keys[0] = True
            
            if event.key == K_DOWN:
                 keys[1] = True

            if event.key == K_LEFT:
                keys[2] = True

            if event.key == K_RIGHT:
                keys[3] = True

        if event.type == pygame.KEYUP:

            if event.key == K_UP:     
                keys[0] = False
            
            if event.key == K_DOWN:
                 keys[1] = False

            if event.key == K_LEFT:
                keys[2] = False

            if event.key == K_RIGHT:
                keys[3] = False


    if keys[0]:
        if p_y >= 0:
            p_y = p_y - 5
    
    if keys[1]:    
        if p_y <= 600:
            p_y = p_y + 5

    if keys[2]:
        if p_x >= 0:
            p_x = p_x - 5

    if keys[3]:
        if p_x <= 800:
            p_x = p_x - 5   





















