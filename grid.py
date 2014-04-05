#!/usr/bin/python

import pygame

TITLE = 'Grid Area!'

# TODO: put this in constants file eventually
# Define colors
BLACK = (  0,  0,  0)
WHITE = (255,255,255)

BLUE  = (  0,  0,255)
GREEN = (  0,255,  0)
RED   = (255,  0,  0)

# Grid constants
WIDTH = 50
HEIGHT = 50
MARGIN = 5

ROWS    = 10
COLUMNS = 10

def pixels( count, length, distance ):
    return length*count + distance*(count+1)

def main():
    # Initialize screen
    size = (pixels(ROWS, HEIGHT, MARGIN), pixels(COLUMNS, WIDTH, MARGIN))
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # Initialize clock
    clock = pygame.time.Clock()

    # Blank screen set to black
    #background = pygame.Surface(screen.get_size())
    #background = background.convert()
    #background.fill(BLACK)

    # Blit everything to the screen
    #screen.blit(background, (0, 0))
    screen.fill(BLACK)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Reinitialize screen 
        #screen.blit(background, (0,0))
        screen.fill(BLACK)

        # Draw grid
        x = MARGIN
        y = MARGIN
        for row in range(ROWS):
            for column in range(COLUMNS):
                pygame.draw.rect( screen, GREEN, (x, y, WIDTH, HEIGHT) )
                x += WIDTH + MARGIN
            y += HEIGHT + MARGIN
            x = MARGIN

        pygame.display.flip()

if __name__ == '__main__':
    main()
