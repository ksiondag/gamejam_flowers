
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
        self.multiplier = 1

        self.row = row
        self.col = col

        self._up = None
        self._down = None
        self._left = None
        self._right = None

    def add_unit( self, unit ):
        self.units.append(unit)

    def remove_unit( self, unit ):
        self.units.remove(unit)

    def contains_unit( self, unit_type=None ):
        for unit in self.units:
            if unit_type is None or unit_type==type(unit):
                return True
        return False
    
    def say_unit(self):
        for unit in self.units:
            return unit

    def up_terrain( self ):
        return self._up

    def down_terrain( self ):
        return self._down

    def left_terrain( self ):
        return self._left

    def right_terrain( self ):
        return self._right

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
        pygame.draw.rect( screen, colors.GREEN, self )

        if self is Terrain.highlight:
            self.draw_border(screen, colors.BLUE)

def init():
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

    for row_index in range(N_ROWS):
        for col_index in range(N_COLS):
            terrain = Terrain.grid[row_index][col_index]

            up_index    = row_index-1
            down_index  = row_index+1
            left_index  = col_index-1
            right_index = col_index+1

            if up_index >= 0:
                terrain._up = Terrain.grid[up_index][col_index]
            if down_index < len(Terrain.grid):
                terrain._down = Terrain.grid[down_index][col_index]
            if left_index >= 0:
                terrain._left = Terrain.grid[row_index][left_index]
            if right_index < len(Terrain.grid[row_index]):
                terrain._right = Terrain.grid[row_index][right_index]

def all():
    return [terrain for row in Terrain.grid for terrain in row]

def collision( pos ):
    
    for terrain in all():
        if terrain.collidepoint( pos ):
            return terrain
    
    return None

