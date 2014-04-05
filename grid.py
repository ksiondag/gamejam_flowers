#!/usr/bin/python

import pygame

import collections
import sys

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

class Terrain( pygame.Rect ):

    grid = None
    active = None

    def __init__( self, left, top, width, height, row, col ):
        pygame.Rect.__init__(self, left, top, width, height)
        self.pos = (row, col)
        self.color = WHITE
        self.growth = 0

        self.row = row
        self.col = col

        # NOTE: currently placeholders
        self.seed = False
        self.hit = 0

    def change_color( self ):
        if self.color == GREEN:
            self.color = WHITE
        elif self.color == WHITE:
            self.color = GREEN

    def is_plant( self ):
        return self.color == GREEN
    
    def up_terrain( self, grid ):
        row = self.row - 1
        col = self.col
        if row < 0:
            return self
        else:
            return grid[row][col]

    def down_terrain( self, grid ):
        row = self.row + 1
        col = self.col
        if row >= len(grid):
            return self
        else:
            return grid[row][col]

    def left_terrain( self, grid ):
        row = self.row
        col = self.col - 1
        if col < 0:
            return self
        else:
            return grid[row][col]

    def right_terrain( self, grid ):
        row = self.row
        col = self.col + 1
        if col >= len(grid[row]):
            return self
        else:
            return grid[row][col]

    def set_active( self ):
        Terrain.active = self

    def draw( self, screen ):
        pygame.draw.rect( screen, self.color, self )
        self.draw_number( screen )

        if self is Terrain.active:
            active_border(screen, self)
    
    def draw_number( self, screen ):
        myfont = pygame.font.SysFont("monospace", 20)

        # render text
        label = myfont.render("%i" % self.growth, 1, BLACK)
        screen.blit(label, (self))

def pixels( count, length, distance ):
    return length*count + distance*(count+1)

def collision( grid, pos ):
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            rect = grid[row][col]
            if rect.collidepoint( pos ):
                return row, col
    
    return None

def turn_end(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            damage(grid)
            grid[row][col].hit = 0
            
            if grid[row][col].color != WHITE:
                grid[row][col].growth += 1

def damage(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            grid[row][col].growth -= grid[row][col].hit

def active_border( screen, square ):
    pygame.draw.rect( screen, RED, (square.left-MARGIN, square.top, MARGIN, HEIGHT) )
    pygame.draw.rect( screen, RED, (square.left, square.top-MARGIN, WIDTH,  MARGIN) )
    pygame.draw.rect( screen, RED, (square.right, square.top, MARGIN, HEIGHT) )
    pygame.draw.rect( screen, RED, (square.left, square.bottom, WIDTH, MARGIN) )

def do_nothing( grid, event ):
    return

def quit( grid, event ):
    pygame.quit()
    sys.exit()

def mouse_button_down( grid, event ):
    result = collision( grid, event.pos )
    if result is not None:
        row, col = result
        grid[row][col].change_color()

def key_down( grid, event ):
    # TODO: some stuff
    movement = {
        pygame.K_UP:    Terrain.active.up_terrain(grid),
        pygame.K_DOWN:  Terrain.active.down_terrain(grid),
        pygame.K_LEFT:  Terrain.active.left_terrain(grid),
        pygame.K_RIGHT: Terrain.active.right_terrain(grid)
    }
    if event.key in movement:
        movement[ event.key ].set_active()

    elif event.key == pygame.K_q:
        Terrain.active.seed = True

    elif event.key == pygame.K_RETURN:
        turn_end(grid)

def init_grid( n_rows, n_cols, height, width, margin ):
    grid = []

    # Grid spacing
    x = margin
    y = margin
    for row_index in range(n_rows):
        row = []
        for col_index in range(n_cols):
            row.append(Terrain(x, y, width, height, row_index, col_index))
            x += width + margin
        y += height + margin
        x = margin

        grid.append( row )

    return grid
    
def main():
    # Initialize screen
    size = (pixels(ROWS, HEIGHT, MARGIN), pixels(COLUMNS, WIDTH, MARGIN))
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # Initialize clock
    clock = pygame.time.Clock()

    # Initialize background
    screen.fill(BLACK)
    pygame.display.flip()

    grid = init_grid(ROWS, COLUMNS, HEIGHT, WIDTH, MARGIN)
    grid[0][0].set_active()

    # Event managing dictionary
    # For events we do not process, we are defaulting to doing nothing
    process = collections.defaultdict( lambda: do_nothing )
    process.update( [
        (pygame.QUIT, quit),
        (pygame.MOUSEBUTTONDOWN, mouse_button_down),
        (pygame.KEYDOWN, key_down)
    ] )

    while True:
        # Handle events and change state as necessary
        for event in pygame.event.get():
            process[event.type]( grid, event )

        # Redraw screen
        screen.fill(BLACK)
        for row in grid:
            for terrain in row:
                terrain.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()

