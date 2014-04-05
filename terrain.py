
import pygame

import colors

# Terrain constants
WIDTH  = 50
HEIGHT = 50
MARGIN = 5

N_ROWS = 10
N_COLS = 10

def _pixels( count, length, distance ):
    return length*count + distance*(count+1)

def screen_size():
    return _pixels(N_ROWS, HEIGHT, MARGIN), _pixels(N_COLS, WIDTH, MARGIN)

class Terrain( pygame.Rect ):

    # Dyanamic grid content
    grid =      None
    highlight = None

    def __init__( self, left, top, width, height, row, col ):
        pygame.Rect.__init__(self, left, top, width, height)
        self.pos = (row, col)

        self.units = []

        self.row = row
        self.col = col

    def add_unit( self, unit ):
        self.units.append(unit)

    def remove_unit( self, unit ):
        self.units.remove(unit)

    def contains_unit( self, type=None ):
        for unit in self.units:
            if type is None or type==type(unit):
                return True
    
    def say_unit(self):
        for unit in self.units:
            return unit

    def up_terrain( self ):
        row = self.row - 1
        col = self.col
        if row < 0:
            return self
        else:
            return Terrain.grid[row][col]

    def down_terrain( self ):
        row = self.row + 1
        col = self.col
        if row >= len(Terrain.grid):
            return self
        else:
            return Terrain.grid[row][col]

    def left_terrain( self ):
        row = self.row
        col = self.col - 1
        if col < 0:
            return self
        else:
            return Terrain.grid[row][col]

    def right_terrain( self ):
        row = self.row
        col = self.col + 1
        if col >= len(Terrain.grid[row]):
            return self
        else:
            return Terrain.grid[row][col]

    def set_highlight( self ):
        Terrain.highlight = self

    def draw_border( self, screen, color ):

        left_rect = (self.left-MARGIN, self.top,      MARGIN, HEIGHT)
        pygame.draw.rect( screen, color, left_rect )

        top_rect = (self.left,       self.top-MARGIN, WIDTH,  MARGIN)
        pygame.draw.rect( screen, color, top_rect )

        right_rect = (self.right,    self.top,        MARGIN, HEIGHT)
        pygame.draw.rect( screen, color, right_rect )

        bottom_rect = (self.left,    self.bottom,     WIDTH,  MARGIN)
        pygame.draw.rect( screen, color, bottom_rect )

    def draw( self, screen ):
        pygame.draw.rect( screen, colors.WHITE, self )

        if self is Terrain.highlight:
            self.draw_border(screen, colors.BLUE)

def init_grid():
    Terrain.grid = []

    # Grid spacing
    x = MARGIN
    y = MARGIN
    for row_index in range(N_ROWS):
        row = []
        for col_index in range(N_COLS):
            row.append(Terrain(x, y, WIDTH, HEIGHT, row_index, col_index))
            x += WIDTH + MARGIN
        y += HEIGHT + MARGIN
        x = MARGIN

        Terrain.grid.append( row )

    #Terrain.grid[0][0].set_active()

def all():
    return [terrain for row in Terrain.grid for terrain in row]

def collision( pos ):
    
    for terrain in all():
        if terrain.collidepoint( pos ):
            return terrain
    
    return None

