
from collections import deque

import pygame

import colors

class Unit( object ):
    
    units  = deque()
    active = None

    @classmethod
    def activate_next( cls ):
        Unit.units.rotate(1)

    @classmethod
    def active( cls ):
        return Unit.units[0]

    @classmethod
    def action_up( cls, event ):
        pass

    @classmethod
    def action_down( cls, event ):
        pass

    @classmethod
    def action_left( cls, event ):
        pass

    @classmethod
    def action_right( cls, event ):
        pass

    def __init__( self ):
        Unit.units.append( self )

        self.growth = 0

    def __del__( self ):
        Unit.units.remove( self )

    def draw_number( self, screen, terrain ):
        myfont = pygame.font.SysFont("monospace", 20)

        # render text
        label = myfont.render("%i" % self.growth, 1, colors.BLACK)
        screen.blit(label, terrain)

    def draw( self, screen, terrain ):
        pygame.draw.rect( screen, colors.GREEN, terrain )
        self.draw_number( screen, terrain )

        if self is Unit.active():
            terrain.draw_border(screen, colors.RED)

