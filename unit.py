
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
    def action( cls, event ):
        active = cls.active()
        action = {
            pygame.K_UP:    active.action_up,
            pygame.K_DOWN:  active.action_down,
            pygame.K_LEFT:  active.action_left,
            pygame.K_RIGHT: active.action_right,
            pygame.K_SPACE: active.action_skip,
            pygame.K_a:     active.action_attack,
            pygame.K_d:     active.action_defend
        }

        return action[ event.key ]()

    def action_direction( self, action_terrain ):
        if action_terrain.contains_unit( type(self) ):
            return False
        else:
            Unit( action_terrain )
            return True

    def action_up( self ):
        action_terrain = self.terrain.up_terrain()
        return self.action_direction( action_terrain )

    def action_down( self ):
        action_terrain = self.terrain.down_terrain()
        return self.action_direction( action_terrain )

    def action_left( self ):
        action_terrain = self.terrain.left_terrain()
        return self.action_direction( action_terrain )

    def action_right( self ):
        action_terrain = self.terrain.right_terrain()
        return self.action_direction( action_terrain )
    
    def action_skip( self ):
        return True

    def action_attack( self ):
        return True

    def action_defend( self ):
        return True

    def __init__( self, terrain ):
        Unit.units.appendleft( self )

        self.growth = 0
        self.terrain = terrain
        self.terrain.add_unit( self )

    def delete( self ):
        self.terrain.remove_unit( self )
        Unit.units.remove(self)

    def is_surrounded( self, unit_type=None ):
        return (self.terrain.up_terrain()   .contains_unit(unit_type) and
                self.terrain.down_terrain() .contains_unit(unit_type) and
                self.terrain.left_terrain() .contains_unit(unit_type) and
                self.terrain.right_terrain().contains_unit(unit_type)    )

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

