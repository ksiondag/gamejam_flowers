
from collections import deque

import pygame

import colors
from terrain import Terrain

import manager


class Unit( object ):
    
    units  = deque()

    @classmethod
    def activate_next( cls ):
        Unit.units.rotate(1)
        manager.restore_default()
        manager.update_current( cls.active().active_listeners )

        #while Unit.active().is_surrounded():
            #Unit.units.rotate(1)

    @classmethod
    def active( cls ):
        return Unit.units[0]
    
    def __init__( self, terrain ):
        Unit.units.appendleft( self )

        self.growth = 0
        self.terrain = terrain
        self.terrain.add_unit( self )

        self.active_listeners = {
        }

    def delete( self ):
        self.terrain.remove_unit( self )
        Unit.units.remove( self )

    def is_surrounded( self ):
        unit_type = type( self )
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
        if self is Unit.active():
            self.terrain.draw_border(screen, colors.RED)

def init():
    import flower
    flower.Flower( Terrain.grid[0][0] )

    manager.restore_default()
    manager.update_current( Unit.active().active_listeners )

def all():
    return Unit.units

def turn_end( event ):
    dlist = []
    for unit in all():
        if unit.is_surrounded():
            unit.growth -= 2
        unit.growth += 1
        if unit.growth < 1:
            dlist.append(unit)
    for unit in dlist:
       unit.delete()

