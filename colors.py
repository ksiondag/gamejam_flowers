'''Define color constants.'''
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREY  = (159,182,205)

BLUE  = (  0,  0,255)
GREEN = (  0,255,  0)
RED   = (255,  0,  0)

import pygame


FLOWER = pygame.image.load('sprite/flower1.png')
RABBIT = pygame.image.load('sprite/rabbit.png')
THORN = pygame.image.load('sprite/thorn_up.png')
POISON = pygame.image.load('sprite/poison.png')

FLOWER_RECT = FLOWER.get_rect()
RABBIT_RECT = RABBIT.get_rect()
THORN_RECT = THORN.get_rect()
POISON_RECT = POISON.get_rect()

FLOWER = pygame.transform.scale(FLOWER,(50,50))
RABBIT = pygame.transform.scale(RABBIT,(50,50))
THORN = pygame.transform.scale(THORN,(50,50))
POISON = pygame.transform.scale(POISON,(50,50))

