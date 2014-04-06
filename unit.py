
from collections import deque
import unit #remove
import pygame

import colors
from terrain import Terrain

import manager

class Unit( object ):
    
    units  = deque()
    end_of_turn = 0

    @classmethod
    def activate_next( cls ):
        cls.units.rotate(1)

        cls.end_of_turn -= 1
        if cls.end_of_turn <= 0:
            turn_end( None )
            cls.end_of_turn = len( cls.units )

        manager.restore_default()
        manager.update_current( cls.active().active_listeners )

    @classmethod
    def active( cls ):
        return Unit.units[0]
    
    def __init__( self, terrain ):
        Unit.units.appendleft( self )

        self.growth = 0
        self.counter = 0
        self.hit = 0
        self.terrain = terrain
        self.terrain.add_unit( self )
        self.active_listeners = {
        }
    
    def set_counter(self, grab):
        self.counter = grab
    
    def set_hit(self, grab):
        self.hit = grab

    def delete( self ):
        self.terrain.remove_unit( self )
        Unit.units.remove( self )

    def is_surrounded( self, unit_type=None ):
        return (self.terrain.up_terrain()   .contains_unit(unit_type) and
                self.terrain.down_terrain() .contains_unit(unit_type) and
                self.terrain.left_terrain() .contains_unit(unit_type) and
                self.terrain.right_terrain().contains_unit(unit_type)    )

    def update( self, dt ):
        pass

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
    flower.Flower( Terrain.grid[4][4] )

    import rabbit
    rabbit.Rabbit( Terrain.grid[5][5] )

    Unit.activate_next()

def all():
    return Unit.units

def turn_end( event ):
    from flower import Flower
    from flower import Obstical
    dlist = []
    for unit in all():
        if unit.is_surrounded():
            unit.growth -= 2
        if isinstance (unit, Flower):
            unit.growth += (1 * unit.terrain.multiplier - unit.hit)
        if unit.growth < 1 and isinstance (unit, Obstical) == False:
            dlist.append(unit)
        print unit.counter
        if unit.counter > 1:
            unit.counter -= 1
            if unit.counter < 1:
                unit.hit = 0
                if isinstance (unit, Obstical):
                    dlist.append(unit)
    for unit in dlist:
       unit.delete()

