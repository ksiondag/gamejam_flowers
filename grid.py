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

class Square( pygame.Rect ):

    def __init__( self, left, top, width, height ):
        pygame.Rect.__init__(self, left, top, width, height)
        self.color = WHITE
        self.growth = 0
        self.hit = 0

    def change_color( self ):
        if self.color == GREEN:
            self.color = WHITE
        elif self.color == WHITE:
            self.color = GREEN
    
    def draw_number( self, screen ):
        # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        myfont = pygame.font.SysFont("monospace", 20)

        # render text
        label = myfont.render("%i" % self.growth, 1, BLACK)
        screen.blit(label, (self))
    
def pixels( count, length, distance ):
    return length*count + distance*(count+1)

def init_grid( rows, columns, height, width, margin ):
    grid = []

    # Draw grid
    x = margin
    y = margin
    for row in range(rows):
        grid.append( [] )
        for column in range(columns):
            grid[row].append( Square( x, y, width, height ) )
            x += width + margin
        y += height + margin
        x = margin

    return grid

def collision( grid, pos ):
    
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            rect = grid[row][column]
            if rect.collidepoint( pos ):
                return row, column
    
    return None

def turn_end(grid):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            damage(grid)
            grid[row][column].hit = 0
            
            #BUG currently acts as though color is default color for all
            if grid[row][column].color != WHITE:
                grid[row][column].growth += 1

def damage(grid):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            grid[row][column].growth -= grid[row][column].hit

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

    grid = init_grid(ROWS, COLUMNS, HEIGHT, WIDTH, MARGIN)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                result = collision( grid, event.pos )
                if result is not None:
                    row, column = result
                    grid[row][column].change_color()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    turn_end(grid)

        # Reinitialize screen 
        #screen.blit(background, (0,0))
        screen.fill(BLACK)

        for row in range(ROWS):
            for column in range(COLUMNS):
                pygame.draw.rect( screen, grid[row][column].color, grid[row][column] )
                grid[row][column].draw_number( screen )

        pygame.display.flip()

if __name__ == '__main__':
    main()
    pygame.quit()

