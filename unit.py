
from collections import deque

import pygame

import colors
from terrain import Terrain


class Unit( object ):
    
    units  = deque()

    @classmethod
    def activate_next( cls ):
        Unit.units.rotate(1)
        while Unit.active().is_surrounded():
            Unit.units.rotate(1)

    @classmethod
    def active( cls ):
        return Unit.units[0]
    
    @classmethod
    def action( cls, action_terrain ):
        if cls.active().terrain is action_terrain or action_terrain.contains_unit():
            return False
        else:
            Unit( action_terrain )
            return True

    @classmethod
    def action_up( cls, event ):
        return cls.action( cls.active().terrain.up_terrain() )

    @classmethod
    def action_down( cls, event ):
        return cls.action( cls.active().terrain.down_terrain() )

    @classmethod
    def action_left( cls, event ):
        return cls.action( cls.active().terrain.left_terrain() )

    @classmethod
    def action_right( cls, event ):
        return cls.action( cls.active().terrain.right_terrain() )
    
    @classmethod
    def action_skip( cls, event ):
        return True

    def __init__( self, terrain ):
        Unit.units.appendleft( self )

        self.growth = 0
        self.terrain = terrain
        self.terrain.add_unit( self )

    def delete( self ):
        self.terrain.remove_unit( self )
        Unit.units.remove(self)

    def is_surrounded( self ):
        return (self.terrain.up_terrain()   .contains_unit() and
                self.terrain.down_terrain() .contains_unit() and
                self.terrain.left_terrain() .contains_unit() and
                self.terrain.right_terrain().contains_unit()    )

    def draw_number( self, screen ):
        myfont = pygame.font.SysFont("monospace", 20)

        # render text
        label = myfont.render("%i" % self.growth, 1, colors.BLACK)
        screen.blit(label, self.terrain)

    def draw( self, screen ):
        pygame.draw.rect( screen, colors.GREEN, self.terrain )
        self.draw_number( screen )

        if self is Unit.active():
            self.terrain.draw_border(screen, colors.RED)

def init_unit():
    Unit( Terrain.grid[0][0] )

def all():
    return Unit.units

