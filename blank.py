#!/usr/bin/python

import pygame

def main():
    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((250,250))
    pygame.display.set_caption('Blank screen!')

    # Blank screen set to black
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            screen.blit(background, (0,0))
            pygame.display.flip()

if __name__ == '__main__':
    main()
