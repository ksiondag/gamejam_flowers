
import pygame

import colors

# Terrain constants
WIDTH = 50
HEIGHT = 50
MARGIN = 5

N_ROWS    = 10
N_COLS = 10

def _pixels( count, length, distance ):
    return length*count + distance*(count+1)

def screen_size():
    return _pixels(N_ROWS, HEIGHT, MARGIN), _pixels(N_COLS, WIDTH, MARGIN)

class Terrain( pygame.Rect ):

    # Dyanamic grid content
    grid =      None

    active =    None
    highlight = None

    def __init__( self, left, top, width, height, row, col ):
        pygame.Rect.__init__(self, left, top, width, height)
        self.pos = (row, col)
        self.color = colors.WHITE

        self.row = row
        self.col = col

        # Terrain will contain units (flowers, rabbits, cake rolls, etc.)
        self.units = []

        # NOTE: depracated
        self.seed = False
        self.hit = 0
        self.growth = 0

    def change_color( self ):
        if self.color == colors.GREEN:
            self.color = colors.WHITE
        elif self.color == colors.WHITE:
            self.color = colors.GREEN

    def is_plant( self ):
        return self.color == colors.GREEN
    
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

    def set_active( self ):
        Terrain.active = self
    
    def set_highlight( self ):
        Terrain.highlight = self
    
    def draw_number( self, screen ):
        myfont = pygame.font.SysFont("monospace", 20)

        # render text
        label = myfont.render("%i" % self.growth, 1, colors.BLACK)
        screen.blit(label, (self))

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
        pygame.draw.rect( screen, self.color, self )
        self.draw_number( screen )

        if self is Terrain.highlight:
            self.draw_border(screen, colors.BLUE)
        if self is Terrain.active:
            self.draw_border(screen, colors.RED)


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

    Terrain.grid[0][0].set_active()

def all():
    return [terrain for row in Terrain.grid for terrain in row]

def collision( pos ):
    
    for terrain in all():
        if terrain.collidepoint( pos ):
            return terrain
    
    return None

